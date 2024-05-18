import pandas as pd
import plotly.express as px
import streamlit as st
import numpy as np
import math
import mpmath as mpm
from PIL import Image as im
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

#------------Distribución Gaussiana
datgaussai = pd.DataFrame({'Aire':count['Aire'], 'hi(x)':count['count']})
datgaussai['Pg(x)'] = fit(datgaussai['Aire'])
datgaussai['[hi(x)-yi(x)]^2'] = (datgaussai['hi(x)']-datgaussai['Pg(x)'])**2
datgaussai['[yi(x)]^2'] = (datgaussai['Pg(x)'])**2
datgaussai['[hi(x)]^2'] = (datgaussai['hi(x)'])**2
datgaussai['χ^2 (1)'] = (datgaussai['[hi(x)-yi(x)]^2'])/((datgaussai['Pg(x)'])**2)
datgaussai['χ^2 (2)'] = (datgaussai['[hi(x)-yi(x)]^2'])/((datgaussai['hi(x)'])**2)
dgaussai =(datgaussai).round(10).astype(str)
achigauss01 = datgaussai['χ^2 (1)'].sum()
achigauss02 = datgaussai['χ^2 (2)'].sum()
# print('chi-square')
# print(achi01)

# Definir fórmula del fit (D. Poisson) para el aire
def poisson_ai(x):
    m = (df['Aire'].sum())/(df['Aire'].count())
    # x = np.array(x, dtype=int)
    P_x = ((m**x)*(mpm.exp(-m)))/(mpm.factorial(x))
    return float(P_x)
v_poisson_ai = np.vectorize(poisson_ai)
    
nd = df['Aire'].count()

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
achipoiss01 = datpossai['χ^2 (1)'].sum()
achipoiss02 = datpossai['χ^2 (2)'].sum()

air_poisson = pd.DataFrame({'Aire': dpoissonai['Aire'],'$$h_{i}(x)$$':dpoissonai['hi(x)'],'$$P_{P}(x)$$':dpoissonai['Pp(x)'],'$$[h_{i}(x)-y_{i}(x)]^2$$':dpoissonai['[hi(x)-yi(x)]^2'],'$$[y_{i}(x)]^2$$':dpoissonai['[yi(x)]^2'],'$$[h_{i}(x)]^2$$':dpoissonai['[hi(x)]^2'],'$$χ_{1}^{2}$$':dpoissonai['χ^2 (1)'],'$$χ_{2}^{2}$$':dpoissonai['χ^2 (2)']})
#print(dpoisson01)

poisson_fitai = px.line(x=value_range, y=(v_poisson_ai(value_range))*(nd))
poisson_fitai.update_traces(line_color='#B21914', line_width=2.5, line_shape='spline')
poisson_fitai.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)','paper_bgcolor': 'rgba(0, 0, 0, 0)',})
poisson_fitai.add_bar(x=count['Aire'], y=count['count'])
    
####################################################################
##                    Gráfica de Plotly (Cesio)                   ##
####################################################################
# Definir fórmula del fit (D. Gaussiana) para el cesio (1/1)
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
cschigauss01 = datgauss01['χ^2 (1)'].sum()
cschigauss02 = datgauss01['χ^2 (2)'].sum()

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
cschipoiss01 = datposs01['χ^2 (1)'].sum()
cschipoiss02 = datposs01['χ^2 (2)'].sum()

cs_poisson01 = pd.DataFrame({'Cesio': dpoisson01['Cesio'],'$$h_{i}(x)$$':dpoisson01['hi(x)'],'$$P_{P}(x)$$':dpoisson01['Pp(x)'],'$$[h_{i}(x)-y_{i}(x)]^2$$':dpoisson01['[hi(x)-yi(x)]^2'],'$$[y_{i}(x)]^2$$':dpoisson01['[yi(x)]^2'],'$$[h_{i}(x)]^2$$':dpoisson01['[hi(x)]^2'],'$$χ_{1}^{2}$$':dpoisson01['χ^2 (1)'],'$$χ_{2}^{2}$$':dpoisson01['χ^2 (2)']})
#print(dpoisson01)

