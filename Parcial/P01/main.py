# import pickle # Se importa la librería de pickle
# from pathlib import Path #Se importa la librería Path
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
# import streamlit_authenticator as stauth

import P01_home, P01_inp, P01_sl

st.set_page_config( #Configuración de la página, titulo e ícono
    page_title="F502 - Parcial 01", #Coloca titulo a la página
    page_icon=':virgo:', #Icóno de la página
    layout="wide"
)

class MultiApp: # Declarando que es una aplicación con múltiples páginas
    def __init__(self):
        self.apps = [] 
    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })
    # Configurar el inicio de la web multipágina
    def run():
        with st.sidebar: # Se hara una barra en donde estarán las diferentes páginas
            app = option_menu(
                menu_title='Páginas ',
                options=['Home','Descripción', 'Input Number', 'Slider'], # Nombre de cada pestaña
                icons=['house-fill', 'bezier', 'bezier2', 'body-text'], #Iconos de las pestañas
                menu_icon='chat-text-fill',
                default_index=1,
                styles={
                    "container": {"padding": "5!important", "background-color":'black'},
                    "icon":{"color":"white", "font-size":"23px"},
                    "nav-link":{"color":"white", "font-size": "20px", "text-align":"left", "margin":"0px","--hover-color":"sepia"},
                    "nav-link-selected":{"background-color":"02ab21"}
                }
            )
        if app == 'Home':
            # Declarando las columnas con tamaño relativo
            C1, C2 = st.columns([1,4])
            with C1:
                st.title('Contenidos')
                tog = st.toggle('Expandir')
                if tog:
                    opt = st.radio('', ["***Descripción***", "***Input***", "***Slider***"])
                    
                    if opt == '***Descripción***':
                        st.markdown('### Inicio')
                        st.write('En esta sección se comentará acerca de lo que se realizó en el documento.')
                        img02 = Image.open('Parcial/P01/img/img02.jpg')
                        st.image(img02)
                        
                    if opt == '***Input***':
                        st.markdown('### Input Number')
                        st.write('En esta sección se observará la distribución binomial a partir de cuadros en donde se ingresan los valores pedidos.')
                        img03 = Image.open('Parcial/P01/img/img03.jpg')
                        st.image(img03)
                        
                    if opt == '***Slider***':
                        st.markdown('### Slider')
                        st.write('En esta sección se observará la distribución binomial a partir de sliders en los cuales se seleccionaran los valores pedidos.')
                        img04 = Image.open('Parcial/P01/img/img04.jpg')
                        st.image(img04)
                
            with C2:
                img = Image.open('Img/img01.png')
                st.image(img)
                
        if app == "Descripción":
            P01_home.app()
            
        if app == "Input Number":
            P01_inp.app()
            
        if app == "Slider":
            P01_sl.app()
        
    run()