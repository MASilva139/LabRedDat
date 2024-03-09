import streamlit as st
from streamlit_option_menu import option_menu as stom
from PIL import Image as im

import home, proyecto

st.set_page_config(
    page_title="Proyecto 01",
    page_icon=':frog:',
    layout="wide",
    initial_sidebar_state="collapsed",
    menu_items={
        'About': "# XD"
    }
)

class MultiApp:
    def __init__(self):
        self.apps = []
    def add_app(self, tittle, function):
        self.apps.append({
            "title": tittle,
            "function": function
        })
    def run():
        with st.sidebar: # Se hara una barra en donde estarán las diferentes páginas
            app = stom(
                menu_title='Páginas ',
                options=['Menú','Inicio', 'Proyecto', 'Slider'], # Nombre de cada pestaña
                icons=['house-fill', 'bezier', 'bezier2', 'body-text'], #Iconos de las pestañas
                menu_icon='alt',
                default_index=0,
                styles={
                    "container": {"padding": "5!important", "background-color":'black'},
                    "icon":{"color":"white", "font-size":"15px"},
                    "nav-link":{"color":"white", "font-size": "12px", "text-align":"left", "margin":"0px","--hover-color":"sepia"},
                    "nav-link-selected":{"background-color":"darkolivegreen"}
                }
            )
        if app == "Proyecto":
            proyecto.app()
    run()