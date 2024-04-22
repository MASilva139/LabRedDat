import pandas as pd
import plotly.express as px
import streamlit as st
import numpy as np
import math

def app():
    with open('Proyectos/P03/form01.css') as f:
        css = f.read()

    # Añade tu CSS
    st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)
    
    st.title('Distribuciones para la Predicción de COVID19')
    
    st.markdown("## **Procedimiento Experimental**")
    # Sección del procedimiento del proyecto
    st.write("""
        En la presente práctica se llevó a cabo el análisis para realizar una predicción con los datos registrados por el Ministerio de Salud, de los casos de COVID-19 en el año 2020. A partir de ello se procedió de la siguiente manera
    """)
    
    expa0 = st.toggle("##### Datos de las constantes GNUPlot (Parte experimental)")
    if expa0:
        #fit.log → lin: 2750 → Wed Apr 10 14:54:58 2024
        st.write(
            '''
            1. Se definió la función de la Distribución Gaussiana, $$f(x)$$.
            2. Se indicaron los valores de las constantes como $$A$$=400, $$u$$=200 y $$r$$=100.
            3. Empleando el comando ``fit f(x) (...)`` se realizó la gráfica de la función con los datos de casos positivos.
            4. Se indicó el uso de 69 datos.
            5. A partir de las iteraciones se determinaron los valores de $$A$$, $$u$$ y $$r$$ que ajustan de mejor manera el fit.
            '''
        )
        
    expa1 = st.toggle("##### Gráfica de la distribución (parte experimental)")
    if expa1:
        st.write(
            '''
            1. Se definió, con el comando ``def``, la función de la Distribución Gaussiana, $$P_{G}(x)$$, con los valores de las constantes $$A$$, $$u$$ y $$r$$ previamente obtenidos.
            2. Se vectorizó la función de la Distribución Gaussiana con ``numpy.vetorize()``, para diferentes valores de $$x$$.
            3. Se definió un rango de 185 datos con ``numpy.arange``.
            4. Se definieron los parámetros de la gráfica y la curva del ajuste.
            5. Se gráfico el ajuste y el histograma con el comando ``streamlit.plotly_chart()``.
            '''
        )
####################################################################
##                    Gráfica de Plotly (Aire)                    ##
####################################################################
    # Definir fórmula del fit para el aire
    def fit(x):
        A=63.5733
        u=2.18871
        r=1.59884
        x = np.array(x, dtype=int)
        return A*math.exp(-((x-u)/r)**2/2)
    fit = np.vectorize(fit)

    # Datos aire
    data = pd.read_csv('Proyectos/P03/csv/muestra_radiacion.csv')
    df = pd.DataFrame(data)
    value_range = np.arange(-3,df['Aire'].max()+1)
    count = df['Aire'].value_counts().reindex(value_range, fill_value=0).reset_index()
    print(count)

    plot_fit = px.line(x=value_range, y=fit(value_range))
    plot_fit.update_traces(line_color='#B21914', line_width=2.5, line_shape='spline')
    plot_fit.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)','paper_bgcolor': 'rgba(0, 0, 0, 0)',})
    plot_fit.add_bar(x=count['Aire'], y=count['count'])
    
####################################################################
##                    Gráfica de Plotly (Cesio)                   ##
####################################################################
    # Definir fórmula del fit para el cesio
    def fit2(x):
        A=5.09287
        u=442.826
        r=19.5836
        x = np.array(x, dtype=int)
        return A*math.exp(-((x-u)/r)**2/2)
    fit2 = np.vectorize(fit2)

    # Datos cesio
    print(df['Cesio'].min())
    value_range2 = np.arange(df['Cesio'].min(),df['Cesio'].max()+1)
    count2 = df['Cesio'].value_counts().reindex(value_range2, fill_value=0).reset_index()
    print(count2)
    print(value_range2)

    plot_fit2 = px.line(x=value_range2, y=fit(value_range2))
    plot_fit2.update_traces(line_color='#B21914', line_width=2.5, line_shape='spline')
    plot_fit2.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)','paper_bgcolor': 'rgba(0, 0, 0, 0)',})
    plot_fit2.add_bar(x=count2['Cesio'], y=count2['count'])
    
