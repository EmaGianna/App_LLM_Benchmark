import streamlit as st
import datetime
import sqlite3
import pandas as pd 
from loguru import logger

from lib_llm_benchmark import staticals_functions
from lib_llm_benchmark import utils


if __name__ == '__main__':

    begin_time = datetime.datetime.now()

##################################################

    st.set_page_config(page_title="Datos Prompts",page_icon="🗃️",)
    st.sidebar.header("Datos Prompts")
    st.write("# Datos Prompts")
    
    #path = "/mnt/e/trabajo/sysberisso/GIT_REPOS/App_LLM_Benchmark/db"
    path = "./db"
    con = sqlite3.connect(f'{path}/prompt_sqlite.db')
    # consulto los objetos de la BBDD para obtener los nombres de los modelos gemma_7b y llama2
    df_view = pd.read_sql_query("SELECT name FROM sqlite_master where type='view' and name not like 'extra_%' limit 2" , con)
    llm_df = pd.DataFrame()
    
    st.markdown(f"""## Prompts enviados a los LLM Llama2 y Gemma""")
    df_set_prompt = pd.read_sql_query("SELECT * FROM set_1" , con)
    st.dataframe(df_set_prompt)

    for index, row in df_view.iterrows():
      logger.debug(f"tbl_name: {row['name']}, index {index}")
      name_tbl = df_view.iloc[index]['name']
      sql_query = f"SELECT id_promtp, answers FROM {name_tbl}" 
      df_prompts = pd.read_sql_query(sql_query, con)
      
      st.markdown(f"""## Respuestas del LLM {name_tbl.replace("_data1", "")}""")
      st.dataframe(df_prompts)
      
      llm_df = pd.concat([llm_df, staticals_functions.get_df_linguistics_statistics_values(df_prompts, name_tbl)])
           
    llm_df = llm_df.reset_index(drop=True)
    llm_df.columns = ['id_promtp', 'respuesta_llm', 'modelo llm', 'idioma', 'tiempo de lectura','cantidad de oraciones','cantidad de caracteres','cantidad de letras'
                    ,'cantidad de silabas','largo promedio de oraciones','promedio de letras por palabra','cantidad de stopwords'
                    ,'cantidad de palabras','densidad lexica','riqueza lexica', 'analisis sentimiento']
    

    logger.debug(f"df resume: {llm_df.info()}")

    st.session_state["key"] = llm_df

    with st.sidebar:
        st.sidebar.success("Selecciones la sección a Visitar")
        st.write('Esta app forma parte de la tesina final de la licenciatura en ciencia de Datos')
        st.markdown("""
                    Proyecto desarrollado por:
                    * [Emanuel Giannattasio](mailto:emanuel.giannattasio@gmail.com)
                    """)

    st.markdown(
        """
        ## Respuestas de los LLM y las estadisticas lingüisticas de las mismas

        """
    )
    st.dataframe(llm_df)

        
###################################################
    end_time = datetime.datetime.now()
    logger.debug(f'tiempo de ejecucion:{str(end_time - begin_time)}')