poisson_fit1 = px.line(x=value_range2, y=(v_poisson_ce01(value_range2))*(nd01))
poisson_fit1.update_traces(line_color='#B21914', line_width=2.5, line_shape='spline')
poisson_fit1.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)','paper_bgcolor': 'rgba(0, 0, 0, 0)',})
poisson_fit1.add_bar(x=count2['Cesio'], y=count2['count'])

# Definir fórmula del fit (D. Gaussiana) para el cesio (5/5)
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
cs2chigauss01 = datgauss02['χ^2 (1)'].sum()
cs2chigauss02 = datgauss02['χ^2 (2)'].sum()

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
cs2chipoiss01 = datposs02['χ^2 (1)'].sum()
cs2chipoiss02 = datposs02['χ^2 (2)'].sum()

cs_poisson02 = pd.DataFrame({'Cesio': dpoisson02['Cesio'],'$$h_{i}(x)$$':dpoisson02['hi(x)'],'$$P_{P}(x)$$':dpoisson02['Pp(x)'],'$$[h_{i}(x)-y_{i}(x)]^2$$':dpoisson02['[hi(x)-yi(x)]^2'],'$$[y_{i}(x)]^2$$':dpoisson02['[yi(x)]^2'],'$$[h_{i}(x)]^2$$':dpoisson02['[hi(x)]^2'],'$$χ_{1}^{2}$$':dpoisson02['χ^2 (1)'],'$$χ_{2}^{2}$$':dpoisson02['χ^2 (2)']})

poisson_fit2 = px.line(x=group, y=(v_poisson_ce02(group))*(nd02))
poisson_fit2.update_traces(line_color='#B21914', line_width=2.5, line_shape='spline')
poisson_fit2.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)','paper_bgcolor': 'rgba(0, 0, 0, 0)',})
poisson_fit2.add_bar(x=group, y=dfd['count'])

