import streamlit as st
import plotly.express as px
import pandas as pd


# Agregar título a la página
st.title('Pingüinos')

# Agregar texto a la página
st.write('Gráfica de pingüinos y prueba de streamlit.')

# Agregar texto con formato Markdown a la página
st.markdown('# Gráfica\n## Bill depth (mm)- Flipper lenght (mm)\nGráfica donde el eje horizontal representa la profundidad del pico y el eje vertical la longitud de las aletas. Al final del documento se mostrará la tabla de datos utilizada para dicha gráfica.')

# Leer datos de pinguinos como lo trabajado en el cuaderno
data = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv')

# Los prints solo serán visibles en la terminal pero no en la página de Streamlit.
print(data)

# Generar la gráfica a partir de los datos y guardarla en una variable llamada grafica.
grafica = px.scatter(data,'bill_depth_mm','flipper_length_mm','species',symbol='sex',)

# Agregar la gráfica a la página
st.plotly_chart(grafica)

# Agregar tabla de datos
st.write("### Tabla de datos", data.sort_index())