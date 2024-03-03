# Importando las librerias de python a utilizar
import streamlit as st
import plotly.express as px
import pandas as pd
from matplotlib import pyplot as plt
import math
import numpy as np

import pickle
from pathlib import Path
import streamlit_authenticator as stauth


#st.set_pages_config(page_title="Examen Parcial 01", layout="wide")
st.title('Distribución Binomial (Parcial 01)')

# Declarando las variables n, p, q para el binomial
n = st.slider("n", min_value=0, max_value=100, value=1, step=1)
p = st.slider("p", 0.0000, 1.0000, value=0.5000)
q = (1-p)
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

dt = pd.DataFrame({'x':l, 'px':lpx, 'qnx':lqnx, 'px*qnx':pq})
dt['Pb'] = dt.apply(lambda row: bin(int(row['x']),n,p,q), axis=1)

# Generando gráfica en steramlit
bin_g, axis = plt.subplots()
axis.bar(dt['x'], dt['Pb'], color='skyblue') #Estableciendo la gráfica de barras
axis.plot(dt['x'], dt['Pb'], color='Red') #Generando la gráfica de línea
plt.xlabel('n')
plt.ylabel('Pb(x,n)')
plt.grid(True)
plt.title(f'Distribución en {n} tiros')
st.pyplot(bin_g)

# Agregar tabla de datos del binomial
st.write("### Tabla de datos", dt.sort_index())

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