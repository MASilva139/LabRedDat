import streamlit as st
from PIL import Image as im

def app():
    st.title("Conclusiones")
    st.write(
        '''
        - Las gráficas presentadas por ``Plotly.Express`` permiten una mejor representación de los datos que las realizadas por el entorno de ``PyPlot``.
        - Los valores experimentales presentan una muy buena aproximación, respecto a los valores teóricos, con la función binomial.
        - Mientras mayor sea el número de datos, la gráfica toma una forma más parecida a una distribución binomial teórica y los datos $$n$$ y $$p$$ obtenidos por el ajuste son más cercanos a los teóricos.
        '''
    )
