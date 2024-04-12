import numpy as np
import pandas as pd
import plotly.express as px
from scipy import stats
from scipy.optimize import curve_fit
from streamlit_option_menu import option_menu
from streamlit_extras.stylable_container import stylable_container as stycont
import streamlit as st
import matplotlib.pyplot as plt
import math
from scipy.special import comb

def app():
    with open('Proyectos/P02/form01.css') as f:
        css = f.read()

    # Añade tu CSS
    st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)
    
    st.title('Proyecto 02: Predicción de COVID19')
    
    # st.title('Proyecto 01: Distribución binomial en lanzamiento de monedas')
    c1, c2 = st.columns([1,5])
    with c1:
        opt = st.radio("", ["Proyecto", "Referencias"], label_visibility="collapsed")
        # with stycont(
        #         key="menu-01",
        #         css_styles="""
        #         """,
        #     ):
        #     opt = option_menu(
        #         #menu_title='Pages',
        #         None,
        #         options=['Proyecto', 'Referencias'], # Nombre de cada pestaña
        #         icons=['house-fill', 'bezier', 'body-text'], #Iconos de las pestañas
        #         menu_icon='alt',
        #         default_index=0, # En este se define la primera página en mostrarse,
        #         orientation="vertical",
        #         styles={
        #             "container": {"padding": "1!important", "background-color":'transparent'},
        #             "icon":{"color":"white", "font-size":"16px"},
        #             "nav-link":{"color":"white", "font-size": "13px", "text-align":"center", "margin":"0px","--hover-color":"sepia"},
        #             "nav-link-selected":{"background-color":"darkolivegreen"}
        #         }
        #     )
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
            st.write(
                """
                ### Distribución binomial
            
                Es una distribución de probabilidad discreta que cuenta la cantidad de éxitos en $$n$$ casos con una
                probabilidad fija $$p$$. Se caracteriza porque únicamente existe dos casos: éxito y fracaso. Además la
                probabilidad $$p$$ es fija, lo que quiere decir que la probabilidad de éxito o fracaso en cada uno de
                los casos no depende de lo que haya sucedido en el anterior.
            
                #### Fórmula
                """
                r'''
                $$
                P_b(x,n)=\begin{pmatrix}
                    n\\
                    x
                \end{pmatrix}
                p^x(1-p)^{n-x}=\frac{n!}{x!(n-x)!}\cdot p^x(1-p)^{n-x}
                $$
                '''
                """
                Donde $$P_b(x,n)$$ es la probabilidad de $$x$$ aciertos en $$n$$ ensayos, cada uno con probabilidad
                $$p$$.
            
                #### Media y desviación estándar
            
                La media de una distribución binomial es de la forma:
                """
                r'''
                $$
                \mu=np
                $$
                '''
                """
                La desviación estándar viene dada por:
                """
                r'''
                $$
                \sigma=\sqrt{npq}=\sqrt{np(1-p)}
                $$
                '''
                """
                ### Fit distribución binomial
            
                La librería `scipy.optimize` permite crear un fit personalizado con la opción `curve_fit()`, la cual
                utiliza mínimos cuadrados no lineales para ajustar una función, $$f$$, a los datos proporcionados.
            
                La síntaxis del comando es la siguiente:
            
                ```python
                scipy.optimize.curve_fit(f, xdata, ydata, p0=None, sigma=None, absolute_sigma=False, check_finite=None, bounds=(-inf, inf), method=None, jac=None, *, full_output=False, nan_policy=None, **kwargs)
                ```
                Puede verse la documentación completa [aquí](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html).
                """
            )
            
            # if st.button('Ir al inicio'):
            #     st.write('<meta http-equiv="refresh" content="0">', unsafe_allow_html=True)
                
        if opt == "Referencias":
            st.markdown("## Referencias bibliográficas (marco teórico)")
            wpages1 = ["Scipy Inc. (n.d.). Scipy.Optimize. Recuperado de https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html", '']
            st.write(wpages1)
            
            
            st.markdown("## Referencias bibliográficas (documentación)")
            wpages2 = ['KaTeX. (2024). Supported Functions. Recuperado de: https://katex.org/docs/supported.html','Streamlit Inc. (n.d.). st.columns. Recuperado de: https://docs.streamlit.io/library/api-reference/layout/st.columns','Streamlit Inc. (n.d.). st.markdown. Recuperado de: https://docs.streamlit.io/library/api-reference/text/st.markdown','Streamlit Inc. (n.d.). st.radio. Recuperado de: https://docs.streamlit.io/library/api-reference/widgets/st.radio','Streamlit Inc. (n.d.). st.set_page_config. Recuperado de: https://docs.streamlit.io/library/api-reference/utilities/st.set_page_config', 'Streamlit Inc. (n.d.). st.radio. Recuperado de: https://docs.streamlit.io/library/api-reference/widgets/st.slider','Streamlit Inc. (n.d.). st.write. Recuperado de: https://docs.streamlit.io/library/api-reference/write-magic/st.write']
            st.write(wpages2)