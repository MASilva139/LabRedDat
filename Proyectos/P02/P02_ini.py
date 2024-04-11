import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image as im
import os

import proyecto
#print(os.path.abspath('form01.css'))
#with open('form01.css') as f:
#    css = f.read()
#st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)
try:
    st.set_page_config(
        page_title="Proyecto 01",
        page_icon=':shinto_shrine:',
        layout="wide"
    )
    #https://github.com/MathCatsAnd/Streamlit-Mechanics-Examples/blob/main/pages/column_selector_v2.py
    with open('Proyectos/P02/form01.css') as f:
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
            st.session_state.app = option_menu(
                menu_title='Pages',
                options=['Inicio', 'Proyecto', 'Conclusiones'], # Nombre de cada pestaña
                icons=['house-fill', 'bezier', 'body-text'], #Iconos de las pestañas
                menu_icon='alt',
                default_index=0, # En este se define la primera página en mostrarse,
                orientation="horizontal",
                styles={
                    "container": {"padding": "1!important", "background-color":'black'},
                    "icon":{"color":"white", "font-size":"16px"},
                    "nav-link":{"color":"white", "font-size": "13px", "text-align":"center", "margin":"0px","--hover-color":"sepia"},
                    "nav-link-selected":{"background-color":"darkolivegreen"}
                }
            )
            if st.session_state.app == "Inicio":
                st.title('Proyecto 01: Distribución binomial en lanzamiento de monedas')
                c1, c2 = st.columns([1,5])
                with c1:
                    opt = st.radio("", ["Proyecto", "Referencias"], label_visibility="collapsed")
                with c2: 
                    if opt == "Proyecto":
                        st.markdown("## Resumen / Caso de estudio")
                        
                        st.write("En la siguiente práctica se procedió a realizar una aplicación web encargada de graficar los datos obtenidos, tras 100 repeticiones, al lanzar un grupo de $$10$$ fichas. Para ello, se emplearon las librerías de ``NumPy``, ``Pandas``, ``Plotly.Express``, ``MatPlotLib``, ``StreamLit`` y ``SciPy``.")
                        st.write("")
                        st.write("Se realizarón $$100$$ repeticiones para el lanzamiento de $$10$$ fichas, en las cuales se contaron el número de caras obtenidas por cada repetición, registrandolas como $$n$$. A partir de los datos obtenidos, convirtiendo las *n* caras por cada repetición, se realizarón las tablas con la librería de ``Pandas.DataFrame()`` y a partir de estas se hicieron las graficas de ``Plotly.Expres`` y ``PyPlot``. Para el fit se usa el arreglo de ``Numpy``, además de utilizar la función ``curve_fit`` de la librería de ``scipy.optimize``.")
                        st.write("")
                        st.write("Se lograron realizar buenos ajustes de la curva, empleando para ello la libreria de ``Plotly.Express``, a partir de la función binomial, obteniendo una gráfica identica tanto a partir de la importación de la función binomial a partir del modulo ``stats`` de la librería de ``scipy``, como de la definición de la función binomial a partir de los parámetros $$n$$, $$x$$ y $$p$$, empleando el comando ``def``.")
                    
                        st.markdown("## Marco Teórico")
                        # A partir de aquí se escribe para el marco teórico
                        if st.button('Ir al inicio'):
                            st.write('<meta http-equiv="refresh" content="0">', unsafe_allow_html=True)
                            
                    if opt == "Referencias":
                        st.markdown("## Referencias bibliográficas (marco teórico)")
                        wpages1 = ["Scipy Inc. (n.d.). Scipy.Optimize. Recuperado de https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html", '']
                        st.write(wpages1)
                        
                        
                        st.markdown("## Referencias bibliográficas (documentación)")
                        wpages2 = ['KaTeX. (2024). Supported Functions. Recuperado de: https://katex.org/docs/supported.html','Streamlit Inc. (n.d.). st.columns. Recuperado de: https://docs.streamlit.io/library/api-reference/layout/st.columns','Streamlit Inc. (n.d.). st.markdown. Recuperado de: https://docs.streamlit.io/library/api-reference/text/st.markdown','Streamlit Inc. (n.d.). st.radio. Recuperado de: https://docs.streamlit.io/library/api-reference/widgets/st.radio','Streamlit Inc. (n.d.). st.set_page_config. Recuperado de: https://docs.streamlit.io/library/api-reference/utilities/st.set_page_config', 'Streamlit Inc. (n.d.). st.radio. Recuperado de: https://docs.streamlit.io/library/api-reference/widgets/st.slider','Streamlit Inc. (n.d.). st.write. Recuperado de: https://docs.streamlit.io/library/api-reference/write-magic/st.write']
                        st.write(wpages2)
                
            if st.session_state.app == "Proyecto":
                proyecto.app()
                
            if st.session_state.app == "Conclusiones":
                final.app()

        run()
    pass
except FileNotFoundError:
    st.error("No se encontró el archivo de configuración")