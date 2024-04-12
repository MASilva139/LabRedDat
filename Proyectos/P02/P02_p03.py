import pandas as pd
import plotly.express as px
import streamlit as st
import numpy as np
import math

def app():
    with open('Proyectos/P02/form01.css') as f:
        css = f.read()

    # Añade tu CSS
    st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)
    
    st.title('Distribución Binomial en lanzamiento de monedas')