#https://python-graph-gallery.com/

import streamlit as st
import datetime
import sqlite3
import pandas as pd 
from loguru import logger
import plotly.express as px

from lib_llm_benchmark import staticals_functions
from lib_llm_benchmark import utils


if __name__ == '__main__':

    begin_time = datetime.datetime.now()

    st.set_page_config(page_title="Análisis y Gráficas",page_icon="📈",)
    st.sidebar.header("📈 Análisis y Gráficas")
    st.markdown("# 📈 Análisis y Gráficas")
##################################################

    llm_df = st.session_state["key"]
    # Subset con dato de Llama2
    df_llm_llama = llm_df[llm_df['modelo llm'] == 'llama2'].reset_index(drop=True)
    # Subset con dato de Gemma
    df_llm_gemma = llm_df[llm_df['modelo llm'] == 'gemma'].reset_index(drop=True)
    # Comparacion de los valores de cada indicador obtenido para llama2 y gemma
    numeric_cols = ['tiempo de lectura','cantidad de oraciones','cantidad de caracteres','cantidad de letras'
                ,'cantidad de silabas','largo promedio de oraciones','promedio de letras por palabra','cantidad de stopwords'
                ,'cantidad de palabras','densidad lexica','riqueza lexica']

    #Promedio los valores de cada variables/columnas numericas de gemma y las guardo en un diccionario
    dict_prom_gemma = df_llm_gemma[numeric_cols].mean().to_dict()
    #Promedio los valores de cada variables/columnas numericas de llama2 y las guardo en un diccionario
    dict_prom_llama2 = df_llm_llama[numeric_cols].mean().to_dict()

    #############RPT#######################################

    keys = dict_prom_gemma.keys()
    st.markdown('## **Reporte de Comparación**\n')

    for key in keys:
        st.markdown(f'### **Comparacion del promedio de {key}**')
        if dict_prom_gemma[key] == dict_prom_llama2[key]:
            st.markdown( f"""El valor promedio de los valores obtenidos para {key} son identicos. 
                             No se puede determinar cual es el mejor en este aspecto\n
                            gemma: {round(dict_prom_gemma[key], 2)} - llama2: {round(dict_prom_llama2[key], 2)}
                            """
                        )
        elif dict_prom_gemma[key] < dict_prom_llama2[key]:
            st.markdown( f"""El valor promedio de los valores obtenidos para {key} son mejores en gemma:7b por sobre llama2\n.
                             gemma: {round(dict_prom_gemma[key], 2)} - llama2: {round(dict_prom_llama2[key], 2)}\n"""
                        )
        elif dict_prom_gemma[key] > dict_prom_llama2[key]:
            st.markdown( f"""El valor promedio de los valores obtenidos para {key} son mejores en llama2 por sobre gemma\n.
                           gemma: {round(dict_prom_gemma[key], 2)} - llama2: {round(dict_prom_llama2[key], 2)}\n""")
        else:
            st.text( f'Para el indicador promedio {key} no se puede determinar benchmark\n')


    #############Graficas#######################################
    
    st.markdown('## **Graficas**\n')
    
    #Creo copias para poder trabajar sobre estas y no afectar a los subsets originales
    df_gemma= df_llm_gemma.copy()
    df_llama= df_llm_llama.copy()
    df_num_gemma = utils.return_numeric_df(df_gemma)
    df_num_llama = utils.return_numeric_df(df_llama)

    ####### Graficos de lineas ###########
    def print_all_scatter_graph(df_num_llama, df_num_gemma):

        columnas = df_num_gemma.columns
        for col in columnas:
            if col != 'id_promtp':
                utils.create_scatter_graph(df_num_llama, df_num_gemma, col)

                # Concatenar los DataFrames con sufijos
                df_compare = pd.concat([
                    df_llm_gemma[['modelo llm', col]].add_suffix("_gemma"),
                    df_llm_llama[['modelo llm', col]].add_suffix("_llama")
                ], axis=1)

                # Comparar los valores y determinar el mejor indicador
                mejor_indicador = df_compare[[f'{col}_gemma', f'{col}_llama']].apply(
                    lambda row: 'gemma' if row[f'{col}_gemma'] < row[f'{col}_llama'] else (
                        'llama2' if row[f'{col}_gemma'] > row[f'{col}_llama'] else 'iguales'
                    ), axis=1
                )

                # Añadir la columna resultante al DataFrame original
                df_compare['mejor_llm'] = mejor_indicador
                # Agrupar y contar por el campo mejor_llm
                resultado = df_compare.groupby('mejor_llm').size().reset_index(name='cantidad')
                # Mostrar el resultado
                st.markdown(f"""**La grafica precedente se realizo con el siguiente set de datos:**""")
                st.dataframe(resultado)
    
    print_all_scatter_graph(df_num_llama, df_num_gemma)

    ####### Graficos de Sentimientos ###########

    df_char_gemma = df_gemma.select_dtypes(include=['object'])
    df_char_llama = df_llama.select_dtypes(include=['object'])
    
    col = 'analisis sentimiento'
    
    #### gemma ####
    df_llm_gemma[['modelo llm', col]].value_counts().reset_index()
    fig = px.bar(df_llm_gemma[['modelo llm', col]].value_counts().reset_index()
                 , x='analisis sentimiento'
                 , y='count'
                 , color='analisis sentimiento'
                 , title='Distribución de Análisis de Sentimientos para Gemma')
    # Personalizar el diseño del gráfico
    fig.update_layout(
        xaxis_title='Análisis Sentimiento',
        yaxis_title='Cantidad',
        showlegend=False
    )
    # Mostrar el gráfico
    st.plotly_chart(fig)

    
    #### llama  ####
    df_llm_llama[['modelo llm', col]].value_counts().reset_index()

    fig = px.bar(df_llm_llama[['modelo llm', col]].value_counts().reset_index()
                 , x='analisis sentimiento'
                 , y='count'
                 , color='analisis sentimiento'
                 , title='Distribución de Análisis de Sentimientos para Llama2')

    # Personalizar el diseño del gráfico
    fig.update_layout(
        xaxis_title='Análisis Sentimiento',
        yaxis_title='Cantidad',
        showlegend=False
    )

    # Mostrar el gráfico
    st.plotly_chart(fig)

    ####### Graficos de Otros ###########
    ## treemap
    # Crear una columna para el nombre de cada métrica
    llm_df_long = llm_df.melt(
        id_vars=['id_promtp', 'modelo llm'],
        value_vars=numeric_cols,
        var_name='metric_name',
        value_name='metric_value'
    )

    # Creación de la gráfica treemap
    fig_treemap = px.treemap(
        llm_df_long,
        path=[px.Constant('marcador lingüistico'),'metric_name', 'modelo llm'],
        values='metric_value',  # Ajusta esto si deseas usar otra métrica como tamaño
        color='metric_value',  # Ajusta esto si deseas colorear basado en otra métrica
        color_continuous_scale='Blues',
        title='Treemap de valores numéricos por variable y modelo LLM'
    )

    # Mostrar el gráfico
    st.plotly_chart(fig_treemap)


    ## sunburst
    fig_sunburst = px.sunburst(llm_df_long, 
                      path=['modelo llm','metric_name'], 
                      values='metric_value',
                      color='metric_value', #'metric_name', 
                      color_continuous_scale= 'Purples', #'Greens', #'Blues',
                      hover_data=['modelo llm'],
                      title='Sunburst de valores numéricos por variable y modelo LLM'
                      )
    # Mostrar el gráfico
    st.plotly_chart(fig_sunburst)
    
    ##icicle
    fig_icicle = px.icicle(llm_df_long
                    , path=[px.Constant('llm'),'modelo llm','metric_name']
                    , values='metric_value'
                    , color='metric_value'
                    ,color_continuous_scale= 'Greens'
                    , hover_data=['modelo llm'])
    # Mostrar el gráfico
    st.plotly_chart(fig_icicle)

##################################################
    end_time = datetime.datetime.now()
    logger.debug(f'tiempo de ejecucion:{str(end_time - begin_time)}')