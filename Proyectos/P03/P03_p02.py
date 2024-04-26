import pandas as pd
import plotly.express as px
import streamlit as st
import numpy as np
import math
import mpmath as mpm
################################################################################################################################
###########################                            Parte práctica                                ###########################
################################################################################################################################

####################################################################
##                    Gráfica de Plotly (Aire)                    ##
####################################################################
# Definir fórmula del fit (D. Gaussiana) para el aire
def fit(x):
    A = 63.5733
    u = 2.18871
    r = 1.59884
    x = np.array(x, dtype=int)
    return A*math.exp(-((x-u)/r)**2/2)
fit = np.vectorize(fit)

# Datos aire
data = pd.read_csv('Proyectos/P03/csv/muestra_radiacion.csv')
df = pd.DataFrame(data)
value_range = np.arange(0,df['Aire'].max()+1)
count = df['Aire'].value_counts().reindex(value_range, fill_value=0).reset_index()
#print(count)

plot_fit = px.line(x=value_range, y=fit(value_range))
plot_fit.update_traces(line_color='#B21914', line_width=2.5, line_shape='spline')
plot_fit.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)','paper_bgcolor': 'rgba(0, 0, 0, 0)',})
plot_fit.add_bar(x=count['Aire'], y=count['count'])

# Definir fórmula del fit (D. Poisson) para el aire
def poisson_ai(x):
    m = (df['Aire'].sum())/(df['Aire'].count())
    # x = np.array(x, dtype=int)
    P_x = ((m**x)*(mpm.exp(-m)))/(mpm.factorial(x))
    return float(P_x)
v_poisson_ai = np.vectorize(poisson_ai)
    
nd = df['Aire'].count()
#------------Distribución Gaussiana
datgaussai = pd.DataFrame({'Aire':count['Aire'], 'hi(x)':count['count']})
datgaussai['Pg(x)'] = fit(datgaussai['Aire'])
datgaussai['[hi(x)-yi(x)]^2'] = (datgaussai['hi(x)']-datgaussai['Pg(x)'])**2
datgaussai['[yi(x)]^2'] = (datgaussai['Pg(x)'])**2
datgaussai['[hi(x)]^2'] = (datgaussai['hi(x)'])**2
datgaussai['χ^2 (1)'] = (datgaussai['[hi(x)-yi(x)]^2'])/((datgaussai['Pg(x)'])**2)
datgaussai['χ^2 (2)'] = (datgaussai['[hi(x)-yi(x)]^2'])/((datgaussai['hi(x)'])**2)
dgaussai =(datgaussai).round(10).astype(str)

air_gaussian = pd.DataFrame({'Aire': dgaussai['Aire'],'$$h_{i}(x)$$':dgaussai['hi(x)'],'$$P_{G}(x)$$':dgaussai['Pg(x)'],'$$[h_{i}(x)-y_{i}(x)]^2$$':dgaussai['[hi(x)-yi(x)]^2'],'$$[y_{i}(x)]^2$$':dgaussai['[yi(x)]^2'],'$$[h_{i}(x)]^2$$':dgaussai['[hi(x)]^2'],'$$χ_{1}^{2}$$':dgaussai['χ^2 (1)'],'$$χ_{2}^{2}$$':dgaussai['χ^2 (2)']})
#------------Poisson
datpossai = pd.DataFrame({'Aire':count['Aire'], 'hi(x)':count['count']})
datpossai['Pp(x)'] = (datpossai['Aire'].apply(v_poisson_ai))*(nd)
datpossai['[hi(x)-yi(x)]^2'] = (datpossai['hi(x)']-datpossai['Pp(x)'])**2
datpossai['[yi(x)]^2'] = (datpossai['Pp(x)'])**2
datpossai['[hi(x)]^2'] = (datpossai['hi(x)'])**2
datpossai['χ^2 (1)'] = (datpossai['[hi(x)-yi(x)]^2'])/((datpossai['Pp(x)'])**2)
datpossai['χ^2 (2)'] = (datpossai['[hi(x)-yi(x)]^2'])/((datpossai['hi(x)'])**2)
dpoissonai = (datpossai).round(10).astype(str)

air_poisson = pd.DataFrame({'Aire': dpoissonai['Aire'],'$$h_{i}(x)$$':dpoissonai['hi(x)'],'$$P_{P}(x)$$':dpoissonai['Pp(x)'],'$$[h_{i}(x)-y_{i}(x)]^2$$':dpoissonai['[hi(x)-yi(x)]^2'],'$$[y_{i}(x)]^2$$':dpoissonai['[yi(x)]^2'],'$$[h_{i}(x)]^2$$':dpoissonai['[hi(x)]^2'],'$$χ_{1}^{2}$$':dpoissonai['χ^2 (1)'],'$$χ_{2}^{2}$$':dpoissonai['χ^2 (2)']})
#print(dpoisson01)

