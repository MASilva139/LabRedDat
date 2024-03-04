# Importando las librerias de python a utilizar
import streamlit as st
# import plotly.express as px
import pandas as pd
from matplotlib import pyplot as plt
import math
import numpy as np
from PIL import Image

pd.set_option('display.precision', 20)

def app():
    st.title('Distribución Binomial (.slider)')

    # Declarando las columnas dentro del streamlit
    c1, c2 = st.columns([1,3])

    with c1:
        # Lista para ver los datos
        option = st.selectbox(
            'Opciones (visualizar)', ('Gráfica (normal)', 'Gráfica (logarítmica)', 'Tabla de datos')
        )
        # Declarando las variables n, p, q para el binomial (con sliders)
        n = st.slider("n: (valor entre 0 y 100)", min_value=0, max_value=100, value=1, step=1) 
        p = st.slider("p: (valor entre 0 y 1)", 0.0000, 1.0000, value=0.5000)
        q = (1-p)
        img = Image.open('Parcial\P01\img\img01.png')
        st.image(img)
        # Generando función del binomial
        def bin(x,n,p,q):
            comb = math.comb(n,x)
            px = p**x
            qnx = q**(n-x)
            return comb*px*qnx

        # Lista y tabla de los valores de la función binomial
        l = np.arange(n+1)

        lpx = []
        for xj in l:
            lpx.append(math.pow(p,int(xj)))
        
        lqnx = []
        for xi in l:
            lqnx.append(math.pow(q,int(n-xi)))
        
        pq = zip(lpx,lqnx)
        pqr = [a*b for a, b in zip(lpx,lqnx)]

        dt = pd.DataFrame({'x':l, 'px':lpx, 'qnx':lqnx, 'px*qnx':pqr})
        dt['Pb'] = dt.apply(lambda row: bin(int(row['x']),n,p,q), axis=1)
        dtr = dt.round(15).astype(str)

    with c2:
        if option == "Gráfica (normal)":
            # Generando gráfica en steramlit
            bin_g, axis = plt.subplots()
            axis.bar(dt['x'], dt['Pb'], color='skyblue') #Estableciendo la gráfica de barras
            axis.plot(dt['x'], dt['Pb'], color='Red') #Generando la gráfica de línea
            plt.xlabel('n')
            plt.ylabel('Pb(x,n)')
            plt.grid(True)
            plt.title(f'Distribución en {n} tiros')
            st.pyplot(bin_g)
            
        if option == "Tabla de datos":
            # Agregar tabla de datos del binomial
            st.write("### Tabla de datos")
            st.table(dtr)

        if option == "Gráfica (logarítmica)":
            # Generando gráfica en escala logarítmica
            bin_gl, ax = plt.subplots()
            ax.bar(dt['x'], dt['Pb'], color='skyblue') #Estableciendo la gráfica de barras
            ax.plot(dt['x'], dt['Pb'], color='Red') #Generando la gráfica de línea
            plt.xlabel('n')
            plt.ylabel('Pb(x,n)')
            plt.grid(True)
            plt.yscale('log')
            plt.title(f'Distribución en {n} tiros (escala logarítmica)')
            st.pyplot(bin_gl)