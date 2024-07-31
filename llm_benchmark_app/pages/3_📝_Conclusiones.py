import streamlit as st
import datetime
import sqlite3
import pandas as pd 


from lib_llm_benchmark import staticals_functions



if __name__ == '__main__':

    begin_time = datetime.datetime.now()
    st.set_page_config(page_title="Conclusiones",page_icon="📝",)
    st.sidebar.header("📝 Conclusiones")
    st.write("# 📝 Conclusiones")
    
    with st.sidebar:
        st.sidebar.success("Selecciones la sección a Visitar")
        st.write('Esta app forma parte de la tesina final de la licenciatura en ciencia de Datos')
        st.markdown("""
                    Proyecto desarrollado por:
                    * [📧 Emanuel Giannattasio](mailto:emanuel.giannattasio@gmail.com)
                    """) 
##################################################

    st.markdown("""
                De los análisis antes enunciados, podemos determinar que, en el orden de los LLMs entrenados con 7 mil millones de parámetros,
                Gemma (el LLM de Google), tiene mejor performance que Llama2 (el LLM de Meta). 
                
                No obstante, estos LLM siguen evolucionando y recientemente Meta lanzo Llama3, que es una evolución de Llama2, 
                pero el entrenamiento se realizó con 8 mil millones de parámetros. 
                Y como se mencionó anteriormente, la comparación se realizó con LLMs que tengan la misma magnitud de entrenamiento.               
                """)

##################################################
    end_time = datetime.datetime.now()