poisson_fitai = px.line(x=value_range, y=(v_poisson_ai(value_range))*(nd))
poisson_fitai.update_traces(line_color='#B21914', line_width=2.5, line_shape='spline')
poisson_fitai.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)','paper_bgcolor': 'rgba(0, 0, 0, 0)',})
poisson_fitai.add_bar(x=count['Aire'], y=count['count'])
    
####################################################################
##                    Gráfica de Plotly (Cesio)                   ##
####################################################################
# Definir fórmula del fit (D. Gaussiana) para el cesio
def fit2(x):
    A = 5.09274
    u = 442.826
    r = 19.5845
    x = np.array(x, dtype=int)
    return A*math.exp(-((x-u)/r)**2/2)
fit2 = np.vectorize(fit2)

# Datos cesio
#print(df['Cesio'].min())
value_range2 = np.arange(df['Cesio'].min(),df['Cesio'].max()+1)
count2 = df['Cesio'].value_counts().reindex(value_range2, fill_value=0).reset_index()
#print(count2)
#print(value_range2)

plot_fit2 = px.line(x=value_range2, y=fit2(value_range2))
plot_fit2.update_traces(line_color='#B21914', line_width=2.5, line_shape='spline')
plot_fit2.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)','paper_bgcolor': 'rgba(0, 0, 0, 0)',})
plot_fit2.add_bar(x=count2['Cesio'], y=count2['count'])

# Definir fórmula del fit (D. Poisson) para el Cesio-137 (1/1)
def poisson_ce01(x):
    m = (df['Cesio'].sum())/(df['Cesio'].count())
    # x = np.array(x, dtype=int)
    P_x = ((m**x)*(mpm.exp(-m)))/(mpm.factorial(x))
    return float(P_x)
v_poisson_ce01 = np.vectorize(poisson_ce01)
    
nd01 = df['Cesio'].count()
#------------Distribución Gaussiana
datgauss01 = pd.DataFrame({'Cesio-137':count2['Cesio'], 'hi(x)':count2['count']})
datgauss01['Pg(x)'] = fit2(datgauss01['Cesio-137'])
datgauss01['[hi(x)-yi(x)]^2'] = (datgauss01['hi(x)']-datgauss01['Pg(x)'])**2
datgauss01['[yi(x)]^2'] = (datgauss01['Pg(x)'])**2
datgauss01['[hi(x)]^2'] = (datgauss01['hi(x)'])**2
datgauss01['χ^2 (1)'] = (datgauss01['[hi(x)-yi(x)]^2'])/((datgauss01['Pg(x)'])**2)
datgauss01['χ^2 (2)'] = (datgauss01['[hi(x)-yi(x)]^2'])/((datgauss01['hi(x)'])**2)
dgauss01 =(datgauss01).round(10).astype(str)

cs_gaussian01 = pd.DataFrame({'Cesio': dgauss01['Cesio-137'],'$$h_{i}(x)$$':dgauss01['hi(x)'],'$$P_{G}(x)$$':dgauss01['Pg(x)'],'$$[h_{i}(x)-y_{i}(x)]^2$$':dgauss01['[hi(x)-yi(x)]^2'],'$$[y_{i}(x)]^2$$':dgauss01['[yi(x)]^2'],'$$[h_{i}(x)]^2$$':dgauss01['[hi(x)]^2'],'$$χ_{1}^{2}$$':dgauss01['χ^2 (1)'],'$$χ_{2}^{2}$$':dgauss01['χ^2 (2)']})
#------------Poisson
datposs01 = pd.DataFrame({'Cesio':count2['Cesio'], 'hi(x)':count2['count']})
datposs01['Pp(x)'] = (datposs01['Cesio'].apply(v_poisson_ce01))*(nd01)
datposs01['[hi(x)-yi(x)]^2'] = (datposs01['hi(x)']-datposs01['Pp(x)'])**2
datposs01['[yi(x)]^2'] = (datposs01['Pp(x)'])**2
datposs01['[hi(x)]^2'] = (datposs01['hi(x)'])**2
datposs01['χ^2 (1)'] = (datposs01['[hi(x)-yi(x)]^2'])/((datposs01['Pp(x)'])**2)
datposs01['χ^2 (2)'] = (datposs01['[hi(x)-yi(x)]^2'])/((datposs01['hi(x)'])**2)
dpoisson01 = datposs01.round(10).astype(str)

