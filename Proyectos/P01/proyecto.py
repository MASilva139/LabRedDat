import numpy as np
import pandas as pd
import plotly.express as px
from scipy import stats
from scipy.optimize import curve_fit
import streamlit as st
import matplotlib.pyplot as plt
import math
from scipy.special import comb

def app():
    st.title('Distribución Binomial en lanzamiento de monedas')
    
    st.markdown("## **Procedimiento Experimental**")
    # Sección del procedimiento del proyecto
    st.write("""En la presente práctica se llevó a cabo el lanzamiento de diez monedas para cada repetición, siendo un total de cien repeticiones, de las cuales en cada una de estas se contaban el número de fichas que caían cara. En caso de que alguna de las fichas fuese interrumpida por alguna circunstancia, se procedia a repetir el tiro de dicha moneda para completar el conteo de caras. A partir de ello se procedió de la siguiente manera""")
    expa1 = st.toggle("##### Datos de la distribución (parte experimental)")
    if expa1:
        st.write(
            '''
            1. Se lanzaron 10 monedas.
            2. Se anotaron la cantidad de caras obtenidas entre las 10 monedas lanzadas.
            3. Se repitieron los pasos (1) y (2) un total de 100 veces.
            '''
        )
    expa2 = st.toggle("##### Distribución binomial (gráficas de los datos)")
    if expa2:
        st.write(
            '''
            1. Se definió la función del binomio a partir del comando ``def`` (de igual forma se utlizó la función incluida dentro de ``scipy``, ``stats.binom()``).
            2. Se configuró un ``st.slider()``.
            3. Se creó una tabla con ``pandas`` para los datos de  los tiros.
            4. Se programó el conteo de caras dentro de la lista de datos obtenida en la parte experimental.
            5. Se definieron los parámetros para la gráfica con el comando ``curve_fit`` de ``scipy.optimize``.
            6. Se generó la gráfica utilizando la librería de ``Plotly.Express`` dentro de la variable ``binomial``.
            '''
        )
    expa3 = st.toggle("##### Ajuste de la Distribución binomial (Fit de los datos obtenidos)")
    if expa3:
        st.write(
            '''
            1. Se convirtió a una tabla ``numpy`` la tabla de ``pandas`` que contiene los datos de los tiros.
            2. Se definieron los parámetros para el ajuste de la gráfica (fit) con el comando ``curve_fit`` de ``scipy.optimize``.
            3. Se generó la gráfica utilizando la librería de ``Plotly.Express`` dentro de la variable ``binomial``.
            4. Se gráfico el arreglo, junto con el histograma, en streamlit con el comando ``streamlit.plotly_chart()``.
            '''
        )
    
    st.markdown("## **Resultados**")
    # Sección de los resultados
    rlist = ['**Gráfica 01**', '**Gráfica 02**', '**Tabla 01**']
    rlist02 = ['Gráfica de los valores propios, utilizando Plotly.', 'Gráfica de los datos de todos los grupos del laboratorio.', 'Datos experimentales de todos los grupos.']
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
        if resultados != 'Tabla 01':
            # Slider de los valores de m
            number = st.slider('Seleccione número de datos', min_value=0, max_value=100, step=1, value=50)
            
            # Función para el fit dada por scipy
            def fit_func(x, n, p):
                return stats.binom(x, n, p)

            # Función propia para el fit
            def fit_function(x,n,p):
            # Todo lo que este aqui adentro es parte de lo que se ejecuta en la funcion
                n = int(n)
                x = np.array(x, dtype=int)
                combi = comb(n,x)
                px = p**x
                qnx = (1-p)**(n-x)
                return combi*px*qnx
            
            # Crear pandas con los datos de los tiros
            data = pd.read_csv('Proyectos/P01/Binomial-fichas.csv')
            df = pd.DataFrame(data)
            # Arange con los valores del 0 al 10
            value_range = np.arange(11)
            # Conteo de los valores de caras
            group = df['GM'].iloc[:number].value_counts().reindex(value_range, fill_value=0).reset_index()
            # Convertir serie a numpy
            group_2 = pd.Series.to_numpy(df['GM'].iloc[:number].value_counts().reindex(value_range, fill_value=0))
            # Fit (Gráfica propia)
            p0=[10,1/2]
            res, cov = curve_fit(fit_function, value_range, group_2, p0=p0, bounds=[(0,0), (np.inf,1)])

            # Gráfica en plotly (Propia)
            binomial = px.line(x=value_range, y=fit_function(value_range, *res)*(number), line_shape='spline')
            binomial.update_traces(line_color='#721422', line_width=2.5)
            binomial.add_bar(x=group['GM'], y=group['count'], marker_color='#6C6960', name='binomial')
            
            if resultados == "Gráfica 01":
                st.markdown("##### Valores de $$n$$ y $$p$$")
                tdp = pd.DataFrame({'n': [res[0]], 'p': [res[1]]})
                tdpr =tdp.round(10).astype(str)
                st.table(tdpr)
                med = res[0]*res[1]
                desv = math.sqrt(res[0]*res[1]*(1-res[1]))
                tmd = pd.DataFrame({'μ': [med], 'σ': [desv]})
                tmdr = tmd.round(9).astype(str)
                
                mexp = np.sum(group_2*value_range)/number
                dexp = math.sqrt(np.sum(group_2*(((value_range)-mexp)**2))/(number-1))
                tmdexp = pd.DataFrame({'$$μ_{exp}$$': [mexp], '$$σ_{exp}$$': [dexp]})
                tmdre = tmdexp.round(9).astype(str)
                
                st.markdown("##### Valores de $$\mu$$ y $$\sigma$$")
                st.table(tmdr)
                st.table(tmdre)
            
            # Gráfica y fit de los datos de toda la clase
            data_class = pd.Series(df.iloc[:number].squeeze().values.ravel()).value_counts().sort_index()
            data_class = data_class.reindex(value_range, fill_value=0)
            group_class = data_class.to_numpy()
            todos = data_class.reset_index()
            # group_class = pd.Series.to_numpy(data_class['count'], dtype=int)
            # Fit
            p0=[10,1/2]
            res_2, cov_2 = curve_fit(fit_function, value_range, data_class, p0=p0, bounds=[(0,0), (np.inf,1)])
            binomial_todos = px.line(x=value_range, y=fit_function(value_range, *res_2)*(number*6), line_shape='spline')
            binomial_todos.update_traces(line_color='#721422', line_width=2.5)
            binomial_todos.add_bar(x=todos['index'], y=todos['count'], marker_color='#6C6960', name='binomial')
            
            if resultados == "Gráfica 02":
                st.markdown("##### Valores de $$n$$ y $$p$$")
                tdp = pd.DataFrame({'n': [res_2[0]], 'p': [res_2[1]]})
                tdpr =tdp.round(10).astype(str)
                st.table(tdpr)
                med = res_2[0]*res_2[1]
                desv = math.sqrt(res_2[0]*res_2[1]*(1-res_2[1]))
                tmd = pd.DataFrame({'μ': [med], 'σ': [desv]})
                tmdr = tmd.round(9).astype(str)
                
                media_2 = np.sum(group_class*value_range)/(number*6)
                desv_2 = math.sqrt(np.sum(group_class*(((value_range)-media_2)**2))/((number*6)-1))
                tmdexp2 = pd.DataFrame({'$$μ_{exp}$$': [media_2], '$$σ_{exp}$$': [desv_2]})
                tmdre2 = tmdexp2.round(9).astype(str)
                
                st.markdown("##### Valores de $$\mu$$ y $$\sigma$$")
                st.table(tmdr)
                st.table(tmdre2)
            
        with c2:
            if resultados == "Gráfica 01":
                st.markdown("## Gráfica Propia (Plotly)")
                c3, c4 = st.columns([6,1.5])
                with c3:
                    # Mostrar gráfica de plotly
                    st.plotly_chart(binomial)
                    
                with c4:
                    # Función para cambiar el color de las celdas
                    def Ccol(val):
                        color = '#000'
                        return f'background-color: {color}'
                    def color_celda(val):
                        if val >= 0 and val < 5:
                            color = '#705335' 
                        elif val >= 5 and val < 10:
                            color='#587246'
                        elif val >= 10 and val < 15:
                            color='#606E8C'
                        elif val >= 15 and val < 20:
                            color='#2C5545'
                        elif val >= 20 :
                            color='#5E2129'
                        return f'background-color: {color}'

                    # Aplicar la función a las celdas del DataFrame
                    fgroup = group.style.applymap(Ccol, subset=['GM']).applymap(color_celda, subset=['count'])
                    st.table(fgroup)
                
            if resultados == "Gráfica 02":
                st.markdown("## Gráfica de todos los datos (Plotly)")
                
                c5, c6 = st.columns([6,1.5])
                with c5:
                    st.plotly_chart(binomial_todos)
                with c6:
                    # Función para cambiar el color de las celdas
                    def Ccol1(val):
                        color1 = '#000'
                        return f'background-color: {color1}'
                    def color_celda1(val):
                        if val >= 0 and val < 20:
                            color1 = '#705335' 
                        elif val >= 20 and val < 40:
                            color1='#587246'
                        elif val >= 40 and val < 60:
                            color1='#606E8C'
                        elif val >= 60 and val < 80:
                            color1='#2C5545'
                        elif val >= 80 and val < 100 :
                            color1='#5E2129'
                        elif val >= 100 and val < 120 :
                            color1='#0A1A00'
                        elif val >= 120  :
                            color1='#0000A0'
                        return f'background-color: {color1}'

                    # Aplicar la función a las celdas del DataFrame
                    ftodos = todos.style.applymap(Ccol1, subset=['index']).applymap(color_celda1, subset=['count'])
                    st.table(ftodos)
    
    
    with c2:        
        if resultados == "Tabla 01":
            data = pd.read_csv('Proyectos/P01/Binomial-fichas.csv')
            st.markdown("## Tabla de datos originales")
            st.table(data)

    st.markdown("## **Discusión de Resultados**")
    # Sección de los resultados
    st.write(
        """
        A partir de los datos obtenidos, presentados en la columna **GM**, en la tabla de datos originales (véase apartado ***Tabla 01***) se procede a determinar el histograma presentado en el apartado ***Gráfica 01***, la cual va presentando con respecto al valor presentado en el slider el conteo de caras obtenidos dicha repetición. Dichos datos pueden verse representados en la tabla que se encuentra a la par de la gráfica. De igual manera, se tiene una gràfica que presenta los datos de todos los grupos que realizaron la práctica (véase el apartado ***Gráfica 02***).
        
        Cabe a resaltar que tanto la gráfica generada a partir de la función ``stats.binom()``, como la función ``def``, dan el mismo resultado; es decir, generan la misma gráfica de barras y de ajuste, por lo que se optó solamente a utiizar una de estas funciones para realizar los fits. De igual manera, por comodidad y sobre todo por estética, se prefirio utilizar la gráfica generada por la librería de ``Plotly.Express``, dado que no solamente presenta la gráfica de la función de ajuste con una curva suave, sino que también permite observar, por medio de un zoom, de mejor manera la función de ajuste.
        
        A partir del valor de $$p$$ presentado en la tabla **Valores de $$n$$ y $$p$$**, de la **Gráfica 01**,  se tiene que $$p=0,5723 [\dots]$$ cuando $$m=19$$, mostrando una alta desviación con respecto al valor teórico $$p=0,50$$, siendo este valor el que mayor desviación presenta, dado que posteriormente se llega a normalizar; mientras que para los primeros tres valores $$m=1, 2, 3$$, se tiene que $p=0,5$. Por lo tanto, con lo previamente mencionado se puede concluir que la curva de ajuste realizada (``def``) presenta una buena aproximación, con respecto al modelo original.
        
        Sin embargo, en el apartado **Gráfica 02**, se tiene que el mayor valor que $$p$$ tiene es de $$0,521678$$ para un $$m=5$$, pero a cambio de ello se puede observar que para la mayoría de los valores de $$m$$ se tiene que el valor de $$p$$ oscila entre $$0,47<p<0,5002$$.
        """
    )