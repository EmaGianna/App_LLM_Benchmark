# emojis: https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
#          https://github.com/ikatyang/emoji-cheat-sheet/blob/master/README.md
          
# markdown: https://github.github.com/gfm/#example-581
#           https://docs.github.com/es/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax
#           https://github.com/ipython/ipython/wiki/Cheatsheet

##cafecito
#https://www.google.com/search?q=cafecito&oq=cafecit&gs_lcrp=EgZjaHJvbWUqDggAEEUYJxg7GIAEGIoFMg4IABBFGCcYOxiABBiKBTIGCAEQRRg5MgcIAhAAGIAEMg0IAxAAGIMBGLEDGIAEMgcIBBAAGIAEMgYIBRBFGD0yBggGEEUYPDIGCAcQRRg80gEIMTgxMGowajeoAgCwAgA&sourceid=chrome&ie=UTF-8
## buy me a coffe
#https://www.google.com/search?client=firefox-b-d&q=buy+me+a+coffe

import streamlit as st
import datetime
import sqlite3
import pandas as pd 
from loguru import logger

#from lib_llm_benchmark import staticals_functions
#from lib_llm_benchmark import utils


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
                    * [📧 Emanuel Giannattasio](mailto:emanuel.giannattasio@gmail.com)
                    """)

    st.markdown(
        """
        # ✨Benchmark de LLMs  
        
        En la presente web, podra encontrar un benchmarking de LLMs (Large Lenguage Model) open source, que se ejecuten 
        en la herramienta [Ollama](https://ollama.com/library) desde la perspectiva de indicadores cuantitativos lingüisticos.
        
        
        ## ✨LLM
        
        Al momento de liberar esta web, el benchmarking fue realizado sobre las versiones con 7b de parametros 
        para [llama2](https://llama.meta.com/llama2/) y [gemma](https://ai.google.dev/gemma?hl=es-419); con el correr del tiempo se ira actualizando con otros modelos.
        Tambien aspiramos a superar nuestras limitaciones de hardware, para poder realizar benchmarks 
        en modelos con mayor consumo computacional
        
        
        ## Objetivo

        El objetivo del presente trabajo es el desarrollo de un framework de comparación independiente para 
        LLMs utilizando diversas herramientas del ambiente Open Source (librerias de python principalmente)


        """
    )
    
        
###################################################
    end_time = datetime.datetime.now()
    logger.debug(f'tiempo de ejecucion:{str(end_time - begin_time)}')