import streamlit as st
from PIL import Image as im

def app():
    c1, c2 = st.columns([1,5])
    with c1:
        opt = st.radio(
            "***SECCIONES:***", ["Marco Teórico", "Problema"]
        )
    
    with c2:   
        if opt == "Marco Teórico":
            st.title("Marco Teórico")
            # A partir de aquí se escribe para el marco teórico
            st.write(
                """
                ## Distribución binomial
            
                Es una distribución de probabilidad discreta que cuenta la cantidad de éxitos en $$n$$ casos con una
                probabilidad fija $$p$$. Se caracteriza porque únicamente existe dos casos: éxito y fracaso. Además la
                probabilidad $$p$$ es fija, lo que quiere decir que la probabilidad de éxito o fracaso en cada uno de
                los casos no depende de lo que haya sucedido en el anterior.
            
                ### Fórmula
                """
                r'''
                $$
                P_b(x,n)=\begin{pmatrix}
                    n\\
                    x
                \end{pmatrix}
                p^x(1-p)^{n-x}=\frac{n!}{x!(n-x)!}\cdot p^x(1-p)^{n-x}
                $$
                '''
                """
                Donde $$P_b(x,n)$$ es la probabilidad de $$x$$ aciertos en $$n$$ ensayos, cada uno con probabilidad
                $$p$$.
            
                ### Media y desviación estándar
            
                La media de una distribución binomial es de la forma:
                """
                r'''
                $$
                \mu=np
                $$
                '''
                """
                La desviación estándar viene dada por:
                """
                r'''
                $$
                \sigma=\sqrt{npq}=\sqrt{np(1-p)}
                $$
                '''
            )
            
        if opt == "Problema":
            st.title("Definición del problema o caso de estudio")
            # A partir de aquí se escribe para la definición del problema
            
