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
        - La distribución de Poisson es la que presenta un mejor ajuste a los datos experimentales del aire, el cual se presenta en la prueba de $$\chi^{2}$$.
        - Debido a la definición matemática de la distribución de Poisson, el fit diverge para los datos del Cesio-137, y con ello la mejor distribución para dichos datos es la descrita por la distribución gaussiana.
        - La exclusión de datos que se alejan del rango usual de medición generó un mejor ajuste de los fits con respecto a los valores experimentales, sin embargo, ésta forma de analizar los datos no es coherente, dado que se están excluyendo datos experimentales.
        - El fit generado por una distribución gaussiana es más general que la de una distribución de Poisson debido a que esta logró aplicarse tanto para el caso del decaimiento del aire como para el decaimiento del Cesio-137.
        '''
    )
    
    st.title("Anexos")
    ca01, ca02 = st.columns([1,5])
    with ca01:
        opt = st.radio(
        "**Anexos**", 
        ["Ajuste (Fit)", "Tabla 01", "Tablas Aire", "Tablas Cs-137", "Tablas Cs-137 (2)", "T02.Aire", "T02.Cs-137", "T02.Cs-137 (2)"]
    )
    
    with ca02:
        if opt == "Ajuste (Fit)":
            st.markdown("## Ajuste/Fit de la gráfica (Distribución gaussiana)")
            
            st.markdown("### Fit 01 GNUPlot")
            c00, c01 = st.columns([2, 2])
            with c00:
                st.markdown("##### Descripción")
                st.write(
                    """
                    Fit realizado a partir de los datos del aire, presentado en las tablas 01 y 02 de la sección ```Tablas Aire```.
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
                        A & = 63,5733 \pm 1,967 \\
                        u & = 2,18871 \pm 0,05799 \\
                        r & = 1,59884 \pm 0,06266
                    \end{aligned}
                    $$
                    '''
                )
            with c01:
                img00 = im.open('Proyectos/P03/img/fit(ai)-01.png')
                st.image(img00)
                
            st.markdown("### Fit 02 GNUPlot")
            c02, c03 = st.columns([2, 2])
            with c02:
                st.markdown("##### Descripción")
                st.write(
                    """
                    Fit realizado a partir de los datos del decaimiento atómico del Cesio-137, datos presentados en las tablas 01 y 02 del apartado ```Tablas Cesio-137```.
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
                        A & = 5,09274 \pm 0,2716 \\
                        u & = 442,826 \pm 1,206 \\
                        r & = 19,5845 \pm 1,209
                    \end{aligned}
                    $$
                    '''
                )
            with c03:
                img01 = im.open('Proyectos/P03/img/fit(cs)-01.png')
                st.image(img01)
                
            st.markdown("### Fit 03 GNUPlot")
            c04, c05 = st.columns([2, 2])
            with c04:
                st.markdown("##### Descripción")
                st.write(
                    """
                    Fit realizado a partir de los datos del decaimiento atómico del Cesio-137, agrupados de 5 en 5. Datos presentados en las tablas 01 y 02 del apartado ```Tablas Cesio-137 (2)```.
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
                        A & = 25,382 \pm 1,211 \\
                        u & = 439,84 \pm 1,083 \\
                        r & = 19,6525 \pm 1,084
                    \end{aligned}
                    $$
                    '''
                )
            with c05:
                img02 = im.open('Proyectos/P03/img/fit(cs)-02.png')
                st.image(img02)
                
        if opt == "Tabla 01":
            st.markdown("## Datos originales")
            from P03_p02 import df
            st.table(df)
                
        if opt == "Tablas Aire":
            st.markdown("## Datos de las gráficas del decaimiento radiactivo del aire")
            from P03_p02 import dgaussai, dpoissonai, air_gaussian, air_poisson
            
            st.markdown("### Tabla 01: Distribución Gaussiana, $$P_{G}(x)$$")
            orig01 = st.toggle("Tabla original distribución gaussiana")
            # form_airgaussian = air_gaussian.applymap(lambda x: '{:.10f}'.format(x) if isinstance(x, (int, float)) else x)
            if orig01:
                st.table(dgaussai)
            else:
                st.markdown(air_gaussian.to_markdown())
            
            st.markdown("### Tabla 02: Distribución de Poisson, $$P_{P}(x)$$")
            orig02 = st.toggle("Tabla original distribución de Poisson")
            if orig02:
                st.table(dpoissonai)
            else:
                st.markdown(air_poisson.to_markdown())
                
        if opt == "Tablas Cs-137":
            st.markdown("## Datos de las gráficas del decaimiento radiactivo del Cesio-137")
            from P03_p02 import dgauss01, dpoisson01, cs_gaussian01, cs_poisson01
            st.markdown("### Tabla 01: Distribución Gaussiana, $$P_{G}(x)$$")
            orig01 = st.toggle("Tabla original distribución gaussiana")
            if orig01:
                st.table(dgauss01)
            else:
                st.markdown(cs_gaussian01.to_markdown())
                #st.write(cs_gaussian01)
            
            st.markdown("### Tabla 02: Distribución de Poisson, $$P_{P}(x)$$")
            orig02 = st.toggle("Tabla original distribución de Poisson")
            if orig02:
                st.table(dpoisson01)
            else:
                st.markdown(cs_poisson01.to_markdown())
            
        if opt == "Tablas Cs-137 (2)":
            st.markdown("## Datos de las gráficas del decaimiento radiactivo del Cesio-137 (Datos agrupados)")
            from P03_p02 import dgauss02, dpoisson02, cs_gaussian02, cs_poisson02
            st.markdown("### Tabla 01: Distribución Gaussiana, $$P_{G}(x)$$")
            orig01 = st.toggle("Tabla original distribución gaussiana")
            if orig01:
                st.table(dgauss02)
            else:
                st.markdown(cs_gaussian02.to_markdown())
            
            st.markdown("### Tabla 02: Distribución de Poisson, $$P_{P}(x)$$")
            orig02 = st.toggle("Tabla original distribución de Poisson")
            if orig02:
                st.table(dpoisson02)
            else:
                st.markdown(cs_poisson02.to_markdown())
                
        if opt == "T02.Aire":
            st.markdown("## Datos de las gráficas del decaimiento radiactivo del aire (modificado)")
            from P03_p02 import dgaussai02, dpoissonai02, air_tgaussian, air_tpoisson
            
            st.markdown("### Tabla 01: Distribución Gaussiana, $$P_{G}(x)$$")
            orig01 = st.toggle("Tabla original distribución gaussiana")
            # form_airgaussian = air_gaussian.applymap(lambda x: '{:.10f}'.format(x) if isinstance(x, (int, float)) else x)
            if orig01:
                st.table(dgaussai02)
            else:
                st.markdown(air_tgaussian.to_markdown())
            
            st.markdown("### Tabla 02: Distribución de Poisson, $$P_{P}(x)$$")
            orig02 = st.toggle("Tabla original distribución de Poisson")
            if orig02:
                st.table(dpoissonai02)
            else:
                st.markdown(air_tpoisson.to_markdown())
                
        if opt == "T02.Cs-137":
            st.markdown("## Datos de las gráficas del decaimiento radiactivo del Cesio-137 (modificado)")
            from P03_p02 import mdgauss01, mdpoisson01, mcs_gaussian01, mcs_poisson01
            st.markdown("### Tabla 01: Distribución Gaussiana, $$P_{G}(x)$$")
            orig01 = st.toggle("Tabla original distribución gaussiana")
            if orig01:
                st.table(mdgauss01)
            else:
                st.markdown(mcs_gaussian01.to_markdown())
                #st.write(cs_gaussian01)
            
            st.markdown("### Tabla 02: Distribución de Poisson, $$P_{P}(x)$$")
            orig02 = st.toggle("Tabla original distribución de Poisson")
            if orig02:
                st.table(mdpoisson01)
            else:
                st.markdown(mcs_poisson01.to_markdown())
            
        if opt == "T02.Cs-137 (2)":
            st.markdown("## Datos de las gráficas del decaimiento radiactivo del Cesio-137, datos agrupados (modificado)")
            from P03_p02 import mdgauss02, mdpoisson02, mcs_gaussian02, mcs_poisson02
            st.markdown("### Tabla 01: Distribución Gaussiana, $$P_{G}(x)$$")
            orig01 = st.toggle("Tabla original distribución gaussiana")
            if orig01:
                st.table(mdgauss02)
            else:
                st.markdown(mcs_gaussian02.to_markdown())
            
            st.markdown("### Tabla 02: Distribución de Poisson, $$P_{P}(x)$$")
            orig02 = st.toggle("Tabla original distribución de Poisson")
            if orig02:
                st.table(mdpoisson02)
            else:
                st.markdown(mcs_poisson02.to_markdown())
       
             