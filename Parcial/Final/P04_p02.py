import pandas as pd
from scipy.stats import spearmanr as sp
from scipy.stats import pearsonr as prs
from scipy.stats import chisquare as chi
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
def fitg(x):
    A = 18.5557
    u = 17.9711
    r = 76.2984
    x = np.array(x, dtype=int)
    return A*math.exp(-((x-u)/r)**2/2)
fitg = np.vectorize(fitg)

def fitl(x):
    A = 0.12825
    u = 1.35399
    r = 9.58845e-31
    x = np.array(x, dtype=int)
    return A*mpm.log(((x+u)/r)**2/2)
fitl = np.vectorize(fitl)

def fit3(x):
    A = 5.07324e-05
    B = -0.00446483
    C = 0.0999895
    D = 17.9175
    x = np.array(x, dtype=int)
    return A*x**3+B*x**2+C*x+D
fit3 = np.vectorize(fit3)

data01 = pd.read_csv('Parcial/Final/csv/App Revenue/AppRev001.csv', sep=";")
dfd = pd.DataFrame(data01)
#print(count)
data02 = pd.read_csv('Parcial/Final/csv/Gatcha Revenue/Gatcha Revenue.csv', sep=";")
dfd2 = pd.DataFrame(data02)

data03 = pd.read_csv('Parcial/Final/csv/Genshin Banner/Genshin Revenue Banner.csv', sep=";")
dfd3 = pd.DataFrame(data03)

################################################################################################################################
###########################                            Parte Escrita                                 ###########################
################################################################################################################################
def app():
    with open('Proyectos/P04/form01.css') as f:
        css = f.read()

    # Añade tu CSS
    st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)
    
    st.title('Final')
    
####################################################################
##                      Apartado de Resultados                    ##
####################################################################
    st.markdown("## **Resultados**")
    
    c1, c2 = st.columns([1,6])
    with c1:
        resultados = st.radio(
            "**Resultados**", 
            ["Gráfica 01", "Gráfica 02", "Gráfica 03", "Tabla 01", "Tabla 02"]
        )
        
    with c2:
        if resultados == "Gráfica 01":
            st.markdown('## Genshin Month Revenue')
            pfit = px.scatter(x=dfd.index, y=dfd['revenue'],log_y=False)
            pfit.update_traces(line_color='#B21914', line_width=2.5)
            pfit.update_layout({'plot_bgcolor':'rgba(0,0,0,0)','paper_bgcolor':'rgba(0,0,0,0)'})
            st.plotly_chart(pfit)
            
            dfd['lrev'] = dfd['revenue'].apply(lambda x: float(mpm.ln(x)))
            dfin01 = pd.DataFrame({'month':dfd['month'], 'mrevenue':dfd['mrevenue'], 'revenue':dfd['revenue'], 'lref':dfd['lrev']})
            dfin01.to_csv('Parcial/Final/csv/App Revenue/AppRev001.csv', sep=";", index=True)
            
            plfit = px.scatter(x=dfd.index, y=dfd['lrev'])
            plfit.update_traces(line_color='#B21914', line_width=2.5)
            plfit.update_layout({'plot_bgcolor':'rgba(0,0,0,0)','paper_bgcolor':'rgba(0,0,0,0)'})
            st.plotly_chart(plfit)
            
            st.table(dfin01)
            
        if resultados == "Gráfica 02":
            st.markdown('## Genshin Month Revenue 02')
            pfit2 = px.scatter(x=dfd2.index, y=dfd2['GenRevGT'])
            
            pfit2.update_traces(line_color='#B21914', line_width=2.5)
            pfit2.update_layout({'plot_bgcolor':'rgba(0,0,0,0)','paper_bgcolor':'rgba(0,0,0,0)'})
            st.plotly_chart(pfit2)
            
            dfd2['LGenRevGT'] = dfd2['GenRevGT'].apply(lambda x: float(mpm.ln(x)))
            dfin02 = pd.DataFrame({'month':dfd2['month'], 'GenRevJ':dfd2['GenRevJ'], 'GenRevG':dfd2['GenRevG'], 'GenRevGT':dfd2['GenRevGT'], 'LGenRevGT':dfd2['LGenRevGT'], 'HIRevJ':dfd2['HIRevJ'], 'HIRevG':dfd2['HIRevG'], 'HIRevGT':dfd2['HIRevGT'], 'HSRRevJ':dfd2['HSRRevJ'], 'HSRRevG':dfd2['HSRRevG'], 'HSRRevGT':dfd2['HSRRevGT'], 'PGRRevJ':dfd2['PGRRevJ'], 'PGRRevG':dfd2['PGRRevG'], 'PGRRevGT':dfd2['PGRRevGT']})
            dfin02.to_csv('Parcial/Final/csv/Gatcha Revenue/Gatcha Revenue.csv', sep=";", index=True)
            
            plfit2 = px.scatter(x=dfd2.index, y=dfd2['LGenRevGT'])
            plfit2.update_traces(line_color='#B21914', line_width=2.5)
            plfit2.update_layout({'plot_bgcolor':'rgba(0,0,0,0)','paper_bgcolor':'rgba(0,0,0,0)'})
            st.plotly_chart(plfit2)
            
            st.table(dfin02)
            
        if resultados == "Gráfica 03":
            st.markdown('## Genshin Banner Revenue iOS china (pc not included)')
            pfit3 = px.scatter(x=dfd3.index, y=dfd3['revenue'], log_x=False)
            
            pfit3.update_traces(line_color='#B21914', line_width=2.5)
            pfit3.update_layout({'plot_bgcolor':'rgba(0,0,0,0)','paper_bgcolor':'rgba(0,0,0,0)'})
            st.plotly_chart(pfit3)
            
            dfd3['lrev'] = dfd3['revenue'].apply(lambda x: float(mpm.ln(x)))
            dfin03 = pd.DataFrame({'version':dfd3['version'], 'bannerfase':dfd3['bannerfase'], 'indate':dfd3['indate'], 'enddate':dfd3['enddate'], 'revenue':dfd3['revenue'], 'lrev':dfd3['lrev'], 'ch01':dfd3['ch01'], 'ch02':dfd3['ch02']})
            dfin03.to_csv('Parcial/Final/csv/Genshin Banner/Genshin Revenue Banner.csv', sep=";", index=True)
            
            plfit3 = px.scatter(x=dfd3.index, y=dfd3['lrev'])
            plfit3.update_traces(line_color='#B21914', line_width=2.5)
            plfit3.update_layout({'plot_bgcolor':'rgba(0,0,0,0)','paper_bgcolor':'rgba(0,0,0,0)'})
            st.plotly_chart(plfit3)
            
            st.table(dfin03)
                