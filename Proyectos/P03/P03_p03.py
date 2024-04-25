import pandas as pd
import plotly.express as px
import streamlit as st
import numpy as np
import math
from PIL import Image as im

#import P03_p02

def app():
    with open('Proyectos/P03/form01.css') as f:
        css = f.read()

    # Añade tu CSS
    st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)
    
    st.title("Conclusiones")
    st.write(
        '''
        - Las gráficas presentadas por ``Plotly.Express`` permiten realizar gráficas interactivas en donde puede observarse la comparación de la proyección dada por el ajuste con los datos reales que ya conocemos.
        - En esta ocasión no era óptimo utilizar una distribución binomial, aunque los datos tomaran esta forma, ya que para ello necesitabamos información que no poseíamos, como lo es la probabilidad.
        - Aunque la elección de la distribución y fórmula a utilizar es un paso clave, la exactitud y fiabilidad del ajuste fue decidida gracias al análisis previo de los datos para definir cuales nos darían resultados más satisfactorios y coherentes con lo estudiado.
        '''
    )
    
    st.title("Anexos")
    ca01, ca02 = st.columns([1,5])
    with ca01:
        opt = st.radio(
        "**Anexos**", 
        ["Ajuste (Fit)", "Tabla 01", "Tablas Aire", "Tablas Cesio-137", "Tablas Cesio-137 (2)"]
    )
    
    with ca02:
        if opt == "Ajuste (Fit)":
            st.markdown("## Ajuste/Fit de la gráfica (Distribución gaussiana)")
            
            st.markdown("### Fit 01 GNUPlot")
            c44, c45 = st.columns([2, 2])
            with c44:
                st.markdown("##### Descripción")
                st.write(
                    """
                    Fit realizado a partir del día 59, después del primer caso positivo registrado.
                    \n
                    ##### Función empleada
                    """
                    r'''
                    $$
                    P_{G}(x)=A\cdot \exp{\left[-\frac{1}{2}\left(\frac{x-u}{r}\right)^{2}\right]}
                    $$
                    '''
                    """
                    ##### Valores de las constantes
                    """
                    r'''
                    $$
                    \begin{aligned}
                        A & = 1195,28 \pm 2,094+04 \\
                        u & = 188,642 \pm 673,3 \\
                        r & = 53,1543 \pm 119,9
                    \end{aligned}
                    $$
                    '''
                )
            with c45:
                img23 = im.open('Proyectos/P02/img/fit23.png')
                st.image(img23)
                
            st.markdown("### Fit 02 GNUPlot")
            c42, c43 = st.columns([2, 2])
            with c42:
                st.markdown("##### Descripción")
                st.write(
                    """
                    Fit realizado a partir del día 60, después del primer caso positivo registrado.
                    \n
                    ##### Función empleada
                    """
                    r'''
                    $$
                    P_{G}(x)=A\cdot \exp{\left[-\frac{1}{2}\left(\frac{x-u}{r}\right)^{2}\right]}
                    $$
                    '''
                    """
                    ##### Valores de las constantes
                    """
                    r'''
                    $$
                    \begin{aligned}
                        A & = 1497,57 \pm 2,715+04 \\
                        u & = 196,503 \pm 694,1 \\
                        r & = 54,302 \pm 120,5
                    \end{aligned}
                    $$
                    '''
                )
            with c43:
                img22 = im.open('Proyectos/P02/img/fit22.png')
                st.image(img22)
                
        if opt == "Tabla 01":
            st.markdown("## Datos originales")
            from P03_p02 import df
            st.table(df)
                
        if opt == "Tablas Aire":
            st.markdown("## Datos de las gráficas del decaimiento radiactivo del aire")
            from P03_p02 import dgaussai, dpoissonai, air_gaussian, air_poisson
            
            st.markdown("### Distribución Gaussiana, $$P_{G}(x)$$")
            orig01 = st.toggle("Tabla original distribución gaussiana")
            # form_airgaussian = air_gaussian.applymap(lambda x: '{:.10f}'.format(x) if isinstance(x, (int, float)) else x)
            if orig01:
                st.table(dgaussai)
            else:
                st.markdown(air_gaussian.to_markdown())
            
            st.markdown("### Distribución de Poisson, $$P_{P}(x)$$")
            orig02 = st.toggle("Tabla original distribución de Poisson")
            if orig02:
                st.table(dpoissonai)
            else:
                st.markdown(air_poisson.to_markdown())
                
        if opt == "Tablas Cesio-137":
            st.markdown("## Datos de las gráficas del decaimiento radiactivo del Cesio-137")
            from P03_p02 import dgauss01, dpoisson01, cs_gaussian01, cs_poisson01
            st.markdown("### Distribución Gaussiana, $$P_{G}(x)$$")
            orig01 = st.toggle("Tabla original distribución gaussiana")
            if orig01:
                st.table(dgauss01)
            else:
                st.markdown(cs_gaussian01.to_markdown())
            
            st.markdown("### Distribución de Poisson, $$P_{P}(x)$$")
            orig02 = st.toggle("Tabla original distribución de Poisson")
            if orig02:
                st.table(dpoisson01)
            else:
                st.markdown(cs_poisson01.to_markdown())
            
        if opt == "Tablas Cesio-137 (2)":
            st.markdown("## Datos de las gráficas del decaimiento radiactivo del Cesio-137 (Datos agrupados)")
            from P03_p02 import dgauss02, dpoisson02, cs_gaussian02, cs_poisson02
            st.markdown("### Distribución Gaussiana, $$P_{G}(x)$$")
            orig01 = st.toggle("Tabla original distribución gaussiana")
            if orig01:
                st.table(dgauss02)
            else:
                st.markdown(cs_gaussian02.to_markdown())
            
            st.markdown("### Distribución de Poisson, $$P_{P}(x)$$")
            orig02 = st.toggle("Tabla original distribución de Poisson")
            if orig02:
                st.table(dpoisson02)
            else:
                st.markdown(cs_poisson02.to_markdown())