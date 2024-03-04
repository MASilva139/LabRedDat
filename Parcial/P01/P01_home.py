import streamlit as st
from PIL import Image

def app():
    st.title('Parcial 01: Parte práctica')
    st.markdown('## Página multiapp')
    st.write('Se decidió hacer una página multiapp, siendo esta una de las formas más cómodas encontradas,  para poder mostrar las dos posibles formas para ingresar los valores de la distribución binomial, utilizando en cada una de ellas los comandos que se explicarán en la sección de ***Input Widgets***. Se intentarón implementar ciertos cosas extra, sin embargo, por falta de tiempo y por necesidad de tener una mayor documentación se omitieron para este primer parcial.')
    st.write('En este trabajo se utilizaron las bibliotecas de ***streamlit_option_menu***, ***PIL***, ***streamlit***, ***matplotlib***,***Pandas***, ***math*** y ***NumPy***. De igual manera se utilizaron comandos para crear columnas (con medida relativa) mediante el código *streamlit.columns([ , ])*.')
    st.write('La biblioteca de ***Streamlit***, de uso obligatorio para el trabajo, se utilizó para realizar la página de streamlit. La librería de ***streamlit_option_menu*** se empleo para realizar la aplicación web multiapp, con enlace a diferentes archivos python empleados para el proyecto. La librería de ***PIL*** se empleo para añadir imagenes al documento.')
    
    st.markdown('## Input Widgets (Streamlit)')
    st.write('En este proyecto (parcial) se implementaron los siguientes input widgets (mencionados en el markdown del repositorio):')
    
    k1, k2 = st.columns([1,3])
    
    with k1:
        inp = st.radio('Nombre del widget:', ["***.radio()***", "***.toggle()***", "***.slider()***", "***.input_number()***", "***.selectbox()***"])
    with k2:
        if inp == "***.radio()***":
            st.markdown('## streamlit.radio()')
            st.write('Muestra un widget de boton de radio.')
            st.write('***st.radio(label, options, index=0, format_func=special_internal_function, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, horizontal=False, captions=None, label_visibility="visible")***')
            
        if inp == "***.toggle()***":
            st.markdown('## streamlit.toggle()')
            st.write('Muestra un widget de alternancia.')
            st.write('***st.toggle(label, value=False, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible")***')
            
        if inp == "***.slider()***":
            st.markdown('## streamlit.slider()')
            st.write('Muestra un widget deslizante.')
            st.write('Esto admite tipos *int*, *float*, *date*, *time* y *datetime*.')
            st.write('Esto también le permite representar un control deslizante de rango pasando una tupla de dos elementos o una lista como valor.')
            st.write('La diferencia entre san deslizador y ***st.select_slider*** es esodeslizador solo acepta datos numéricos o de fecha/hora y toma un rango como entrada, mientras que seleccionar_deslizador acepta cualquier tipo de datos y toma un conjunto de opciones iterables.')
            st.write('***st.slider(label, min_value=None, max_value=None, value=None, step=None, format=None, key=None, help=None, on_change=None, args=None, kwargs=None, *, disabled=False, label_visibility="visible")***')
            
        if inp == "***.input_number()***":
            st.markdown('## streamlit.input_number()')
            st.write('Muestra un widget de entrada numérico.')
            st.write('***st.number_input(label, min_value=None, max_value=None, value="min", step=None, format=None, key=None, help=None, on_change=None, args=None, kwargs=None, *, placeholder=None, disabled=False, label_visibility="visible")***')
            
        if inp == "***.selectbox()***":
            st.markdown('## streamlit.selectbox()')
            st.write('Muestra un widget selecto.')
            st.write('***st.selectbox(label, options, index=0, format_func=special_internal_function, key=None, help=None, on_change=None, args=None, kwargs=None, *, placeholder="Choose an option", disabled=False, label_visibility="visible")***')
    