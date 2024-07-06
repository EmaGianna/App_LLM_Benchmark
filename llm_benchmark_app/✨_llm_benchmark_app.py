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

    st.set_page_config(page_title="Open Source LLM Benchmark",page_icon="✨",)
    st.sidebar.header("Open Source LLM Benchmark")
    st.write("# Open Source LLM Benchmark")
    
    with st.sidebar:
        st.sidebar.success("Selecciones la sección a Visitar")
        st.write('Esta app forma parte de la tesina final de la licenciatura en ciencia de Datos')
        st.markdown("""
                    Proyecto desarrollado por:
                    * [Emanuel Giannattasio](mailto:emanuel.giannattasio@gmail.com)
                    """)

    st.markdown(
        """
        # Escribir en formato markdown

        """
    )
    
        
###################################################
    end_time = datetime.datetime.now()
    logger.debug(f'tiempo de ejecucion:{str(end_time - begin_time)}')