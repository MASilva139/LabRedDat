import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_extras.stylable_container import stylable_container as stycont
from PIL import Image as im
import os

import P04_p01, P04_p02, P04_p03
#print(os.path.abspath('form01.css'))
#with open('form01.css') as f:
#    css = f.read()
#st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)
try:
    st.set_page_config(
        page_title="Proyecto 04",
        page_icon=':shinto_shrine:',
        layout="wide"
    )
    #https://github.com/MathCatsAnd/Streamlit-Mechanics-Examples/blob/main/pages/column_selector_v2.py
    with open('Proyectos/P04/form01.css') as f:
        css = f.read()

    # Añade tu CSS
    st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)
    
    class MultiApp:
        def __init__(self):
            self.apps = []
        def add_app(self, tittle, func):
            self.apps.append({
                "title": tittle,
                "function": func
            })
        def run():
            if 'app' not in st.session_state:
                st.session_state.app = 'Inicio'
            with stycont(
                key="opt_menu",
                css_styles="""
                """,
            ):
                st.session_state.app = option_menu(
                    #menu_title='Pages',
                    None,
                    options=['Inicio', 'Proyecto', 'Conclusiones'], # Nombre de cada pestaña
                    icons=['house-fill', 'bezier', 'body-text'], #Iconos de las pestañas
                    menu_icon='alt',
                    default_index=0, # En este se define la primera página en mostrarse,
                    orientation="horizontal",
                    styles={
                        "container": {"padding": "1!important", "background-color":'#353535'},
                        "icon":{"color":"white", "font-size":"16px"},
                        "nav-link":{
                            "color":"white", 
                            "font-size": "15px", 
                            "text-align":"center", 
                            "margin":"0px",
                            "--hover-color":"#0f0f0f"
                        },
                        "nav-link-selected":{
                            "background-color":"#000",
                            "color": "#fff"
                        }
                    }
                )
            if st.session_state.app == "Inicio":
                P04_p01.app()
                
            if st.session_state.app == "Proyecto":
                P04_p02.app()
                
            if st.session_state.app == "Conclusiones":
                P04_p03.app()

        run()
    pass
except FileNotFoundError:
    st.error("No se encontró el archivo de configuración")