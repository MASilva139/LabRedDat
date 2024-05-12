from streamlit_option_menu import option_menu
from streamlit_extras.stylable_container import stylable_container as stycont
from streamlit.components.v1 import html
import streamlit as st
import pandas as pd

def app():
    with open('Proyectos/P04/form01.css') as f:
        css = f.read()

    # Añade tu CSS
    st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)
    
    st.title('Proyecto 04: Machine Learning')
    
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
                En la siguiente práctica se procedió a realizar un fit del decaimiento radiactivo del aire y del cesio-137, para una distribución Gaussiana y una distribución de Poisson y posteriormente se realizó la prueba de $$\chi^{2}$$ para comprobar la certeza de los ajustes realizados. Para obtener los datos se realizaron 250 mediciones con un contador de Geiger, primero sin utilizar ningún material (medición del aire) y después utilizando el cesio-137. Para realizar las gráficas se utilizó ```Plotly-express```, con lo cual se colocó el histograma y la curva de ajuste, y para obtener los valores de la curva de ajuste de la distribución Gaussiana se utilizó ```GNUPlot```, mientras que para la curva de ajuste de la distribución de Poisson se definió únicamente una función.

                Empleando el programa de ```GNUPlot``` se determinaron los valores de las constantes de la ecuación de Distribución Gaussiana $$A$$, $$\mu$$ y $$\sigma$$, realizando un fit sobre los datos del aire, del cesio-137 y los datos agrupados de cinco en cinco del cesio-137. Siendo estos valores $$A=63.5727$$, $$\mu=2.1887$$ y $$\sigma=1.59887$$; $$A=5.09274$$, $$\mu=442.826$$ y $$\sigma=19.5845$$; $$A=25.382$$, $$\mu=439.84$$ y $$\sigma=19.6525$$; para cada medición respectivamente. Se vectorizó la función de distribución Gaussiana para poder introducir diferentes valores de $$x$$ como una lista y con ello poder graficar la curva de ajuste respecto a los datos. Para la definición de la distribución de Poisson, primero se calculó el valor de $$\mu$$ y con este se procedió a realizar la función de Poisson como se presenta en el marco téorico. Para dicha función se empleó la librería ``mpmath`` dado que la librería ``math`` no soporta valores numéricos muy grandes (ocasionados por la exponencial), y con ello se procede a retornar la función de Poisson como un flotante ``return float($$P_{P}(x)$$)`` y se vectorizó, para poder introducir diferentes valores de $$x$$ como una lista.
                
                A partir de la definición matemática de $$\chi^{2}$$, presentada en el marco teórico, se determinó el valor individual de $$\chi^{2}$$ para cada dato de las diferentes distribuciones y con esta prueba se determinó que distribución se adecuaba mejor a los datos experimentales. Repitiendo el procedimiento se realizó la misma prueba excluyendo los datos experimentales que generaban un valor elevado de $$\chi^{2}$$, es decir, aquellos que se salían del rango usual de medición, para comparar estos resultados con los obtenidos con anterioridad.
            """
            )
            st.markdown("## Marco Teórico")
            
            d = {'Comando': ['pwd','cd','load [fichero]','clear','exit/quit','plot','splot','replot'], 'Descripción': ['Indica cual es el directorio por defecto.','Cambia el directorio por defecto. El path del directorio se puede indicar en forma absoluta o relativa.','Si [fichero] es un script contiene comandos gnuplot, esta orden ejecuta dichos comandos. Cuando se termina, se vuelve al modo interactivo.','Borra el terminal gráfico.','En la línea de comandos de gnuplot, terminan la ejecución del programa.','Para dibujar curvas planas y gráficos 2D.','Para dibujar superficies.','Para hacer modificaciones de un plot o un splot anterior.']}
            df = pd.DataFrame(d)
            
            # A partir de aquí se escribe para el marco teórico
            st.write(
                r"""
                ### Machine learning vs. deep learning vs. redes neuronales
                
                Dado que el deep learning y el machine learning tienden a utilizarse indistintamente, conviene señalar los matices entre ambos. El machine learning, el deep learning y las redes neuronales son subcampos de la inteligencia artificial. Sin embargo, las redes neuronales son en realidad un subcampo del machine learning, y el deep learning es un subcampo de las redes neuronales.

                La forma en que el deep learning y el machine learning difieren es en cómo aprende cada algoritmo. El "deep" machine learning puede utilizar conjuntos de datos etiquetados, también conocido como aprendizaje supervisado, para informar a su algoritmo, pero no requiere necesariamente un conjunto de datos etiquetados. El proceso de deep learning puede ingerir datos no estructurados en su forma bruta (por ejemplo, texto o imágenes) y determinar automáticamente el conjunto de características que distinguen unas categorías de datos de otras. Esto elimina parte de la intervención humana necesaria y permite utilizar grandes cantidades de datos. 
                
                El machine learning clásico, o "no profundo", depende más de la intervención humana para aprender. Los expertos humanos determinan el conjunto de características para comprender las diferencias entre las entradas de datos, lo que suele requerir datos más estructurados para aprender.

                Las redes neuronales, o redes neuronales artificiales (RNA), se componen de capas de nodos, que contienen una capa de entrada, una o más capas ocultas y una capa de salida. Cada nodo, o neurona artificial, se conecta a otro y tiene un peso y un umbral asociados. Si la salida de cualquier nodo individual está por encima del valor umbral especificado, ese nodo se activa y envía datos a la siguiente capa de la red. En caso contrario, ese nodo no transmite ningún dato a la siguiente capa de la red. El término "deep" (profundo) en deep learning se refiere al número de capas de una red neuronal. Una red neuronal que consta de más de tres capas (que incluirían la entrada y la salida) puede considerarse un algoritmo de deep learning o una red neuronal profunda. Una red neuronal que sólo tiene tres capas no es más que una red neuronal básica.
                
                ### Métodos de machine learning
                
                #### Machine learning supervisado
                
                El aprendizaje supervisado, también conocido como machine learning supervisado, se define por su uso de conjuntos de datos etiquetados para entrenar algoritmos que clasifiquen datos o predigan resultados con precisión. A medida que se introducen datos de entrada en el modelo, éste ajusta sus ponderaciones hasta que se ha ajustado adecuadamente. Esto ocurre como parte del proceso de validación cruzada para garantizar que el modelo evite el sobreajuste o el infraajuste. El aprendizaje supervisado ayuda a las organizaciones a resolver una variedad de problemas del mundo real a escala, como clasificar el spam en una carpeta separada de su bandeja de entrada. Algunos métodos utilizados en el aprendizaje supervisado son las redes neuronales, el clasificador bayesiano ingenuo, la regresión lineal y logística, el bosque aleatorio y la máquina de vectores de soporte (SVM).
                
                #### Machine learning no supervisado
                
                El aprendizaje no supervisado, también conocido como machine learning no supervisado, utiliza algoritmos de machine learning para analizar y agrupar conjuntos de datos no etiquetados (subconjuntos denominados clústeres). Estos algoritmos descubren patrones ocultos o agrupaciones de datos sin necesidad de intervención humana. La capacidad de este método para descubrir similitudes y diferencias en la información lo hace ideal para el análisis exploratorio de datos, las estrategias de venta cruzada, la segmentación de clientes y el reconocimiento de imágenes y patrones. También se utiliza para reducir el número de características de un modelo mediante el proceso de reducción de la dimensionalidad. El análisis de componentes principales (PCA) y la descomposición en valores singulares (DVE) son dos métodos habituales para ello. Otros algoritmos utilizados en el aprendizaje no supervisado son las redes neuronales, el k-medias y los métodos de agrupación probabilística.
                
                #### Aprendizaje semisupervisado
                
                El aprendizaje semisupervisado ofrece un término medio entre el aprendizaje supervisado y el no supervisado. Durante el entrenamiento, utiliza un conjunto de datos etiquetados más pequeño para guiar la clasificación y la extracción de características a partir de un conjunto de datos más grande sin etiquetar. El aprendizaje semisupervisado puede resolver el problema de no disponer de suficientes datos etiquetados para un algoritmo de aprendizaje supervisado. También ayuda si etiquetar los datos suficientes resulta demasiado costoso.
                
                ### Introducción a Machine Learning
                
                De un data set ($$ds$$) tira a un learner ($$L$$) y ello tira a una función de peso ($$W$$), donde el data set es la lista que contiene pares ($$x$$, $$y$$) conocidos, El Learner se encarga de encontrar el vector de peso. Se tiene una función que depende de la variable $$x$$, tal que
                """
                r'''
                $$ 
                x \longrightarrow \vec{\phi}(x)
                $$
                '''
                r"""
                donde $$\vec{\phi}(x)$$ es el vector de característica (feature vector) definido como
                """
                r'''
                $$ 
                f(x): \hspace{10pt} x \longmapsto \vec{\phi}(x)
                $$
                '''
                r"""
                Con el vector de peso de peso $$W$$ y el vector de característica se define al $$Score()$$, siendo este el producto punto entre dichos vectores
                """
                r'''
                $$ 
                Score\left( \vec{\phi}(x),\hspace{2pt}\vec{W} \right) = \vec{W}\cdot\vec{\phi}(x)
                $$
                '''
                r"""
                Y a partir del $$Score()$$ se define a la función $$y$$, que da tres posibles resultados
                """
                r'''
                $$ 
                y\left( Score\left( \vec{\phi}(x),\hspace{2pt}\vec{W} \right) \right) = 
                \left\{
                \begin{aligned}
                    1 \hspace{3pt};\hspace{10pt} Score\left( \vec{\phi}(x),\hspace{2pt}\vec{W} \right)>0 \\
                    ? \hspace{3pt};\hspace{10pt} Score\left( \vec{\phi}(x),\hspace{2pt}\vec{W} \right)=0 \\
                    0 \hspace{3pt};\hspace{10pt} Score\left( \vec{\phi}(x),\hspace{2pt}\vec{W} \right)<0
                \end{aligned}
                \right.
                $$
                '''
                r"""
                donde se tiene que $$y$$ es un clasificador lineal. Sin embargo, para tener valores diferentes de 0 se tiene que 
                """
                r'''
                $$ 
                y\left( Score\left( \vec{\phi}(x),\hspace{2pt}\vec{W} \right) \right) = 
                \left\{
                \begin{aligned}
                    1 \hspace{3pt};\hspace{10pt} Score\left( \vec{\phi}(x),\hspace{2pt}\vec{W} \right)>0 \\
                    ? \hspace{3pt};\hspace{10pt} Score\left( \vec{\phi}(x),\hspace{2pt}\vec{W} \right)=0 \\
                    -1 \hspace{3pt};\hspace{10pt} Score\left( \vec{\phi}(x),\hspace{2pt}\vec{W} \right)<0
                \end{aligned}
                \right.
                $$
                '''
                r"""
                El training data set se define por
                """
                r'''
                $$ 
                T_{ds} = \left\{ \left(\phi_{1} \hspace{2pt},\hspace{3pt} y_{1}\right) \hspace{2pt},\hspace{3pt} \left(\phi_{2} \hspace{2pt},\hspace{3pt} y_{2}\right) \hspace{2pt},\hspace{3pt} \dots \hspace{2pt},\hspace{3pt} \left(\phi_{n} \hspace{2pt},\hspace{3pt} y_{n}\right) \right\}
                $$
                '''
                r"""
                La pérdida, conocida como función $$loss()$$, se define de la siguiente forma
                """
                r'''
                $$ 
                loss\left( \vec{W} ,\hspace{2pt} \vec{\phi}(x) ,\hspace{2pt} y, \hspace{2pt} Score\left( \vec{\phi}(x),\hspace{2pt}\vec{W} \right) \right) = \left| \left[ \vec{\phi}(x)\cdot\vec{W}\leq0 \right] \right.
                $$
                '''
                r"""
                Hay una cantidad dada por el producto del $$Score()$$ y $$y()$$, tal que a esta cantidad se le denominará como $$P_{\pi2}()$$
                """
                r'''
                $$ 
                P_{\pi2} = Score\left( \vec{\phi}(x),\hspace{2pt}\vec{W} \right) * y\left( Score\left( \vec{\phi}(x),\hspace{2pt}\vec{W} \right) \right)
                $$
                '''
                r"""
                Se tiene que $$P_{\pi2}$$ sirve para evaluar el valor del vector de peso. Una función $$loss()$$ se le conoce como
                """
                r'''
                $$ 
                loss_{0-1} = \left| \left[ \left( \vec{W}\cdot\vec{\phi}(x) \right)y \leq 0 \right] \right.
                $$
                '''
                r"""
                donde $$\left|\right.$$ denota un operador que retorna valores booleanos, es decir, 0 y 1. Para minimizar la función $$loss_{0-1}$$ se busca otra función que se pueda derivar, empleando para ello el descenso del gradiente. Para ello se tiene que $$loss_{hinge}$$ es otra función $$loss$$ que da
                """
                r'''
                $$ 
                loss_{hinge} = 
                \left\{ 
                    \begin{aligned}
                        -P_{\pi2}+1 & \hspace{5pt};\hspace{10pt} P_{\pi2}\leq1 \\
                        0 & \hspace{5pt};\hspace{10pt} P_{\pi2}>1
                    \end{aligned}
                \right.
                $$
                '''
                r"""
                Del mismo modo
                """
                r'''
                $$ 
                loss_{hinge} = 
                \left\{ 
                    \begin{aligned}
                        -P_{\pi2}+y & \hspace{5pt};\hspace{10pt} P_{\pi2} \leq y \\
                        0 & \hspace{5pt};\hspace{10pt} P_{\pi2} > y
                    \end{aligned}
                \right.
                $$
                '''
                r"""
                Entonces, si el vector característico se define por
                """
                r'''
                $$ 
                \vec{\phi}(x) = \left( \phi_{1} \hspace{2pt},\hspace{5pt} \phi_{2} \hspace{2pt},\hspace{5pt} \phi_{3} \hspace{2pt},\hspace{5pt} \dots \hspace{2pt},\hspace{5pt} \phi_{n} \right)
                $$
                '''
                r"""
                y se considera el vector de peso como
                """
                r'''
                $$ 
                \vec{W} = \left( W_{1} \hspace{2pt},\hspace{5pt} W_{2} \hspace{2pt},\hspace{5pt} W_{3} \hspace{2pt},\hspace{5pt} \dots \hspace{2pt},\hspace{5pt} W_{n} \right)
                $$
                '''
                r"""
                Por lo tanto, el gradiente, definido en las diferentes componentes del espacio, esta dado por
                """
                r'''
                $$ 
                \nabla{loss_{hinge}} = \frac{\partial\left[ loss_{hinge} \right]}{\partial\vec{W}} + \frac{\partial\left[ loss_{hinge} \right]}{\partial\vec{\phi}}
                $$
                '''
                r"""
                Considerando coordenadas cartesianas $$\left(x_{1},x_{2},\dots,x_{n}\right)$$, se tiene que para dos dimensiones 
                """
                r'''
                $$ 
                \nabla{loss_{hinge}} = \frac{\partial}{\partial W_{1}}\left[-\left( \phi_{1}W_{1}+\phi_{2}W_{2} \right)y+1\right]\boldsymbol{\hat{x}_{1}} + \frac{\partial}{\partial W_{2}}\left[-\left( \phi_{1}W_{1}+\phi_{2}W_{2} \right)y+1\right]\boldsymbol{\hat{x}_{2}}
                $$
                '''
                r"""
                Como el vector de característica $$\vec{\phi}(x)$$ no es variable, se tiene que 
                """
                r'''
                $$ 
                \frac{\partial\left[ loss_{hinge} \right]}{\partial\vec{\phi}} = 0
                $$
                '''
                r"""
                Con ello, se tiene que
                """
                r'''
                $$
                \begin{aligned}
                    \nabla{loss_{hinge}} & = \left[- \left( \frac{\partial W_{1}}{\partial W_{1}} \phi_{1} + \frac{\partial \phi_{1}}{\partial W_{1}} W_{1} \right)y \right] \boldsymbol{\hat{x}_{1}} + \left[- \left( \frac{\partial W_{2}}{\partial W_{2}} \phi_{2} + \frac{\partial \phi_{2}}{\partial W_{2}} W_{2} \right)y \right] \boldsymbol{\hat{x}_{2}} \\
                    \nabla{loss_{hinge}} & = - \left( \phi_{1} \boldsymbol{\hat{x}_{1}} + \phi_{2} \boldsymbol{\hat{x}_{2}} \right) y
                \end{aligned}
                $$
                '''
                r"""
                De manera general, se tiene que para $$n$$ dimensiones el gradiente de la función $$loss_{hinge}$$
                """
                r'''
                $$
                \begin{aligned}
                    \nabla{loss_{hinge}} & = -\vec{\phi}y
                \end{aligned}
                $$
                '''
                r"""
                Donde el gradiente de la función $$loss_{hinge}$$ puede tener dos posibles soluciones
                """
                r'''
                $$
                \nabla{loss_{hinge}} = \frac{\partial}{\partial\vec{W}}
                \left\{
                \begin{aligned}
                    -\left( \vec{W}\cdot\vec{\phi}(x) \right)y + 1 & \hspace{2pt};\hspace{10pt} P_{\pi2}\leq1 \\
                    0 & \hspace{2pt};\hspace{10pt} P_{\pi2}>1
                \end{aligned}
                \right.
                $$
                '''
            )
                
        if opt == "Referencias":
            st.markdown("## Referencias bibliográficas (marco teórico)")
            wpages1 = ['Anónimo. (n.d.) ¿Qué es el machine learning (ML)?, [En línea]. Recuperado de: https://www.ibm.com/es-es/topics/machine-learning']
            st.write(wpages1)
            
            st.markdown("## Referencias bibliográficas (documentación)")
            wpages2 = ['Anónimo, (n.d.). Streamlit-extras. Recuperado de: https://extras.streamlit.app','KaTeX. (2024). Supported Functions. Recuperado de: https://katex.org/docs/supported.html','Pandas documentation, (2024). pandas.DataFrame. Recuperado de: https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html','Streamlit Inc. (n.d.). st.columns. Recuperado de: https://docs.streamlit.io/library/api-reference/layout/st.columns','Streamlit Inc. (n.d.). st.markdown. Recuperado de: https://docs.streamlit.io/library/api-reference/text/st.markdown','Streamlit Inc. (n.d.). st.radio. Recuperado de: https://docs.streamlit.io/library/api-reference/widgets/st.radio','Streamlit Inc. (n.d.). st.set_page_config. Recuperado de: https://docs.streamlit.io/library/api-reference/utilities/st.set_page_config', 'Streamlit Inc. (n.d.). st.slider. Recuperado de: https://docs.streamlit.io/library/api-reference/widgets/st.slider','Streamlit Inc. (n.d.). st.table. Recuperado de: https://docs.streamlit.io/develop/api-reference/data/st.table','Streamlit Inc. (n.d.). st.write. Recuperado de: https://docs.streamlit.io/library/api-reference/write-magic/st.write']
            st.write(wpages2)
            
