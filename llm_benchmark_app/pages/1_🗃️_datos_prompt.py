import streamlit as st
import datetime
import sqlite3
import pandas as pd 
from loguru import logger

from lib_llm_benchmark import staticals_functions
# from lib_llm_benchmark import utils


if __name__ == '__main__':

    begin_time = datetime.datetime.now()

##################################################

    st.set_page_config(page_title="Datos Prompts",page_icon="🗃️",)
    st.sidebar.header("🗃️ Datos Prompts")
    st.write("# 🗃️ Datos Prompts")
 
    with st.sidebar:
        st.sidebar.success("Selecciones la sección a Visitar")
        st.write('Esta app forma parte de la tesina final de la licenciatura en ciencia de Datos')
        st.markdown("""
                    Proyecto desarrollado por:
                    * [Emanuel Giannattasio](mailto:emanuel.giannattasio@gmail.com)
                    """) 
 
    path = "./llm_benchmark_app/db"
    con = sqlite3.connect(f'{path}/prompt_sqlite.db')
    # consulto los objetos de la BBDD para obtener los nombres de los modelos gemma_7b y llama2
    df_view = pd.read_sql_query("SELECT name FROM sqlite_master where type='view' and name not like 'extra_%' limit 2" , con)
    llm_df = pd.DataFrame()

    tab1, tab2, tab3= st.tabs(["Listado de Prompts"
                        , "Respuestas de los LLM"
                        , "Indicadores calculados"
                        ])

    with tab1:
        st.header("Prompts enviados a los LLM")
        st.markdown(f"""A continuacion se muestran los prompts, que se enviaron a los LLMs.
                        Se pueden visualizar las caracteristicas de dificultar que se le han asignado
                        a los mismos.            
                    """)
        df_set_prompt = pd.read_sql_query("SELECT * FROM set_1" , con)
        st.dataframe(df_set_prompt)

    with tab2:
        st.header(f"Respuestas del LLM")
        st.markdown(f"""A continuacion se muestran las respuestas a los prompts, que otorgo cada LLM                
                """)    
    
        for index, row in df_view.iterrows():
          logger.debug(f"tbl_name: {row['name']}, index {index}")
          name_tbl = df_view.iloc[index]['name']
          sql_query = f"SELECT id_promtp, answers FROM {name_tbl}" 
          df_prompts = pd.read_sql_query(sql_query, con)

          st.markdown(f"""### Respuestas del LLM {name_tbl.replace("_data1", "")}""")
          st.dataframe(df_prompts)

          llm_df = pd.concat([llm_df, staticals_functions.get_df_linguistics_statistics_values(df_prompts, name_tbl)])
 
    with tab3:          

        llm_df.columns = ['id_promtp', 'respuesta_llm', 'modelo llm', 'idioma', 'tiempo de lectura','cantidad de oraciones','cantidad de caracteres','cantidad de letras'
                        ,'cantidad de silabas','largo promedio de oraciones','promedio de letras por palabra','cantidad de stopwords'
                        ,'cantidad de palabras','densidad lexica','riqueza lexica', 'analisis sentimiento']
        st.header("Respuestas de los LLM con los indicadores calculados")
        st.markdown(f"""El dataframe que se visualiza a continuacion, es una concatenacion
                        de los dataframes que se encuentran en la solapa "Respuestas de los LLM";
                        a este se le han aplicados los calculos de indicadores, lo cuales figuran 
                        como columnas "agregadas".               
            """)
        st.dataframe(llm_df)

    llm_df = llm_df.reset_index(drop=True)  
    st.session_state["key"] = llm_df      
###################################################
    end_time = datetime.datetime.now()
    logger.debug(f'tiempo de ejecucion:{str(end_time - begin_time)}')