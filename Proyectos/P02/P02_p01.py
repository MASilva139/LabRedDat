from streamlit_option_menu import option_menu
from streamlit_extras.stylable_container import stylable_container as stycont
from streamlit.components.v1 import html
import streamlit as st

def app():
    with open('Proyectos/P02/form01.css') as f:
        css = f.read()

    # Añade tu CSS
    st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)
    
    st.title('Proyecto 02: Predicción de COVID19')
    
    #########################################################
    ##                       javascript                    ##
    #########################################################
    # Define tu JavaScript
    # bjs = """
    # function handleClick() {
    #     // Obtén una referencia a los botones de radio y al elemento de texto
    #     var radios = document.getElementsByClassName('miRadio');
    #     var texto = document.getElementById('texto');

    #     // Cambia el color de fondo y el color del texto del botón de radio cuando se selecciona
    #     for (var i = 0; i < radios.length; i++) {
    #         radios[i].style.backgroundColor = 'green';
    #         radios[i].style.color = 'white';

    #         // Muestra el texto correspondiente
    #         if (radios[i].checked) {
    #             if (radios[i].value == 'Proyecto') {
    #                 texto.innerHTML = '<h2>Proyecto</h2>';
    #             } else if (radios[i].value == 'Referencias') {
    #                 texto.innerHTML = '<h2>Referencias</h2>';
    #             }
    #         }
    #     }
    # }

    # // Agrega un manejador de eventos para el evento 'click' a cada botón de radio
    # window.onload = function() {
    #     var radios = document.getElementsByClassName('miRadio');
    #     for (var i = 0; i < radios.length; i++) {
    #         radios[i].addEventListener('click', handleClick);
    #     }
    # };
    # """
    # # Define tu HTML para los botones de radio
    # html_radio = """
    # <input type="radio" id="proyecto" name="miRadio" class="miRadio" value="Proyecto">
    # <label for="proyecto">Proyecto</label><br>
    # <input type="radio" id="referencias" name="miRadio" class="miRadio" value="Referencias">
    # <label for="referencias">Referencias</label><br>
    # <script>{}</script>
    # """.format(bjs)
    # # Define tu HTML para el texto
    # html_texto = """
    # <div id="texto"></div>
    # """
    
    c1, c2 = st.columns([1,5])
    with c1:
        #########################################################
        ##                       st.radio()                    ##
        #########################################################
        
        opt = st.radio("", ["Proyecto", "Referencias"], label_visibility="collapsed")
        
        #########################################################
        ##                       contenedor                    ##
        #########################################################
        
        # with stycont(
        #         key="menu-01",
        #         css_styles="""
        #         """,
        #     ):
        #     opt = option_menu(
        #         #menu_title='Pages',
        #         None,
        #         options=['Proyecto', 'Referencias'], # Nombre de cada pestaña
        #         icons=['house-fill', 'bezier', 'body-text'], #Iconos de las pestañas
        #         menu_icon='alt',
        #         default_index=0, # En este se define la primera página en mostrarse,
        #         orientation="vertical",
        #         styles={
        #             "container": {"padding": "1!important", "background-color":'transparent'},
        #             "icon":{"color":"white", "font-size":"16px"},
        #             "nav-link":{"color":"white", "font-size": "13px", "text-align":"center", "margin":"0px","--hover-color":"sepia"},
        #             "nav-link-selected":{"background-color":"darkolivegreen"}
        #         }
        #     )
        
        #########################################################
        ##                       javascript                    ##
        #########################################################
        # html(html_radio)
        
    with c2: 
        #########################################################
        ##                       st.radio                      ##
        #########################################################
        if opt == "Proyecto":
            st.markdown("## Resumen / Caso de estudio")
            st.write(
            """
                En la siguiente práctica se procedió a realizar una aplicación web para graficar los datos de los registros de casos de COVID-19 del año 2020 dados por el Ministerio de Salud y a partir de ello predecir el pico de contagios asumiendo que no se cuentan con los datos futuros; empleando para ello la biblioteca de ``Plotly-Express``, para gráficar el histograma y la curva de ajuste, y el programa de ``GNUPlot``, para los valores de la curva de ajuste. \n
                Empleando el programa de ``GNUPlot`` se determinaron los valores de las constantes de la ecuación de Distribución Gaussiana $$A$$, $$\mu$$ y $$\sigma$$, realizando un fit sobre los datos de casos positivos, columna 5 del csv; utilizando 69 datos, comenzando desde el día 13 de marzo del 2020, se determinaron que los valores de las constantes son $$A=$$930.848, $$\mu=$$109.684 y $$\sigma=$$23.3855. Se vectorizó la función de Distribución Gaussiana para poder introducir diferentes valores de $$x$$ como una lista y con ello poder graficar la curva de ajuste respecto a los datos de casos positivos registrados. \n
                Se evaluaron los datos disponibles y se eliminaron aquellos que ocasionaban un sobreajuste al fit, de manera que solamente se utilizaron los valores de los primeros 69 días, debido a que con otros datos el ajuste toma que el pico de casos positivos ya se dio, de manera que los datos solamente decrecerian. De igual manera, se utilizó la distribución Gaussiana, en lugar de la distribución binomial, debido a que al tratarse de datos y no probabilidades, el ajuste que daba la primera de estas era mejor, mientras que con la binomial se hubiese tenido que arreglar la función o los datos para poder realizar el ajuste de la curva.
            """
            )
            st.markdown("## Marco Teórico")
            # A partir de aquí se escribe para el marco teórico
            st.write(
                """
                ### Distribución binomial
            
                Es una distribución de probabilidad discreta que cuenta la cantidad de éxitos en $$n$$ casos con una
                probabilidad fija $$p$$. Se caracteriza porque únicamente existe dos casos: éxito y fracaso. Además la
                probabilidad $$p$$ es fija, lo que quiere decir que la probabilidad de éxito o fracaso en cada uno de
                los casos no depende de lo que haya sucedido en el anterior.
            
                #### Fórmula
                """
                r'''
                $$
                P_{G}(x)=\frac{1}{\sigma\sqrt{2\pi}}e^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^{2}} \longleftrightarrow P_{G}(x)=\frac{1}{\sigma\sqrt{2\pi}} \cdot \exp{\left[-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^{2}\right]}
                $$
                '''
                """
                Donde $$P_G(x)$$ es la distribución gaussiana. La ecuación empleada en la práctica está dada por:
                """
                r'''
                $$
                P_{G}(x)=A\cdot e^{-\frac{1}{2}\left(\frac{x-u}{r}\right)^{2}} \longleftrightarrow P_{G}(x)=A\cdot \exp{\left[-\frac{1}{2}\left(\frac{x-u}{r}\right)^{2}\right]}
                $$
                '''
                """
                #### Media y desviación estándar
            
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
                """
                ### Fit distribución binomial
            
                La librería `scipy.optimize` permite crear un fit personalizado con la opción `curve_fit()`, la cual
                utiliza mínimos cuadrados no lineales para ajustar una función, $$f$$, a los datos proporcionados.
            
                La síntaxis del comando es la siguiente:
            
                ```python
                scipy.optimize.curve_fit(f, xdata, ydata, p0=None, sigma=None, absolute_sigma=False, check_finite=None, bounds=(-inf, inf), method=None, jac=None, *, full_output=False, nan_policy=None, **kwargs)
                ```
                Puede verse la documentación completa [aquí](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html).
                """
            )
            
            # if st.button('Ir al inicio'):
            #     st.write('<meta http-equiv="refresh" content="0">', unsafe_allow_html=True)
                
        if opt == "Referencias":
            st.markdown("## Referencias bibliográficas (marco teórico)")
            wpages1 = ["Scipy Inc. (n.d.). Scipy.Optimize. Recuperado de https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html", '']
            st.write(wpages1)
            
            st.markdown("## Referencias bibliográficas (documentación)")
            wpages2 = ['KaTeX. (2024). Supported Functions. Recuperado de: https://katex.org/docs/supported.html','Streamlit Inc. (n.d.). st.columns. Recuperado de: https://docs.streamlit.io/library/api-reference/layout/st.columns','Streamlit Inc. (n.d.). st.markdown. Recuperado de: https://docs.streamlit.io/library/api-reference/text/st.markdown','Streamlit Inc. (n.d.). st.radio. Recuperado de: https://docs.streamlit.io/library/api-reference/widgets/st.radio','Streamlit Inc. (n.d.). st.set_page_config. Recuperado de: https://docs.streamlit.io/library/api-reference/utilities/st.set_page_config', 'Streamlit Inc. (n.d.). st.radio. Recuperado de: https://docs.streamlit.io/library/api-reference/widgets/st.slider','Streamlit Inc. (n.d.). st.write. Recuperado de: https://docs.streamlit.io/library/api-reference/write-magic/st.write']
            st.write(wpages2)
            
        #########################################################
        ##                       javascript                    ##
        #########################################################
        # html(html_texto)