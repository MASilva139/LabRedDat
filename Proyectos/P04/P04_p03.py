import pandas as pd
import plotly.express as px
import streamlit as st
import numpy as np
import math
from PIL import Image as im

#import P03_p02

def app():
    with open('Proyectos/P04/form01.css') as f:
        css = f.read()

    # Añade tu CSS
    st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)
    
    st.title("Conclusiones")
    st.write(
        '''
        - La distribución de Poisson es la que presenta un mejor ajuste a los datos experimentales del aire, el cual se presenta en la prueba de $$\chi^{2}$$.
        - Debido a la definición matemática de la distribución de Poisson, el fit diverge para los datos del Cesio-137, y con ello la mejor distribución para dichos datos es la descrita por la distribución gaussiana.
        - La exclusión de datos que se alejan del rango usual de medición generó un mejor ajuste de los fits con respecto a los valores experimentales, sin embargo, ésta forma de analizar los datos no es coherente, dado que se están excluyendo datos experimentales.
        - El fit generado por una distribución gaussiana es más general que la de una distribución de Poisson debido a que esta logró aplicarse tanto para el caso del decaimiento del aire como para el decaimiento del Cesio-137.
        '''
    )
    