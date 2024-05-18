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
        r'''
        - La diferencia entre el set de datos de entrenamiento y el set de datos ingresado es pequeña debido a que se logró entrenar el vector de peso de buna manera.
        - La diferencia entre el vector de peso entrenado $$\vec{W}_{trained}$$ y el vector de peso esperado $$\vec{W}_{target}$$ disminuiría en caso de realizarse más iteraciones.
        '''
    )
    