cs_poisson01 = pd.DataFrame({'Cesio': dpoisson01['Cesio'],'$$h_{i}(x)$$':dpoisson01['hi(x)'],'$$P_{P}(x)$$':dpoisson01['Pp(x)'],'$$[h_{i}(x)-y_{i}(x)]^2$$':dpoisson01['[hi(x)-yi(x)]^2'],'$$[y_{i}(x)]^2$$':dpoisson01['[yi(x)]^2'],'$$[h_{i}(x)]^2$$':dpoisson01['[hi(x)]^2'],'$$χ_{1}^{2}$$':dpoisson01['χ^2 (1)'],'$$χ_{2}^{2}$$':dpoisson01['χ^2 (2)']})
#print(dpoisson01)

poisson_fit1 = px.line(x=value_range2, y=(v_poisson_ce01(value_range2))*(nd01))
poisson_fit1.update_traces(line_color='#B21914', line_width=2.5, line_shape='spline')
poisson_fit1.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)','paper_bgcolor': 'rgba(0, 0, 0, 0)',})
poisson_fit1.add_bar(x=count2['Cesio'], y=count2['count'])

#-----------------------------
def fit2_1(x):
    A = 25.382
    u = 439.84
    r = 19.6525
    x = np.array(x, dtype=int)
    return A*math.exp(-((x-u)/r)**2/2)
fit2_1 = np.vectorize(fit2_1)

group = np.arange(350, 505, 5)
cesio_cut = df.groupby(pd.cut(df['Cesio'], group))['Cesio'].count()
#print(cesio_cut)
data_c = pd.read_csv('Proyectos/P03/csv/Cesio01.csv')
dfd = pd.DataFrame(data_c)

plot_fit2_1 = px.line(x=group, y=fit2_1(group))
plot_fit2_1.update_traces(line_color='#B21914', line_width=2.5, line_shape='spline')
plot_fit2_1.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)','paper_bgcolor': 'rgba(0, 0, 0, 0)',})
plot_fit2_1.add_bar(x=group, y=dfd['count'])

# Definir fórmula del fit (D. Poisson) para el Cesio-137 (5/5)
def poisson_ce02(x):
    m = (dfd['Cesio'].sum())/(dfd['Cesio'].count())
    # x = np.array(x, dtype=int)
    P_x = ((m**x)*(mpm.exp(-m)))/(mpm.factorial(x))
    return float(P_x)
v_poisson_ce02 = np.vectorize(poisson_ce02)
    
nd02 = dfd['Cesio'].count()
#------------Distribución Gaussiana
datgauss02 = pd.DataFrame({'Cesio-137':dfd['Cesio'], 'hi(x)':dfd['count']})
datgauss02['Pg(x)'] = (fit2(datgauss02['Cesio-137']))
datgauss02['[hi(x)-yi(x)]^2'] = (datgauss02['hi(x)']-datgauss02['Pg(x)'])**2
datgauss02['[yi(x)]^2'] = (datgauss02['Pg(x)'])**2
datgauss02['[hi(x)]^2'] = (datgauss02['hi(x)'])**2
datgauss02['χ^2 (1)'] = (datgauss02['[hi(x)-yi(x)]^2'])/((datgauss02['Pg(x)'])**2)
datgauss02['χ^2 (2)'] = (datgauss02['[hi(x)-yi(x)]^2'])/((datgauss02['hi(x)'])**2)
dgauss02 =(datgauss02).round(10).astype(str)

cs_gaussian02 = pd.DataFrame({'Cesio': dgauss02['Cesio-137'],'$$h_{i}(x)$$':dgauss02['hi(x)'],'$$P_{G}(x)$$':dgauss02['Pg(x)'],'$$[h_{i}(x)-y_{i}(x)]^2$$':dgauss02['[hi(x)-yi(x)]^2'],'$$[y_{i}(x)]^2$$':dgauss02['[yi(x)]^2'],'$$[h_{i}(x)]^2$$':dgauss02['[hi(x)]^2'],'$$χ_{1}^{2}$$':dgauss02['χ^2 (1)'],'$$χ_{2}^{2}$$':dgauss02['χ^2 (2)']})
#------------Poisson
datposs02 = pd.DataFrame({'Cesio':dfd['Cesio'], 'hi(x)':dfd['count']})
datposs02['Pp(x)'] = (datposs02['Cesio'].apply(v_poisson_ce02))*(nd02)
datposs02['[hi(x)-yi(x)]^2'] = (datposs02['hi(x)']-datposs02['Pp(x)'])**2
datposs02['[yi(x)]^2'] = (datposs02['Pp(x)'])**2
datposs02['[hi(x)]^2'] = (datposs02['hi(x)'])**2
datposs02['χ^2 (1)'] = (datposs02['[hi(x)-yi(x)]^2'])/((datposs02['Pp(x)'])**2)
datposs02['χ^2 (2)'] = (datposs02['[hi(x)-yi(x)]^2'])/((datposs02['hi(x)'])**2)
dpoisson02 = datposs02.round(10).astype(str)

