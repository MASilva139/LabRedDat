import streamlit as st
from streamlit_option_menu import option_menu as stom
from PIL import Image as im

def app():
    c1, c2 = st.columns([1,5])
    with c1:
        opt = st.radio(
            "***SECCIONES:***", ["Marco Teórico", "Problema"]
        )
    
    with c2:   
        if opt == "Marco Teórico":
            st.title("Marco Teórico")
            
        if opt == "Problema":
            st.title("Definición del problema o caso de estudio")
    # with c2:
        # if opt == ""