####################################################################
##                      Apartado de Resultados                    ##
####################################################################
    st.markdown("## **Resultados**")
    # Sección de los resultados
    rlist = ['**Gráfica 01**', '**Gráfica 02**', '**Tabla 01**']
    rlist02 = ['Gráfica del Aire.', 'Gráfica Cesio.', 'Datos de las gráficas.']
    # Diccionario con los valores de rlist con el valor de cada valor de rlist02
    dic = {key: i for key, i in zip(rlist,rlist02)}
    # Imprime cada par en el markdown
    s = "\n".join([f'- {key}: {i}' for key, i in dic.items()])
    # for i in rlist:
    #     s += "- " + i + "\n"
    st.write(
        """
        En la presente sección se presentarán los resultados obtenidos en la presente práctica, de los cuales están divididos en:
        """
    )
    st.markdown(s)
    
    c1, c2 = st.columns([1,4])
    with c1:
        resultados = st.radio(
            "**Resultados**", 
            ["Gráfica 01", "Gráfica 02", "Tabla 01"]
        )
        
    with c2:
        if resultados == "Gráfica 01":
            st.markdown("## Gráfica del decaimiento radiactivo del Aire")
            
            # c3, c4 = st.columns([6,1.5])
            # with c3:
            # Mostrar gráfica de plotly
            st.plotly_chart(plot_fit)
                
        if resultados == "Gráfica 02":
            st.markdown("## Gráfica del decaimiento radiactivo del Cesio-137")
            
            # c3, c4 = st.columns([6,1.5])
            # with c3:
            st.plotly_chart(plot_fit2)
            
        if resultados == "Tabla 01":
            st.markdown("## Datos de las gráficas")
            # l = np.arange(368)
            # table = pd.DataFrame({'Fechas': df['fecha'], 'Resultados Positivos': df['resultados']})
            st.table(data)
            
    
    st.markdown("## **Discusión de Resultados**")
    # Sección de los resultados
    st.write(
        """
        A partir de los datos dados por el Ministerio de Salud, de los casos positivos desde el 13 de marzo del 2020 hasta el 15 de marzo del 2021 (véase apartado ***Tabla 01***), se procede a realizar en las gráficas el histograma presentado en la ***Gráfica 01*** y ***Gráfica 02***. Del mismo modo se realizó una curva de ajuste empleando para ello la distribución gaussiana, con respecto a cierta cantidad de datos del histograma, para predecir un posible pico de contagios de COVID-19; esto es, considerando que se está en el día 69 y 80, después del primer caso, presentados en la ***Gráfica 01*** y ***Gráfica 02***, respectivamente.
        \n
        De los fits realizados en ``GNUPlot`` se consideró utilizar el del día 69, después del primer caso de contagio registrado, presentados en los apartados ***Gráfica 01*** y ***Fit 11 GNUPlot***, del apédice. Esto se debe a que en otros días los valores aumentaban o disminuian de manera drástica, como en el caso que se presenta en el ***Fit 13 GNUPlot*** (véase apéndice), donde el valor de $$A$$ cambiaba de 930,848 $$\pm$$ 3038 a 73351,4 $$\pm$$ 1,105e+06. Además, a partir del día 71 los datos tendían a decrecer, y con ello al realizar el ajuste tomando de ese día en adelante hacía que el fit proyectara que el valor máximo ya había sucedido y decreciera en vez de predecir un pico.
        
        De igual manera existían datos anteriores que también lograban realizar una proyección de un pico coherente a futuro, pero el utilizar estos ocasionaba que se desecharan
        un gran número de datos y por lo mismo su predicción podría ser menos fiable. Pero, como se mencionó anteriormente, también existían datos que ocasionaban que el ajuste
        se disparara a cantidades exageradas, debido a que eran días en donde los datos aumentaban o disminuían de manera drástica, obteniendo de esta manera una proyección que
        parecía improbable y por ende fue desechada.
        """
    )
