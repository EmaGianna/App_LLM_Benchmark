# emojis: https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
#          https://github.com/ikatyang/emoji-cheat-sheet/blob/master/README.md
          
# markdown: https://github.github.com/gfm/#example-581
#           https://docs.github.com/es/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax
#           https://github.com/ipython/ipython/wiki/Cheatsheet


## Streamlit DOC
#https://docs.streamlit.io/


##cafecito
#https://www.google.com/search?q=cafecito&oq=cafecit&gs_lcrp=EgZjaHJvbWUqDggAEEUYJxg7GIAEGIoFMg4IABBFGCcYOxiABBiKBTIGCAEQRRg5MgcIAhAAGIAEMg0IAxAAGIMBGLEDGIAEMgcIBBAAGIAEMgYIBRBFGD0yBggGEEUYPDIGCAcQRRg80gEIMTgxMGowajeoAgCwAgA&sourceid=chrome&ie=UTF-8
## buy me a coffe
#https://www.google.com/search?client=firefox-b-d&q=buy+me+a+coffe

import streamlit as st
import datetime
import sqlite3
import pandas as pd 
#from loguru import logger

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
                **Bienvenidos!!** Aqui podra encontrar un benchmarking de LLMs (Large Lenguage Model) open source, que se ejecuten 
                en la herramienta [Ollama](https://ollama.com/library) desde la perspectiva de indicadores cuantitativos lingüisticos.
                
                Al momento de liberar esta web, el benchmarking fue realizado sobre las versiones con 7b de parametros
                de entrenamiento que disponibilizan [llama2](https://llama.meta.com/llama2/) y [gemma](https://ai.google.dev/gemma?hl=es-419); 
                con el correr del tiempo se ira actualizando con otros modelos.  
                Tambien aspiramos a superar nuestras limitaciones de hardware, para poder realizar benchmarks 
                en modelos con mayor consumo computacional
                """             
              )

    tab_con_ini, tab_fram_llm, tab_indicadores = st.tabs(["Consideraciones Iniciales"
                        , "Framework de Benchmark LLM"
                        , "Indicadores seleccionados"
                        ])

    with tab_con_ini:
        st.markdown(
            """
            ## Objetivo

            El objetivo del presente trabajo es el desarrollo de un framework de comparación independiente para 
            LLMs utilizando diversas herramientas del ambiente Open Source (librerias de python principalmente)


            ## Seleccion de los LLM

            Por esta razón es que se decidió desarrollar una serie de métricas para realizar la evaluación de un LLM frente a otro. 
            Se eligieron los LLM Open Source de dos de las compañías de tecnología más grandes e innovadoras 
            Llama2 de Meta y Gema de Google, en ambos casos, para que la comparación/benchmark sea justo, 
            se eligieron las versiones que fueron entrenadas con 7 mil millones de parámetros en cada caso; 
            es decir la parametrización de entrenamiento de ambos modelos de LLM, a nivel numérico cuantitativo 
            son idénticas (no tenemos certeza si son los mismos sets de parámetros a nivel cualitativo).

            """
        )
    
        col_gemma, col_llama = st.columns(2)

        with col_gemma:
            st.image('./llm_benchmark_app/img/gemma.jpg', caption="gemma")

        with col_llama:
            st.image('./llm_benchmark_app/img/llama2.jpg', caption="llama2")
    
    
    with tab_fram_llm:
        st.markdown(
            """ 
            ## Descripción del experimento	

            El experimento consta del envío de una cantidad finita de prompts a los LLMs, 
            los cuales otorgaran una respuesta a los mismos. Los prompts enviados a LLMs serán los mismos en cada caso.
            Las respuestas se almacenarán en una base de datos; de cada respuesta se obtendrán estadísticas 
            léxicas para cada respuesta de cada LLM y se realizarán comparaciones entre las mismas, 
            obteniendo indicadores particulares con los que se llegara a la conclusión de que LLM fue 
            el que mejor desempeño tuvo de acuerdo a las mismas.
            """
        )
        
        
        st.image('./llm_benchmark_app/img/Diagrama_Benchmark.jpg', caption="Diagrama de Flujo de Procesamiento")
        
        
    with tab_indicadores:
        st.markdown(
            """ 
            ## Indicadores seleccionados	

            *	**Tiempo de lectura (Reading Time):** Indica el tiempo aproximado de lectura del texto.

            *	**Conteo de oraciones (Sentence Count):** Es el número de oraciones que se encuentran en el texto.

            *	**Conteo de Caracteres (Character Count):** Es el número de caracteres que se encuentran en el texto (esto incluye signos de puntuación).

            *	**Conteo de letras (Letter Count):** Es el número de caracteres que se encuentran en el texto (esto excluye signos de puntuación).

            *	**Conteo de palabras (Lexicon count):** Es la cantidad de palabras presentes en el texto.

            *	**Largo promedio de oraciones (Average sentence length):** Es el largo promedio de las oraciones medido en cantidad de palabras en la misma. 

            *	**Promedio de letras por palabra (Average letters per Word):**  Es el número promedio de letras por palabras en el texto.

            *	**Cantidad de Stopwors (Quantity Stopwords):** Es la cantidad de stopwords contenidas en el texto.

            *	**Cantidad de Palabras (Quantity Words):** Es la cantidad de palabras presentes en el texto.

            *	**Densidad Léxica (Lexical Density):** Es la densidad léxica, calculada como la cantidad de palabras sin repetición dividido por la cantidad total de palabras

            *	**Riqueza Léxica (Lexical Richness):** Es la densidad léxica expresada en porcentajes al multiplicar la mencionada por 100.

            *	**Análisis de Sentimiento (Analyze Sentiment):** Es el valor que se obtiene del análisis de sentimientos expresado en Neutro, Negativo, Positivo.

            ## **Mas Detalles**
            
            Para obtener mas detalles, los invito a visitar 
            el siguiente [documento](https://github.com/EmaGianna/LLM_Benchmark/blob/main/documents/Benchmark%20de%20Respuesta%20de%20LLMs%20desde%20la%20perspectiva%20de%20indicadores%20ling%C3%BC%C3%ADsticos.pdf)
            o bien el [repositorio raiz](https://github.com/EmaGianna/LLM_Benchmark) donde encontrara los codigos fuentes
            para experimentar (Ante dudas o consultas pueden contactarme al mail que figura en la barra lateral).
            
            """
        )
        
        
        
###################################################
    end_time = datetime.datetime.now()
#    logger.debug(f'tiempo de ejecucion:{str(end_time - begin_time)}')