#######################################
##        Tabla de chi-square        ##
#######################################
#________________________________________#
#             Datos originales           #
# ----------------- Aire -----------------
adgaussdict01 = (datgaussai.to_dict()).get("χ^2 (1)")
sumairgauss01 = sum(adgaussdict01[i] for i in range(26))/26
sum2airgauss01 = sum(adgaussdict01[i] for i in range(12))/12
adgaussdict02 = (datgaussai.to_dict()).get("χ^2 (2)")
sumairgauss02 = sum(adgaussdict02[i] for i in range(26))/26
sum2airgauss02 = sum(adgaussdict02[i] for i in range(12))/12
adpoissdict01 = (datpossai.to_dict()).get("χ^2 (1)")
sumairpoiss01 = sum(adpoissdict01[i] for i in range(26))/26
sum2airpoiss01 = sum(adpoissdict01[i] for i in range(12))/12
adpoissdict02 = (datpossai.to_dict()).get("χ^2 (2)")
sumairpoiss02 = sum(adpoissdict02[i] for i in range(26))/26
sum2airpoiss02 = sum(adpoissdict02[i] for i in range(12))/12
# ----------------- Cesio (1/1) -----------------
cs1dgaussdict01 = (datgauss01.to_dict()).get("χ^2 (1)")
sumcs1gauss01 = sum(cs1dgaussdict01[i] for i in range(len(cs1dgaussdict01)))/146
sum2cs1gauss01 = sum(cs1dgaussdict01[i] for i in range(41,len(cs1dgaussdict01)))/105
cs1dgaussdict02 = (datgauss01.to_dict()).get("χ^2 (2)")
sumcs1gauss02 = sum(cs1dgaussdict02[i] for i in range(len(cs1dgaussdict02)))/146
sum2cs1gauss02 = sum(cs1dgaussdict02[i] for i in range(41,len(cs1dgaussdict02)))/105
cs1dpoissdict01 = (datposs01.to_dict()).get("χ^2 (1)")
sumcs1poiss01 = sum(cs1dpoissdict01[i] for i in range(len(cs1dpoissdict01)))/146
sum2cs1poiss01 = sum(cs1dpoissdict01[i] for i in range(41,len(cs1dpoissdict01)))/105
cs1dpoissdict02 = (datposs01.to_dict()).get("χ^2 (2)")
sumcs1poiss02 = sum(cs1dpoissdict02[i] for i in range(len(cs1dpoissdict02)))/146
sum2cs1poiss02 = sum(cs1dpoissdict02[i] for i in range(41,len(cs1dpoissdict02)))/105
# ----------------- Cesio (5/5) -----------------
cs2dgaussdict01 = (datgauss02.to_dict()).get("χ^2 (1)")
sumcs2gauss01 = sum(cs2dgaussdict01[i] for i in range(len(cs2dgaussdict01)))/32
sum2cs2gauss01 = sum(cs2dgaussdict01[i] for i in range(8,len(cs2dgaussdict01)))/24
cs2dgaussdict02 = (datgauss02.to_dict()).get("χ^2 (2)")
sumcs2gauss02 = sum(cs2dgaussdict02[i] for i in range(len(cs2dgaussdict02)))/32
sum2cs2gauss02 = sum(cs2dgaussdict02[i] for i in range(8,len(cs2dgaussdict02)))/24
cs2dpoissdict01 = (datposs02.to_dict()).get("χ^2 (1)")
sumcs2poiss01 = sum(cs2dpoissdict01[i] for i in range(len(cs2dpoissdict01)))/32
sum2cs2poiss01 = sum(cs2dpoissdict01[i] for i in range(8,len(cs2dpoissdict01)))/24
cs2dpoissdict02 = (datposs02.to_dict()).get("χ^2 (2)")
sumcs2poiss02 = sum(cs2dpoissdict02[i] for i in range(len(cs2dpoissdict02)))/32
sum2cs2poiss02 = sum(cs2dpoissdict02[i] for i in range(8,len(cs2dpoissdict02)))/24

tchi = pd.DataFrame({
    '$$χ^2$$':['Gauss $$(1/[y_{i}(x)]^{2})$$', 'Gauss $$(1/[h_{i}(x)]^{2})$$', 'Poisson $$(1/[y_{i}(x)]^{2})$$', 'Poisson $$(1/[h_{i}(x)]^{2})$$'], 
    '$${χ^2}_{Aire}$$': [sumairgauss01, sumairgauss02, sumairpoiss01, sumairpoiss02],
    '$${χ^2}_{Cs-137}$$': [sumcs1gauss01, sumcs1gauss02, sumcs1poiss01, sumcs1poiss02],
    '$${χ^2}_{Cs-137}$$ (arr)': [sumcs2gauss01, sumcs2gauss02, sumcs2poiss01, sumcs2poiss02]
})
tchi02 = pd.DataFrame({
    '$$χ^2$$':['Gauss $$(1/[y_{i}(x)]^{2})$$', 'Gauss $$(1/[h_{i}(x)]^{2})$$', 'Poisson $$(1/[y_{i}(x)]^{2})$$', 'Poisson $$(1/[h_{i}(x)]^{2})$$'], 
    '$${χ^2}_{Aire}$$': [sum2airgauss01, sum2airgauss02, sum2airpoiss01, sum2airpoiss02],
    '$${χ^2}_{Cs-137}$$': [sum2cs1gauss01, sum2cs1gauss02, sum2cs1poiss01, sum2cs1poiss02],
    '$${χ^2}_{Cs-137}$$ (arr)': [sum2cs2gauss01, sum2cs2gauss02, sum2cs2poiss01, sum2cs2poiss02]
})

