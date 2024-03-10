import streamlit as st
from streamlit_option_menu import option_menu as stom
from PIL import Image as im

import home, proyecto, final

st.set_page_config(
    page_title="Proyecto 01",
    page_icon=':frog:',
    layout="wide",
    initial_sidebar_state="collapsed"
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
                options=['Inicio','Descripción', 'Proyecto', 'Conclusiones'], # Nombre de cada pestaña
                icons=['house-fill', 'bezier', 'bezier2', 'body-text'], #Iconos de las pestañas
                menu_icon='alt',
                default_index=0,
                styles={
                    "container": {"padding": "3!important", "background-color":'black'},
                    "icon":{"color":"white", "font-size":"18px"},
                    "nav-link":{"color":"white", "font-size": "15px", "text-align":"left", "margin":"0px","--hover-color":"sepia"},
                    "nav-link-selected":{"background-color":"darkolivegreen"}
                }
            )
        if app == "Inicio":
            st.title('Proyecto 01: Distribución binomial en lanzamiento de monedas')
            c1, c2 = st.columns([1,5])
            with c1:
                opt = st.radio("", ["Resumen", "Referencias"], label_visibility="collapsed")
            with c2: 
                if opt == "Resumen":
                    st.markdown("## Resumen del trabajo")
                    st.write("En la siguiente práctica se procedió a realizar una aplicación web encargada de graficar los datos obtenidos, tras 100 repeticiones, al lanzar un grupo de 10 fichas. Para ello, se empleó el uso de las librerías de *NumPy*, *Pandas*, *StreamLit* y *SciPy*.")
                    st.write("")
                    st.write("Para gráficar los datos, ...")
                    st.write("")
                    st.write("Se determino que . . .")
                        
                if opt == "Referencias":
                    st.markdown("## Referencias bibliográficas (marco teórico)")
                    wpages1 = ["a", '']
                    st.write(wpages1)
                    
                    
                    st.markdown("## Referencias bibliográficas (documentación)")
                    wpages2 = ['st.radio: https://docs.streamlit.io/library/api-reference/widgets/st.radio', '']
                    st.write(wpages2)
                
        if app == "Descripción":
            home.app()
            
        if app == "Proyecto":
            proyecto.app()
            
        if app == "Conclusiones":
            final.app()

    run()