from streamlit_option_menu import option_menu
from streamlit_extras.stylable_container import stylable_container as stycont
from streamlit.components.v1 import html
import streamlit as st
import pandas as pd

def app():
    with open('Proyectos/P04/form01.css') as f:
        css = f.read()

    # Añade tu CSS
    st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)
    
    st.title('Proyecto 04: Machine Learning')
    
    c1, c2 = st.columns([1,5])
    with c1:
        #########################################################
        ##                       st.radio()                    ##
        #########################################################
        
        opt = st.radio("", ["Proyecto", "Referencias"], label_visibility="collapsed")
        
    with c2: 
        #########################################################
        ##                       st.radio                      ##
        #########################################################
        if opt == "Proyecto":
            st.markdown("## Resumen / Caso de estudio")
            
            st.markdown("## Marco Teórico")
            
            # A partir de aquí se escribe para el marco teórico
        if opt == "Referencias":
            st.markdown("## Referencias bibliográficas (marco teórico)")
            wpages1 = ['Anónimo. (n.d.) ¿Qué es el machine learning (ML)?, [En línea]. Recuperado de: https://www.ibm.com/es-es/topics/machine-learning']
            st.write(wpages1)
            
            st.markdown("## Referencias bibliográficas (documentación)")
            wpages2 = ['Anónimo, (n.d.). Streamlit-extras. Recuperado de: https://extras.streamlit.app','KaTeX. (2024). Supported Functions. Recuperado de: https://katex.org/docs/supported.html','Pandas documentation, (2024). pandas.DataFrame. Recuperado de: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html','Streamlit Inc. (n.d.). st.columns. Recuperado de: https://docs.streamlit.io/library/api-reference/layout/st.columns','Streamlit Inc. (n.d.). st.markdown. Recuperado de: https://docs.streamlit.io/library/api-reference/text/st.markdown','Streamlit Inc. (n.d.). st.radio. Recuperado de: https://docs.streamlit.io/library/api-reference/widgets/st.radio','Streamlit Inc. (n.d.). st.set_page_config. Recuperado de: https://docs.streamlit.io/library/api-reference/utilities/st.set_page_config', 'Streamlit Inc. (n.d.). st.slider. Recuperado de: https://docs.streamlit.io/library/api-reference/widgets/st.slider','Streamlit Inc. (n.d.). st.table. Recuperado de: https://docs.streamlit.io/develop/api-reference/data/st.table','Streamlit Inc. (n.d.). st.write. Recuperado de: https://docs.streamlit.io/library/api-reference/write-magic/st.write']
            st.write(wpages2)
            
