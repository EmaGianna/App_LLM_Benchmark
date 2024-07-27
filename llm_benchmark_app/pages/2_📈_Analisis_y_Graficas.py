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

    st.set_page_config(page_title="Análisis y Gráficas",page_icon="📈",)
    st.sidebar.header("Análisis y Gráficas")
    st.write("# Análisis y Gráficas")
##################################################
    end_time = datetime.datetime.now()
    logger.debug(f'tiempo de ejecucion:{str(end_time - begin_time)}')