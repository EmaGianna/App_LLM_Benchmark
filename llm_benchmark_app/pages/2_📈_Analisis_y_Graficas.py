import streamlit as st
import datetime
import plotly.express as px
from lib_llm_benchmark import utils
from lib_llm_benchmark import st_functions 

if __name__ == '__main__':

    begin_time = datetime.datetime.now()

    st.set_page_config(page_title="Análisis y Gráficas",page_icon="📈",)
    st.sidebar.header("📈 Análisis y Gráficas")
    st.markdown("# 📈 Análisis y Gráficas")
    
    
    with st.sidebar:
        st.sidebar.success("Selecciones la sección a Visitar")
        st.write('Esta app forma parte de la tesina final de la licenciatura en ciencia de Datos')
        st.markdown("""
                    Proyecto desarrollado por:  
                    [📧 Emanuel Giannattasio](mailto:emanuel.giannattasio@gmail.com)
                    """)
        icon_size = 20
        st_functions.st_button('linkedin', 'https://www.linkedin.com/in/emanuel-giannattasio-76744911/', 'Follow me on LinkedIn', icon_size)
    
    st.markdown("""
                 En la presente seccion se presentan una serie de graficas que, muestran de modo 
                 visual el analisis que se realizo con los datos obtenidos.
                 """) 
    
    #########obtengo los datos para trabajalos en las graficas, analisis y rpts#####################
    llm_df = st.session_state["key"]
    # Subset con dato de Llama2
    df_llm_llama = llm_df[llm_df['modelo llm'] == 'llama2'].reset_index(drop=True)
    # Subset con dato de Gemma
    df_llm_gemma = llm_df[llm_df['modelo llm'] == 'gemma'].reset_index(drop=True)
    

    tab_comp_graph, tab_total_graph, tab_sentiment_graph, tap_rpt_comparison = st.tabs(["Grafica comparativa de valores"
                        , "Graficas de Totales"
                        , "Analisis de Sentimientos"
                        , "Reporte de Comparacion"
                        ])

    #############Graficas Lineas#######################################
    
    with tab_comp_graph:
        st.markdown('## **Graficas Comparativas**\n')
        #Creo copias para poder trabajar sobre estas y no afectar a los subsets originales
        df_gemma= df_llm_gemma.copy()
        df_llama= df_llm_llama.copy()
        df_num_gemma = utils.return_numeric_df(df_gemma)
        df_num_llama = utils.return_numeric_df(df_llama)

        utils.print_all_scatter_graph(df_num_llama, df_num_gemma, df_llm_llama, df_llm_gemma)


    ####### Graficos de Sentimientos ###########

    with tab_sentiment_graph:
        st.markdown('## **Graficas Del Analisis de Sentimientos**\n')
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

    with tab_total_graph:
        
        st.markdown('## **Graficas De Sumarizacion**\n')
        
        ## treemap
        # Crear una columna para el nombre de cada métrica
        numeric_cols = ['tiempo de lectura','cantidad de oraciones','cantidad de caracteres','cantidad de letras'
                    ,'cantidad de silabas','largo promedio de oraciones','promedio de letras por palabra','cantidad de stopwords'
                    ,'cantidad de palabras','densidad lexica','riqueza lexica']

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
                        , color_continuous_scale= 'Greens'
                        , hover_data=['modelo llm']
                        ,title='Icicle de valores numéricos por variable y modelo LLM')
        # Mostrar el gráfico
        st.plotly_chart(fig_icicle)


    #############RPT#######################################
    with tap_rpt_comparison:


        st.markdown("""      
                    Se realizó la comparación de los valores promedios de los indicadores obtenidos cuantitativos lingüísticos; 
                    vale mencionar que valores menores en cada caso, son mejores; por ejemplo, en el caso de tiempo de lectura, 
                    que es el primer valor comparado, se visualiza que es mejor en el LLM Gemma por sobre Llama2, 
                    lo que en ese ítem lo hace mejor; teniendo en cuenta lo antes dicho, generamos el siguiente reporte.
                         
                    """
                    )        
        st.divider() 
        utils.print_rpt_comparison(df_llm_gemma, df_llm_llama)
        st.divider() 
        st.markdown("""
                    Podemos observar que en los indicadores obtenemos que, de un total de 11 
                    indicadores los valores promedios de los indicadores de Gemma son mejores en 8 de ellos, 
                    mientras que solo 3 son mejores en el caso de Llama. Si esto lo expresáramos porcentualmente 
                    podríamos decir que Gemma es mejor en el 73% de los indicadores, por sobre un 27% de los indicadores de Llama2
                    """
                    )

    ##################################################
    end_time = datetime.datetime.now()