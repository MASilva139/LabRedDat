import numpy as np
import pandas as pd
import plotly.express as px
from scipy import stats
from scipy.optimize import curve_fit
import streamlit as st
import matplotlib.pyplot as plt
import math
from scipy.special import comb

def app():
    with open('Proyectos/P02/form01.css') as f:
        css = f.read()

    # Añade tu CSS
    st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)
    
    st.title('Distribución Binomial en lanzamiento de monedas')