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
    
    st.markdown("## **Procedimiento Experimental**")
    # Sección del procedimiento del proyecto
    st.write(
        """
        En la presente práctica se llevó a cabo el lanzamiento de diez monedas para cada repetición, siendo un total de cien repeticiones, de las cuales en cada una de estas se contaban el número de fichas que caían cara. En caso de que alguna de las fichas fuese interrumpida por alguna cosa, se procedia a repetir el tiro de dicha moneda para completar el conteo de caras. 
        """
    )
    
    st.markdown("## **Resultados**")
    # Sección de los resultados
    rlist = ['a', 'b', 'c']

    s = ''

    for i in rlist:
        s += "- " + i + "\n"

    st.markdown(s)
    st.write(
        """
        En la presente sección se presentarán los resultados obtenidos en la presente práctica, de los cuales están divididos en
        """
        '''
        1. **Gráfica 01**: Gráfica de los valores propios, utilizando Plotly.
        2. **Gráfica 02**: Gráfica de los datos de todos los grupos del laboratorio.
        '''
    )
    
    c1, c2 = st.columns([1,4])
    with c1:
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
            
        if resultados == "Gráfica 01":
            st.markdown("## Gráfica Propia (Plotly)")
            c3, c4 = st.columns([6,1.5])
            with c3:
                # Fit
                p0=[10,1/2]
                res, cov = curve_fit(fit_function, value_range, group_2, p0=p0, bounds=[(0,0), (np.inf,1)])

                # Gráfica en plotly
                binomial = px.line(x=value_range, y=fit_function(value_range, *res)*(number), line_shape='spline')
                binomial.update_traces(line_color='#721422', line_width=2.5)
                binomial.add_bar(x=group['GM'], y=group['count'], marker_color='#6C6960', name='binomial')
                # Mostrar gráfica de plotly
                st.plotly_chart(binomial)
                st.write(f'El valor de n es: {res[0]}')
                st.write(f'El valor de p es: {res[1]}')
                
            with c4:
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
            
        if resultados == "Gráfica 03":
            st.markdown("## Gráfica de todos los datos (Plotly)")
            # Gráfica y fit de los datos de toda la clase
            data_class = pd.Series(df.iloc[:number].squeeze().values.ravel()).value_counts().sort_index()
            data_class = data_class.reindex(value_range, fill_value=0)
            group_class = data_class.to_numpy()
            todos = data_class.reset_index()
            # group_class = pd.Series.to_numpy(data_class['count'], dtype=int)
            # Fit
            p0=[10,1/2]
            res_2, cov_2 = curve_fit(fit_function, value_range, data_class, p0=p0, bounds=[(0,0), (np.inf,1)])
            binomial_todos = px.line(x=value_range, y=fit_function(value_range, *res_2)*(number*6), line_shape='spline')
            binomial_todos.update_traces(line_color='#721422', line_width=2.5)
            binomial_todos.add_bar(x=todos['index'], y=todos['count'], marker_color='#6C6960', name='binomial')
            st.plotly_chart(binomial_todos)
            st.write(f'El valor de n es: {res_2[0]}')
            st.write(f'El valor de p es: {res_2[1]}')

    st.markdown("## **Discusión de Resultados**")
    # Sección de los resultados