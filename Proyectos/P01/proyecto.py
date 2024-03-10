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
    st.title('Distribución Binomial en lanzamiento de monedas')
    
    c1, c2 = st.columns([1,4])
    with c1:
        opt = st.radio(
            "***Seleccione lo que desee ver***", ["Procedimiento", "Resultados", "Discusión"]
        )
        c3, c4 = st.columns([1,10])
        with c4:
            if opt == "Resultados":
                resultados = st.radio(
                    "**Resultados**", 
                    ["Gráfica 01", "Gráfica 02", "Gráfica 03"]
                )# Slider de los valores de m
                number = st.slider('Seleccione número de datos', min_value=0, max_value=100, step=1)
                
                # Función para el fit dada por scipy
                def fit_func(x, n, p):
                    return stats.binom(x, n, p)

                # Función propia para el fit
                def fit_function(x,n,p):
                # Todo lo que este aqui adentro es parte de lo que se ejecuta en la funcion
                    n = int(n)
                    x = np.array(x, dtype=int)
                    combi = comb(n,x)
                    px = p**x
                    qnx = (1-p)**(n-x)
                    return combi*px*qnx
                
                # Crear pandas con los datos de los tiros
                data = pd.read_csv('Proyectos/P01/Binomial-fichas.csv')
                df = pd.DataFrame(data)
                # Arange con los valores del 0 al 10
                value_range = np.arange(11)
                # Conteo de los valores de caras
                group = df['GM'].iloc[:number].value_counts().reindex(value_range, fill_value=0).reset_index()
                # Convertir serie a numpy
                group_2 = pd.Series.to_numpy(df['GM'].iloc[:number].value_counts().reindex(value_range, fill_value=0))
        
    with c2:
        if opt == "Procedimiento":
            st.markdown("## Procedimiento Experimental")
            # A partir de aca se escribe lo del procedimiento experimental
            
            
        if opt == "Discusión":
            st.markdown("## Discusión de Resultados")
            # A partir de acá se escribe la discusión de resultados
            
            
        if opt=="Resultados" and resultados == "Gráfica 01":
            st.markdown("## Gráfica Propia (Plotly)")
            c5, c6 = st.columns([6,1.5])
            with c5:
                # Fit
                p0=[10,1/2]
                res, cov = curve_fit(fit_function, value_range, group_2, p0=p0)

                # Gráfica en plotly
                binomial = px.line(x=value_range, y=fit_function(value_range, *res)*(number), line_shape='spline')
                binomial.update_traces(line_color='#721422', line_width=2.5)
                binomial.add_bar(x=group['GM'], y=group['count'], marker_color='#6C6960', name='binomial')
                # Mostrar gráfica de plotly
                st.plotly_chart(binomial)
                
            with c6:
                # Función para cambiar el color de las celdas
                def Ccol(val):
                    color = '#6C6874'
                    return f'background-color: {color}'
                def color_celda(val):
                    if val >= 0 and val < 5:
                        color = '#705335' 
                    elif val >= 5 and val < 10:
                        color='#587246'
                    elif val >= 10 and val < 15:
                        color='#606E8C'
                    elif val >= 15 and val < 20:
                        color='#2C5545'
                    elif val >= 20 :
                        color='#5E2129'
                    return f'background-color: {color}'

                # Aplicar la función a las celdas del DataFrame
                fgroup = group.style.applymap(Ccol, subset=['GM']).applymap(color_celda, subset=['count'])
                st.table(fgroup)
            
        if opt=="Resultados" and resultados == "Gráfica 02":
            st.markdown("## Gráfica Propia (PyPlot)")
            c7, c8 = st.columns([6,1.5])
            with c7:
                # Fit
                p0=[10,1/2]
                res, cov = curve_fit(fit_function, value_range, group_2, p0=p0)
                # Gráfica en pyplot
                fig, ax = plt.subplots(figsize=(10,6))
                ax.bar(value_range, group_2)
                ax.plot(value_range, fit_function(value_range, *res)*(number), color='C3')
                
                # Otro tipo de fit y de gráfica
                temp = df['GM'].iloc[:number]
                # Mostrar gráfica de pyplot
                st.pyplot(fig)
            with c8:
                # Función para cambiar el color de las celdas
                def Ccol(val):
                    color = '#000'
                    return f'background-color: {color}'
                def color_celda(val):
                    if val >= 0 and val < 5:
                        color = '#705335' 
                    elif val >= 5 and val < 10:
                        color='#587246'
                    elif val >= 10 and val < 15:
                        color='#606E8C'
                    elif val >= 15 and val < 20:
                        color='#2C5545'
                    elif val >= 20 :
                        color='#5E2129'
                    return f'background-color: {color}'

                # Aplicar la función a las celdas del DataFrame
                fgroup = group.style.applymap(Ccol, subset=['GM']).applymap(color_celda, subset=['count'])
                st.table(fgroup)
            
        if opt=="Resultados" and resultados == "Gráfica 03":
            st.markdown("## Gráfica de todos los datos (Plotly)")
            # Gráfica y fit de los datos de toda la clase
            data_class = pd.Series(df.squeeze().values.ravel()).value_counts().sort_index()
            data_class = data_class.reindex(value_range, fill_value=0)
            group_class = data_class.to_numpy()
            todos = data_class.reset_index()
            # group_class = pd.Series.to_numpy(data_class['count'], dtype=int)
            # Fit
            p0=[10,1/2]
            res_2, cov_2 = curve_fit(fit_function, value_range, data_class, p0=p0)
            binomial_todos = px.line(x=value_range, y=fit_function(value_range, *res_2)*(450), line_shape='spline')
            binomial_todos.update_traces(line_color='#721422', line_width=2.5)
            binomial_todos.add_bar(x=todos['index'], y=todos['count'], marker_color='#6C6960', name='binomial')
            st.plotly_chart(binomial_todos)