cs_poisson02 = pd.DataFrame({'Cesio': dpoisson02['Cesio'],'$$h_{i}(x)$$':dpoisson02['hi(x)'],'$$P_{P}(x)$$':dpoisson02['Pp(x)'],'$$[h_{i}(x)-y_{i}(x)]^2$$':dpoisson02['[hi(x)-yi(x)]^2'],'$$[y_{i}(x)]^2$$':dpoisson02['[yi(x)]^2'],'$$[h_{i}(x)]^2$$':dpoisson02['[hi(x)]^2'],'$$χ_{1}^{2}$$':dpoisson02['χ^2 (1)'],'$$χ_{2}^{2}$$':dpoisson02['χ^2 (2)']})

poisson_fit2 = px.line(x=group, y=(v_poisson_ce02(group))*(nd02))
poisson_fit2.update_traces(line_color='#B21914', line_width=2.5, line_shape='spline')
poisson_fit2.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)','paper_bgcolor': 'rgba(0, 0, 0, 0)',})
poisson_fit2.add_bar(x=group, y=dfd['count'])

################################################################################################################################
###########################                            Parte Escrita                                 ###########################
################################################################################################################################
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
##                      Apartado de Resultados                    ##
####################################################################
    st.markdown("## **Resultados**")
    # Sección de los resultados
    rlist = ['**Gráfica 01**', '**Gráfica 02**', '**Gráfica 03**', '**Tabla 01**', '**Tabla 02**']
    rlist02 = ['Distribución Gaussiana del Aire.', 'Distribución del Cesio-137.', 'Distribución del Cesio-137, datos agrupados de 5 en 5.', 'Datos de las gráficas, histograma y ajuste de las ditribuciones gaussianas y de Poisson.']
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
            ["Gráfica 01", "Gráfica 02", "Gráfica 03", "Tabla 01", "Tabla 02"]
        )
        
    with c2:
        if resultados == "Gráfica 01":
            st.markdown("## Distribución del decaimiento radiactivo del Aire")
            st.markdown("### Distribución Gaussiana")
            # c3, c4 = st.columns([6,1.5])
            # with c3:
            # Mostrar gráfica de plotly
            st.plotly_chart(plot_fit)
            
            st.markdown("### Distribución de Poisson")
            st.plotly_chart(poisson_fitai)
                
        if resultados == "Gráfica 02":
            st.markdown("## Distribución del decaimiento radiactivo del Cesio-137")
            
            st.markdown("### Distribución Gaussiana")
            # c3, c4 = st.columns([6,1.5])
            # with c3:
            st.plotly_chart(plot_fit2)
            
            st.markdown("### Distribución de Poisson")
            st.plotly_chart(poisson_fit1)
            
        if resultados == "Gráfica 03":
            st.markdown("## Distribución del decaimiento radiactivo del Cesio-137, datos agrupados de 5 en 5")
            
            st.markdown("### Distribución Gaussiana")
            # c3, c4 = st.columns([6,1.5])
            # with c3:
            st.plotly_chart(plot_fit2_1)
            
            st.markdown("### Distribución de Poisson")
            st.plotly_chart(poisson_fit2)
                
        if resultados == "Tabla 01":
            st.markdown("### Datos de las gráficas")
            datc = pd.DataFrame({'Aire':count['Aire'], "$$N_{Aire}$$":count['count'], "$$P_{G_{Aire}}$$":dgaussai['Pg(x)'],"$$P_{P_{Aire}}$$":dpoissonai['Pp(x)'], 'Cs':count2['Cesio'], '$$N_{Cs}$$':count2['count'], "$$P_{G_{Cs}}$$":dgauss01['Pg(x)'],'Cs (arr)':data_c['Cesio'], '$$N_{Cs} (arr)$$':data_c['count'],"$$P_{G_{Cs}} (arr)$$":dgauss02['Pg(x)']})
            st.markdown(datc.to_markdown())
                
    
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
