import plotly.graph_objects as go
import streamlit as st
import pandas as pd 


def list_to_dict(in_list):
    """
    The function `list_to_dict` converts a list into a dictionary where the index of each element in the
    list becomes the key in the dictionary.
    
    :param in_list: Thank you for providing the code snippet. Could you please provide an example of the
    `in_list` that you would like to convert to a dictionary using the `list_to_dict` function?
    :return: The function `list_to_dict` is returning a dictionary where the keys are the indices of the
    elements in the input list `in_list`, and the values are the elements themselves.
    """
    dict_ = {}
    for i, valor in enumerate(in_list):
        dict_[i] = valor

    return dict_


def  return_numeric_df(df):
    """
    The function `return_numeric_df` selects numeric columns from a DataFrame and renames the columns
    with specific names.
    
    :param df: It looks like the function `return_numeric_df` takes a DataFrame as input and returns a
    new DataFrame containing only the columns with numeric data types. Additionally, it renames the
    columns of the new DataFrame with specific names
    :return: A DataFrame containing only the columns with numeric data types, with renamed columns.
    """
    df = df.select_dtypes(include=['number'])
    #df.columns = ['id_promtp','tiempo de lectura','cantidad de oraciones','cantidad de caracteres','cantidad de letras'
    #            ,'cantidad de silabas','largo promedio de oraciones','promedio de letras por palabra','cantidad de stopwords'
    #            ,'cantidad de palabras','densidad lexica','riqueza lexica']
    return df

def create_scatter_graph(df_llama, df_gemma, column):
    """
    The function `create_scatter_graph` generates a scatter graph comparing data from two DataFrames for
    a specified column.
    
    :param df_llama: The `df_llama` parameter is a DataFrame containing data related to the Llama model.
    It likely includes columns such as 'id_prompt' and the specified `column` for comparison in the
    scatter graph. The function `create_scatter_graph` uses this DataFrame to plot a scatter graph
    comparing the
    :param df_gemma: The `df_gemma` parameter is a DataFrame containing data related to Gemma. It is
    used in the `create_scatter_graph` function to plot a scatter graph comparing a specific column
    between Gemma and Llama
    :param column: The `create_scatter_graph` function you provided seems to be creating a scatter graph
    using Plotly to compare data between two dataframes (`df_llama` and `df_gemma`) based on a specified
    column
    """

    # Crear la figura
    fig = go.Figure()
    # Añadir la primera gráfica de líneas (Llama)
    fig.add_trace(go.Scatter(x=df_llama['id_promtp'], 
                             y=df_llama[column],
                             mode='lines+markers', 
                             name='Llama',
                             #line=dict(color='blue'),
                             #marker=dict(color='blue')
                             )
                    )

    # Añadir la segunda gráfica de líneas (Gemma)
    fig.add_trace(go.Scatter(x=df_gemma['id_promtp'], 
                             y=df_gemma[column],
                             mode='lines+markers',
                             name='Gemma',
                             #line=dict(color='red'),
                             #marker=dict(color='red')
                             )
                  )

    # Configurar el título y los ejes
    fig.update_layout(
        title=f'Comparación de {column}',
        xaxis_title='ID Prompt',
        yaxis_title=column,
        legend_title='Modelo LLM',
        xaxis=dict(
            tickmode='linear',  # Usar modo de ticks lineal
            tick0=1,            # Primer tick en el valor 1
            dtick=1             # Distancia entre ticks igual a 1
        )
    )
    # Mostrar el gráfico
    st.plotly_chart(fig)

def print_all_scatter_graph(df_num_llama, df_num_gemma, df_llm_llama, df_llm_gemma):
    """
    The function `print_all_scatter_graph` creates scatter graphs for numerical columns in two
    DataFrames, compares the values, determines the better indicator, and displays the results.
    
    :param df_num_llama: It looks like the code snippet you provided is a function that generates
    scatter graphs and compares values between two DataFrames. However, the definition of `df_num_llama`
    is missing in the code snippet you shared. Could you please provide the definition of `df_num_llama`
    so that I can
    :param df_num_gemma: It looks like the code snippet you provided is a function that generates
    scatter graphs and compares values between two DataFrames. However, the definition of `df_num_gemma`
    is missing in the code snippet you shared
    """

    cols = df_num_gemma.columns.drop('id_promtp')
    columnas = st.multiselect('Elija Área/País: ', cols, cols[0])
    
    for col in columnas:
        #if col != 'id_promtp':
        create_scatter_graph(df_num_llama, df_num_gemma, col)

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


def print_rpt_comparison(df_llm_gemma, df_llm_llama):
    """
    The function `print_rpt_comparision` compares the average values of numeric columns between two
    dataframes and generates a report highlighting the differences.
    
    :param df_llm_gemma: The function `print_rpt_comparision` compares the average values of numeric
    columns between two DataFrames `df_llm_gemma` and `df_llm_llama`. It calculates the average values
    for each numeric column in both DataFrames and then compares them to determine which DataFrame has
    better average
    :param df_llm_llama: The function `print_rpt_comparision` compares the average values of different
    numeric columns between two dataframes `df_llm_gemma` and `df_llm_llama`. It calculates the average
    values for each numeric column in both dataframes and then compares them to determine which
    dataframe has better
    """
    # Comparacion de los valores de cada indicador obtenido para llama2 y gemma
    numeric_cols = ['tiempo de lectura','cantidad de oraciones','cantidad de caracteres','cantidad de letras'
                ,'cantidad de silabas','largo promedio de oraciones','promedio de letras por palabra','cantidad de stopwords'
                ,'cantidad de palabras','densidad lexica','riqueza lexica']

    #Promedio los valores de cada variables/columnas numericas de gemma y las guardo en un diccionario
    dict_prom_gemma = df_llm_gemma[numeric_cols].mean().to_dict()
    #Promedio los valores de cada variables/columnas numericas de llama2 y las guardo en un diccionario
    dict_prom_llama2 = df_llm_llama[numeric_cols].mean().to_dict()

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