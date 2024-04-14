import pandas as pd
import plotly.express as px
import streamlit as st
import numpy as np
import math
from PIL import Image as im

def app():
    with open('Proyectos/P02/form01.css') as f:
        css = f.read()

    # Añade tu CSS
    st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)
    
    st.title("Conclusiones")
    st.write(
        '''
        - Las gráficas presentadas por ``Plotly.Express`` permiten una mejor representación de los datos que las realizadas por el entorno de ``PyPlot``.
        - Los valores experimentales presentan una muy buena aproximación, respecto a los valores teóricos, con la función binomial.
        - Mientras mayor sea el número de datos, la gráfica toma una forma más parecida a una distribución binomial teórica y los datos $$n$$ y $$p$$ obtenidos por el ajuste son más cercanos a los teóricos.
        '''
    )
    
    st.title("Anexos")
    anex = st.toggle("Mostrar anexos")
    if anex:
        st.markdown("### Fit 01 GNUPlot")
        c0, c1 = st.columns([2, 2])
        with c0:
            st.markdown("##### Descripción")
            st.write(
                """
                Fit realizado a partir del día 66, después del primer caso positivo registrado.
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
                    A & = 3298,26 \pm 3,582e+04 \\
                    u & = 163 \pm 292,4 \\
                    r & = 38,5015 \pm 50,25
                \end{aligned}
                $$
                '''
            )
        with c1:
            img01 = im.open('Proyectos/P02/img/fit09.png')
            st.image(img01)
            
        st.markdown("### Fit 02 GNUPlot")
        c0, c1 = st.columns([2, 2])
        with c0:
            st.markdown("##### Descripción")
            st.write(
                """
                Fit realizado a partir del día 69, después del primer caso positivo registrado.
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
                    A & = 930,848 \pm 3038 \\
                    u & = 109,684 \pm 70,81 \\
                    r & = 23,3855 \pm 16,1
                \end{aligned}
                $$
                '''
            )
        with c1:
            img01 = im.open('Proyectos/P02/img/fit07.png')
            st.image(img01)
            
        st.markdown("### Fit 03 GNUPlot")
        c0, c1 = st.columns([2, 2])
        with c0:
            st.markdown("##### Descripción")
            st.write(
                """
                Fit realizado a partir del día 71, después del primer caso positivo registrado.
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
                    A & = 73351,4 \pm 1,105e+06 \\
                    u & = 157,543 \pm 225,8 \\
                    r & = 26,6576 \pm 30,94
                \end{aligned}
                $$
                '''
            )
        with c1:
            img01 = im.open('Proyectos/P02/img/fit08.png')
            st.image(img01)
            
        st.markdown("### Fit 04 GNUPlot")
        c0, c1 = st.columns([2, 2])
        with c0:
            st.markdown("##### Descripción")
            st.write(
                """
                Fit realizado a partir del día 74, después del primer caso positivo registrado.
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
                    A & = 856,207 \pm 1023 \\
                    u & = 97,0032 \pm 24,16 \\
                    r & = 17,8682 \pm 6,666
                \end{aligned}
                $$
                '''
            )
        with c1:
            img01 = im.open('Proyectos/P02/img/fit10.png')
            st.image(img01)
            
        st.markdown("### Fit 05 GNUPlot")
        c0, c1 = st.columns([2, 2])
        with c0:
            st.markdown("##### Descripción")
            st.write(
                """
                Fit realizado a partir del día 75, después del primer caso positivo registrado.
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
                    A & = 343,99 \pm 55,61 \\
                    u & = 77,6314 \pm 4,169 \\
                    r & = 11,3053 \pm 2,061
                \end{aligned}
                $$
                '''
            )
        with c1:
            img01 = im.open('Proyectos/P02/img/fit11.png')
            st.image(img01)
            
        st.markdown("### Fit 06 GNUPlot")
        c0, c1 = st.columns([2, 2])
        with c0:
            st.markdown("##### Descripción")
            st.write(
                """
                Fit realizado a partir del día 79, después del primer caso positivo registrado.
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
                    A & = 298,665 \pm 11,53 \\
                    u & = 72,888 \pm 0,639 \\
                    r & = 8,41933 \pm 0,6413
                \end{aligned}
                $$
                '''
            )
        with c1:
            img01 = im.open('Proyectos/P02/img/fit04.png')
            st.image(img01)
            
        st.markdown("### Fit 07 GNUPlot")
        c0, c1 = st.columns([2, 2])
        with c0:
            st.markdown("##### Descripción")
            st.write(
                """
                Fit realizado a partir del día 80, después del primer caso positivo registrado.
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
                    A & = 298,165 \pm 11,26 \\
                    u & = 73,5442 \pm 0,6857 \\
                    r & = 9,04991 \pm 0,683
                \end{aligned}
                $$
                '''
            )
        with c1:
            img01 = im.open('Proyectos/P02/img/fit03.png')
            st.image(img01)
            
        st.markdown("### Fit 08 GNUPlot")
        c0, c1 = st.columns([2, 2])
        with c0:
            st.markdown("##### Descripción")
            st.write(
                """
                Fit realizado a partir del día 81, después del primer caso positivo registrado.
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
                    A & = 1027,2 \pm 584,2 \\
                    u & = 81,1102 \pm 6,36 \\
                    r & = 3,54778 \pm 4,035
                \end{aligned}
                $$
                '''
            )
        with c1:
            img01 = im.open('Proyectos/P02/img/fit01.png')
            st.image(img01)
            
        st.markdown("### Fit 09 GNUPlot")
        c0, c1 = st.columns([2, 2])
        with c0:
            st.markdown("##### Descripción")
            st.write(
                """
                Fit realizado a partir del día 183, después del primer caso positivo registrado.
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
                    A & = 972,387 \pm 34,67 \\
                    u & = 136,241 \pm 1,767 \\
                    r & = 37,6463 \pm 1,975
                \end{aligned}
                $$
                '''
            )
        with c1:
            img01 = im.open('Proyectos/P02/img/fit06.png')
            st.image(img01)
            
        st.markdown("### Fit 10 GNUPlot")
        c0, c1 = st.columns([2, 2])
        with c0:
            st.markdown("##### Descripción")
            st.write(
                """
                Fit realizado a partir del día 367, después del primer caso positivo registrado.
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
                    A & = 678,576 \pm 27,98 \\
                    u & = 230,504 \pm 8,664 \\
                    r & = 139,61 \pm 11,36
                \end{aligned}
                $$
                '''
            )
        with c1:
            img01 = im.open('Proyectos/P02/img/fit05.png')
            st.image(img01)
            
        st.markdown("### Fit 11 GNUPlot")
        c0, c1 = st.columns([2, 2])
        with c0:
            st.markdown("##### Descripción")
            st.write(
                """
                Fit realizado a partir del día 368, después del primer caso positivo registrado.
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
                    A & = 0 \pm 0 \\
                    u & = 0 \pm 0 \\
                    r & = 0 \pm 0
                \end{aligned}
                $$
                '''
            )
        with c1:
            img01 = im.open('Proyectos/P02/img/fit02.png')
            st.image(img01)