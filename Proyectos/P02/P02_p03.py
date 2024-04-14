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
        c32, c33 = st.columns([2, 2])
        with c32:
            st.markdown("##### Descripción")
            st.write(
                """
                Fit realizado a partir del día 65, después del primer caso positivo registrado.
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
                    A & = 25513,4 \pm 5,69e+05 \\
                    u & = 194,236 \pm 511,8 \\
                    r & = 40,2838 \pm 71,31
                \end{aligned}
                $$
                '''
            )
        with c33:
            img17 = im.open('Proyectos/P02/img/fit17.png')
            st.image(img17)
            
        st.markdown("### Fit 02 GNUPlot")
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
            
        st.markdown("### Fit 03 GNUPlot")
        c30, c31 = st.columns([2, 2])
        with c30:
            st.markdown("##### Descripción")
            st.write(
                """
                Fit realizado a partir del día 67, después del primer caso positivo registrado.
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
                    A & = 3679,37 \pm 3,657e+04 \\
                    u & = 161,712 \pm 260,6 \\
                    r & = 37,5399 \pm 44,71
                \end{aligned}
                $$
                '''
            )
        with c31:
            img16 = im.open('Proyectos/P02/img/fit16.png')
            st.image(img16)
            
        st.markdown("### Fit 04 GNUPlot")
        c28, c29 = st.columns([2, 2])
        with c28:
            st.markdown("##### Descripción")
            st.write(
                """
                Fit realizado a partir del día 68, después del primer caso positivo registrado.
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
                    A & = 5663,65 \pm 5,77e+04 \\
                    u & = 151,612 \pm 223,3 \\
                    r & = 32,1612 \pm 37,29
                \end{aligned}
                $$
                '''
            )
        with c29:
            img15 = im.open('Proyectos/P02/img/fit15.png')
            st.image(img15)
            
        st.markdown("### Fit 05 GNUPlot")
        c2, c3 = st.columns([2, 2])
        with c2:
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
        with c3:
            img02 = im.open('Proyectos/P02/img/fit07.png')
            st.image(img02)
            
        st.markdown("### Fit 06 GNUPlot")
        c26, c27 = st.columns([2, 2])
        with c26:
            st.markdown("##### Descripción")
            st.write(
                """
                Fit realizado a partir del día 70, después del primer caso positivo registrado.
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
                    A & = 7092,97 \pm 5,647e+04 \\
                    u & = 140,643 \pm 151 \\
                    r & = 27,5726 \pm 25,48
                \end{aligned}
                $$
                '''
            )
        with c27:
            img14 = im.open('Proyectos/P02/img/fit14.png')
            st.image(img14)
            
        st.markdown("### Fit 07 GNUPlot")
        c4, c5 = st.columns([2, 2])
        with c4:
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
        with c5:
            img03 = im.open('Proyectos/P02/img/fit08.png')
            st.image(img03)
            
        st.markdown("### Fit 08 GNUPlot")
        c24, c25 = st.columns([2, 2])
        with c24:
            st.markdown("##### Descripción")
            st.write(
                """
                Fit realizado a partir del día 72, después del primer caso positivo registrado.
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
                    A & = 8063,98 \pm 5,426e+04 \\
                    u & = 134,038 \pm 118 \\
                    r & = 24,9124 \pm 20,35
                \end{aligned}
                $$
                '''
            )
        with c25:
            img13 = im.open('Proyectos/P02/img/fit13.png')
            st.image(img13)
            
        st.markdown("### Fit 09 GNUPlot")
        c22, c23 = st.columns([2, 2])
        with c22:
            st.markdown("##### Descripción")
            st.write(
                """
                Fit realizado a partir del día 73, después del primer caso positivo registrado.
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
                    A & = 7734,52 \pm 4,47e+04 \\
                    u & = 135,621 \pm 105,8 \\
                    r & = 25,6137 \pm 18,53
                \end{aligned}
                $$
                '''
            )
        with c23:
            img12 = im.open('Proyectos/P02/img/fit12.png')
            st.image(img12)
            
        st.markdown("### Fit 10 GNUPlot")
        c6, c7 = st.columns([2, 2])
        with c6:
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
        with c7:
            img04 = im.open('Proyectos/P02/img/fit10.png')
            st.image(img04)
            
        st.markdown("### Fit 11 GNUPlot")
        c8, c9 = st.columns([2, 2])
        with c8:
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
        with c9:
            img05 = im.open('Proyectos/P02/img/fit11.png')
            st.image(img05)
            
        st.markdown("### Fit 12 GNUPlot")
        c10, c11 = st.columns([2, 2])
        with c10:
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
        with c11:
            img06 = im.open('Proyectos/P02/img/fit04.png')
            st.image(img06)
            
        st.markdown("### Fit 13 GNUPlot")
        c12, c13 = st.columns([2, 2])
        with c12:
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
        with c13:
            img07 = im.open('Proyectos/P02/img/fit03.png')
            st.image(img07)
            
        st.markdown("### Fit 14 GNUPlot")
        c14, c15 = st.columns([2, 2])
        with c14:
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
        with c15:
            img08 = im.open('Proyectos/P02/img/fit01.png')
            st.image(img08)
            
        st.markdown("### Fit 15 GNUPlot")
        c16, c17 = st.columns([2, 2])
        with c16:
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
        with c17:
            img09 = im.open('Proyectos/P02/img/fit06.png')
            st.image(img09)
            
        st.markdown("### Fit 16 GNUPlot")
        c18, c19 = st.columns([2, 2])
        with c18:
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
        with c19:
            img10 = im.open('Proyectos/P02/img/fit05.png')
            st.image(img10)
            
        st.markdown("### Fit 17 GNUPlot")
        c20, c21 = st.columns([2, 2])
        with c20:
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
        with c21:
            img11 = im.open('Proyectos/P02/img/fit02.png')
            st.image(img11)