################################################################################################################################
###########################                            Parte Escrita                                 ###########################
################################################################################################################################
def app():
    with open('Proyectos/P04/form01.css') as f:
        css = f.read()

    # Añade tu CSS
    st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)
    
    st.title('Introducción al Machine Learning')
    
    st.markdown("## **Procedimiento Experimental**")
    # Sección del procedimiento del proyecto
    st.write("""
        En la presente práctica se llevó a cabo el análisis del proyecto que presentó el licenciado de machine learning de la siguiente manera
    """)
    
    expa0 = st.toggle("##### Machine learning")
    if expa0:
        #fit.log → lin: 2750 → Wed Apr 10 14:54:58 2024
        st.write(
            r'''
            1. Se definió la función de predicción de la etiqueta $$y$$, utilizando para ello el $$Score()$$, que depende del vector de peso $$\vec{W}$$ y el vector de característica $$\vec{\phi}(x)$$.
            2. Se definió la función $$loss_{hinge}()$$, que depende del $$Score()$$ y $$P_{\pi2}()$$.
            3. Se definió la función del descenso del gradiente, $$\nabla loss_{hinge}()$$.
            4. Se definió la función del cuadrado de la función loss, $$loss^{2}()$$.
            5. Se definió la función del descenso del gradiente del cuadrado de la función loss, $$\nabla loss^{2}()$$.
            6. Se definió la cantidad de dimensiones, $$dim$$.
            7. Se definió el vector de peso $$\vec{W}$$, que depende de la dimensión $$dim$$, con valores random.
            8. Se definió un total de 500 para el tamaño del training data set, $$tds_{len}$$.
            9. Se generó el diccionario del training data set, $$tds=[\hspace{3pt}]$$, a partir de un ciclo ```for```.
            10. Se generó una tabla con los valores del set de datos de entrenamiento (training data set).
            11. Se definió el número máximo de iteraciones a realizar.
            12. Se definió el origen del vector de peso.
            '''
        )

