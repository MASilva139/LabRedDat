from streamlit_option_menu import option_menu
from streamlit_extras.stylable_container import stylable_container as stycont
from streamlit.components.v1 import html
import streamlit as st
import pandas as pd

def app():
    with open('Proyectos/P03/form01.css') as f:
        css = f.read()

    # Añade tu CSS
    st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)
    
    st.title('Proyecto 03: Decaimiento de Cesio-137')
    
    c1, c2 = st.columns([1,5])
    with c1:
        #########################################################
        ##                       st.radio()                    ##
        #########################################################
        
        opt = st.radio("", ["Proyecto", "Referencias"], label_visibility="collapsed")
        
    with c2: 
        #########################################################
        ##                       st.radio                      ##
        #########################################################
        if opt == "Proyecto":
            st.markdown("## Resumen / Caso de estudio")
            st.write(
            """
                En la siguiente prácita se procedio a realizar un fit del decaimiento radiactivo del aire y del cesio-137, para una distribución Gaussiana y una distribución de Poisson.
                Para obtener los datos se realizaron 250 mediciones con un contador de Geiger, primero sin utilizar ningún material (medición del aire) y después utilizando el
                cesio-137. Para realizar las gráficas se utilizó ```Plotly-express```, con lo cual se colocó el histograma y la curva de ajuste, y para obtener los valores de la
                curva de ajuste de la distribución Gaussiana se utilizó ```GNUPlot```, mientras que para la curva de ajuste de la distribución de Poisson se definió únicamente una
                función.

                Empleando el programa de ```GNUPlot``` se determinaron los valores de las constantes de la ecuación de Distribución Gaussiana $$A$$, $$\mu$$ y $$\sigma$$, realizando un
                fit sobre los datos del aire, del cesio-137 y los datos agrupados de cinco en cinco del cesio-137. Siendo estos valores $$A=63.5727$$, $$\mu=2.1887$$ y $$\sigma=1.59887$$; 
                $$A=5.09274$$, $$\mu=442.826$$ y $$\sigma=19.5845$$; $$A=25.382$$, $$\mu=439.84$$ y $$\sigma=19.6525$$; para cada medición respectivamente.Se vectorizó la función de 
                distribución Gaussiana para poder introducir diferentes valores de $$x$$ como una lista y con ello poder graficar la curva de ajuste respecto a los datos.
            """
            )
            st.markdown("## Marco Teórico")
            
            d = {'Comando': ['pwd','cd','load [fichero]','clear','exit/quit','plot','splot','replot'], 'Descripción': ['Indica cual es el directorio por defecto.','Cambia el directorio por defecto. El path del directorio se puede indicar en forma absoluta o relativa.','Si [fichero] es un script contiene comandos gnuplot, esta orden ejecuta dichos comandos. Cuando se termina, se vuelve al modo interactivo.','Borra el terminal gráfico.','En la línea de comandos de gnuplot, terminan la ejecución del programa.','Para dibujar curvas planas y gráficos 2D.','Para dibujar superficies.','Para hacer modificaciones de un plot o un splot anterior.']}
            df = pd.DataFrame(d)
            
            # A partir de aquí se escribe para el marco teórico
            st.write(
                r"""
                ### Cesio
                
                Es un metal de color blanco argénteo muy reactivo que cristaliza en pequeños octaedros. Se caracteriza por su baja dureza. Tiene el puesto más alto en la serie electromotriz; posee también el punto de fusión más bajo de cualquier otro metal y el más bajo potencial iónico de cualquier elemento. Tiene un único isótopo estable, de masa atómica 133. Químicamente presenta el número de oxidación +1. El cesio se oxida con facilidad y arde fácilmente en presencia del aire a temperatura ambiente. Es soluble en alcohol y ácidos.
                
                #### Cesio-137
                
                Es un isótopo radiactivo del cesio que se produce principalmente por fisión nuclear. Tiene un periodo de semidesintegración de 30,23 años y decae emitiendo partículas beta a un isómero nuclear metaestable de Bario-137. El Bario-137 tiene un periodo de semidesintegración de 2,65 minutos.
                
                ### Decaimiento radiactivo
                
                Es un proceso en el que un núcleo inestable se transforma en uno más estable, emitiendo patículas y/o fotones y liberando energía durante el proceso. 
                Una sustancia que experimenta este fenómeno espotáneamente se denomina sustancia radioactiva. Pueden emitir tres tipos de radiación:
                - Radiación $$\alpha$$
                - Radiación $$\beta$$
                - Radiación $$\gamma$$
                
                En general, los núcleos de los distintos elementos no son estables. Emiten espontáneamente partículas cargadas y radiación electromagnética. Este fenómeno se conoce como radiactividad natural.
                
                Los núcleos excitados se desexcitan mediante tres tipos de decaimiento: 
                - $$\alpha$$: consiste en la emisión de helio doblemente ionizados.
                - $$\beta$$: consiste en la emisión de partículas beta, electrones o positrones.
                - $$\gamma$$: cuando la desexcitación se lleva a cabo mediante la emisión de radiación electromagnética.
                
                La desintegración radiactiva es un fenómeno naturalmente estadístico. Las hipótesis con las cuales se trabaja para el estudio de las desintegraciones radiactivas son:
                - Dado un intervalo temporal, todos los átomos de una muestra tienen la misma probabilidad de desintegrarse en dicho intervalo.
                - La desintegración de un átomo es un evento independiente de la desintegración de los demás átomos de la muestra.
                - La probabilidad de desintegración de un átomo en un intervalo temporal permanece constante para todo intervalo temporal de la misma duración.
                
                Las fluctuaciones en el número de desintegraciones están representadas por una distribución de Poisson
                """
                r'''
                $$
                P_{P}(x) = \frac{\mu^{x}e^{-\mu}}{x!}
                $$
                '''
                r"""
                Esta distribución expresa la probabilidad $$P_{P}(x)$$ de que en cierto intervalo se observa un número entero $$x$$ de desintegraciones, siendo $$\mu$$ el número de desintegraciones predicho.
                
                ### Contador de Geiger
                Un contador Geiger-Müller es un dispositivo que permite detectar radiaciones ionizantes, es decir, radiación alfa, beta, gamma, fotones y rayos X. Fue inventado en 1928 en Kiel, Alemania, por los físicos Hans Geiger y Walter Müller. El modo de funcionamiento de cualquier contador Geiger se basa en un principio simple: Los iones producidos por las radiaciones, al atravesar el volumen activo del detector, son acelerados por un campo eléctrico, produciendo un pulso de corriente que señala el paso de radiación.
                
                ### Prueba $$\chi$$-cuadrado $$\left(\chi^{2}\right)$$
                Esta prueba puede utilizarse con datos medibles en una escala nominal. La hipótesis nula de la prueba $$\chi^{2}$$ postula una distribución de probabilidad totalmente específicada.
                
                Para realizar este contraste se disponen los datos en una tabla de frecuencias. Para cada valor o intervalo de valores se indica la frecuencia absoluta observada o empirica $$(x_{i})$$. A continuación, y suponiendo que la hipótesis nula es cierta, se calculan para cada valor o intervalo de valores la frecuencia absoluta que cabría esperar o frecuencia esperada
                """
                r'''
                $$
                \Omicron_{i} = n\cdot p_{i}
                $$
                '''
                r"""
                donde $$n$$ es el tamaño de la muestra y $$p_{i}$$ la probabilidad del $$i$$-ésimo valor o intervalo de valores según la hipótesis nula. La hipótesis nula es cierta si $$n\rightarrow\infty$$, de manera que la prueba $$\chi^{2}$$ se define por
                """
                r'''
                $$
                \chi^{2} = \sum_{i=1}^{k}\frac{\left(x_{i}-\Omicron_{i}\right)^{2}}{\Omicron_{i}}
                $$
                '''
                r"""
                Esta ecuación tiene una distribución $$\chi^{2}$$ con $$k-1$$ grados de libertad si $$n$$ es suficientemente grande, es decir, si todas las frecuencias esperadas son mayores que 5.
                
                Si existe concordancia perfecta entre las frecuencias observadas y las esperadas el estadístico tomará un valor igual a 0; por el contrario, si existe una gran discrepancia entre estas frecuencias el estadístico tomará un valor grande y, en consecuencia, se rechazará la hipótesis nula. Así pues, la región crítica estará situada en el extremo superior de la distribución $$\chi^{2}$$ con $$k-1$$ grados de libertad.
                """
            )
            st.write(
                """
                ### Distribución Normal
            
                También conocida como distribución de Gauss, es una distribución de variable continua, con campo de variación $$(-\infty, \infty)$$. Esta queda especificada por dos parámetros de los que depende su función de densidad y que resultan ser la media $$\mu$$ y la dsviación típica de la distribución $$\sigma$$. Su estudio teórico suele introducirse directamente a partir de su función de densidad.
                
                Dado que depende de dos parámetros, $$\mu$$ y $$\sigma$$, el hecho de que una variable $$X$$ se distribuya con una distribución normal de media $$\mu$$ y desviación típica $$\sigma$$ se representa por la siguiente expresión:
                """
                r'''
                $$
                X \rightarrow N \left[\mu : \sigma\right] \hspace{20pt} \| \hspace{20pt} L(X) \rightarrow N \left[\mu : \sigma\right]
                $$
                '''
                """
                Por tanto, se tiene que la función de densidad está dada por 
                """
                r'''
                $$
                f(x) = \frac{1}{\sigma\sqrt{2\pi}}e^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^{2}} \hspace{20pt} \forall x \in \Re
                $$
                '''
                """
                Las características de dicha función de densidad son:
                """
                '''
                1. Si se realiza la primera derivada de la función se tiene que
                '''
                r'''
                $$
                f'(x) = -\frac{\left(x-\mu\right)}{{\sigma}^{3}\sqrt{2\pi}}e^{-\frac{1}{2}\left(\frac{x-\mu}{\sigma}\right)^{2}} \longrightarrow f'(x) = -\frac{\left(x-\mu\right)}{\sigma^{2}}\cdot f(x)
                $$
                '''
                '''
                2. Si se realiza la segunda derivada de la función se tiene que
                '''
                r'''
                $$
                f''(x) = \frac{\left(x-\mu\right)^{2}-\sigma^{2}}{\sigma^{4}}\cdot f(x)
                $$
                '''
                """
                Al igualar a cero la primera derivada se obtiene que $$f'(x)=0$$ para $$X=\mu$$ y para $$X=\infty$$. Como la segunda derivada en $$X=\mu$$ es negativa, se puede concluir que la función de densidad presenta un máximo en $$X=\mu$$, lo que afir,a que la media es también la moda de la distribución normal.
                
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
                #### GNUPlot
            
                Es un programa de visualización gráfica de datos científicos. Permite realizar gráficos 2D y 3D de curvas, líneas de nivel y superficies, tanto a partir de funciones como de datos discretos. Este software funciona mediante comandos, que pueden usarse en modo interactivo como escribiendo scripts; es decir, la secuencia de comandos escritos en un fichero.\n
                Algunos comandos son:
                """
            )
            st.table(df)
                
        if opt == "Referencias":
            st.markdown("## Referencias bibliográficas (marco teórico)")
            wpages1 = ['Universitat de Barcelona. (n.d.) Prueba Chi-cuadrado, [En Línea]. Recuperado de: http://www.ub.edu/aplica_infor/spss/cap5-2.htm','CEACES, (n.d.). Distribución normal, [PDF]. Recuperado de https://www.uv.es/ceaces/pdf/normal.pdf','Ciocci, L., Acuña, G. (2001) Estudio de la estadística del decaimiento radiactivo [PDF]. Buenos Aires. Recuperado de: http://users.df.uba.ar/sgil/labo5_uba/inform/info/pautadas/estadistica_decaimiento_ligia.pdf', "Echevarría, R. (n.d.). Breve Introducción a GNUPlot. Recuperado de https://personal.us.es/echevarria/documentos/APUNTESgnuplot.pdf",'Navarro, F. (2004) La Enciclopedia Vol 4. Madrid: Salvat.','Wikipedia. (2022) Cesio-137 [En línea]. Recuperado de: https://es.wikipedia.org/wiki/Cesio-137']
            #https://www.ugr.es/~bioestad/guiaspss/practica6/ (prueba chi-cuadrado, universidad de granada)
            st.write(wpages1)
            
            st.markdown("## Referencias bibliográficas (documentación)")
            wpages2 = ['Anónimo, (n.d.). Streamlit-extras. Recuperado de: https://extras.streamlit.app','KaTeX. (2024). Supported Functions. Recuperado de: https://katex.org/docs/supported.html','Pandas documentation, (2024). pandas.DataFrame. Recuperado de: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html','Streamlit Inc. (n.d.). st.columns. Recuperado de: https://docs.streamlit.io/library/api-reference/layout/st.columns','Streamlit Inc. (n.d.). st.markdown. Recuperado de: https://docs.streamlit.io/library/api-reference/text/st.markdown','Streamlit Inc. (n.d.). st.radio. Recuperado de: https://docs.streamlit.io/library/api-reference/widgets/st.radio','Streamlit Inc. (n.d.). st.set_page_config. Recuperado de: https://docs.streamlit.io/library/api-reference/utilities/st.set_page_config', 'Streamlit Inc. (n.d.). st.slider. Recuperado de: https://docs.streamlit.io/library/api-reference/widgets/st.slider','Streamlit Inc. (n.d.). st.table. Recuperado de: https://docs.streamlit.io/develop/api-reference/data/st.table','Streamlit Inc. (n.d.). st.write. Recuperado de: https://docs.streamlit.io/library/api-reference/write-magic/st.write']
            st.write(wpages2)
            