####################################################################
##                      Apartado de Resultados                    ##
####################################################################
    st.markdown("## **Resultados**")
    # Sección de los resultados
    rlist = ['**Test**', '**Trained**', '**Compare**']
    rlist02 = ['','','']
    # Diccionario con los valores de rlist con el valor de cada valor de rlist02
    dic = {key: i for key, i in zip(rlist,rlist02)}
    # Imprime cada par en el markdown
    s = "\n".join([f'- {key}: {i}' for key, i in dic.items()])
    # for i in rlist:
    #     s += "- " + i + "\n"
    # st.markdown(s)
    
    c1, c2 = st.columns([1,4])
    with c1:
        resultados = st.radio(
            "**Resultados**", 
            ["Test", "Trained", "Compare"]
        )
        
    with c2:
        if resultados == "Test":
            st.markdown("## Gráfica del test")
            img01 = im.open('Proyectos/P04/img/test.jpg')
            st.image(img01)
                
        if resultados == "Trained":
            st.markdown("## Gráfica del trained")
            img02 = im.open('Proyectos/P04/img/trained.jpg')
            st.image(img02)
            
        if resultados == "Compare":
            st.markdown("## Comparación")
            img03 = im.open('Proyectos/P04/img/compare.jpg')
            st.image(img03)
    
    st.markdown("## **Discusión de Resultados**")
    st.write(
        """
        A partir de los datos obtenidos del decaimiento radiactivo del aire y del Cesio-137, empleando un contador de particulas Geiger, se procedió a realizar en las gráficas los histogramas presentados en las secciones de resultados ***Gráfica 01***, ***Gráfica 02*** y ***Gráfica 03***, siendo estos las del aire, las del Cesio-137 y las del Cesio-137 con datos agrupados, respectivamente. Del mismo modo, se realizó una curva de ajuste empleando para ello las distribuciones de Gauss y de Poisson para verificar a cual de estas se ajustaba de mejor manera cada caso de decaimiento radactivo; además, se realizó la prueba de $$\chi^{2}$$ para cada uno de los casos.
        \n
        De los fits realizados en ```GNUPlot``` se determinaron los valores del ajuste de la curva de la distribución gaussiana, presentados en el apartado de resultados ***Gráfica 01***, ***Gráfica 02***, ***Gráfica 03*** en la sección de **Distribución Gaussiana**. De manera que se obtuvo un resultado de $$A$$=63.5733, $$u$$=2,18871 y $$r$$=1,59884 para el aire, $$A$$=5,09274, $$u$$=442,826 y $$r$$=19,5845 para el Cesio-137 y para los datos agrupados del Cesio-137 $$A$$=25,382, $$u$$=439,84 y $$r$$=19,6525. Estos valores pueden verse en el apartado de ***Ajuste (Fit)*** en la sección de **Anexos**. Con ello, en la sección de **Resultados**, en el apartado ***Gráfica 01*** se puede observar que el ajuste para el aire presentado por la distribución de Poisson tiene un mejor ajuste con respecto a los valores medidos; sin embargo, a pesar de que el ajuste dado por la distribución gaussiana no esta mal, se puede observar que dicho ajuste difiere en mayor medida respecto a los datos experimentales. 
        \n
        Cabe resaltar, que el ajuste que presenta la distribución de Poisson para el Cesio-137 tiende al infinito, esto se puede observar en los apartados ***Tablas Cs-137***, ***Tablas Cs-137 (2)***, ***T02.Cs-137*** y ***T02.Cs-137 (2)*** en la sección de **Anexos**; esto se debe a que los valores donde se presentan los datos (x) son demasiado grandes, de manera que debido a la definición matemática de la distribución de Poisson se tiene que la función tiende a infinito, en cada punto del ajuste. Sin embargo, la distribución gaussiasna presenta un mejor ajuste para los datos agrupados (véase apartado ***Gráfica 03***), que con los datos sin agrupar (véase apartado ***Gráfica 02***); esta diferencia se debe a que al agrupar los datos estos se ven menos dispersos, con ello el fit se ajusta de mejor manera a ellos, mientras que al no agruparlos hay muchos datos (bines) que comparten altura, por lo tanto, el ajuste presenta una mayor discrepancia con respecto a los datos experimentales. 
        \n
        De lo previamente mencionado, respecto a los ajustes realizados por las distribuciones de Gauss y de Poisson, a partir de la prueba de $$\chi^{2}$$ se confirmó que la distribución que presenta un mejor ajuste es la distrubución de Poisson, en el caso del aire, dado presenta una menor diferencia significativa entre la frecuencia esperada (obtenida a partir del fit) y la frecuencia observada (datos experimentales), véase *Tabla 01: Prueba de $$\chi^{2}$$* en el apartado ***Tabla 02*** en la sección de **Resultados**. Esto se debe a que el valor de $$\chi^{2}$$=4,1719e+25 para la distribución de Poisson, mientras que $$\chi^{2}$$=2,4149e+83 para la distribución gaussiana. Sin embargo, al no poderse realizar el ajuste del fit a partir de la distribución de Poisson en el Cesio-137, no se puede realizar la prueba del $$\chi^{2}$$ para la misma, por lo tanto, se tiene que la única distribución que cumple para la prueba del $$\chi^{2}$$ es la distribución gaussiana, que presenta un valor de $$\chi^{2}$$=931520.
        \n
        Se pudo observar que eliminando los datos que se alejaban mucho del rango usual de mediciones los cuales afectaban el valor de $$\chi^{2}$$, siendo estos el dato 25 del aire y 351 del Cesio-137; se tiene un mejor ajuste de las distribuciones con respecto a los datos experimentales, esto se puede ver en la *Tabla 02: Prueba de $$\chi^{2}$$ (datos acotados)* en el apartado ***Tabla 02*** en la sección de Resultados; donde $$\chi^{2}$$=275.362 para la distribución de Poisson, mientras que $$\chi^{2}$$=3.2001e+08 para la distribución gaussiana. Obviamente estos resultados no son coherentes con los datos experimentales, ya que se están omitiendo de manera intencional los datos que causaban discrepancia. Se puede visualizar en los apartados que tienen el término **(modificado)**, las gráficas y tablas con las consideraciones previamente mencionadas.
        """
    )