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
            dfin01 = pd.DataFrame({'month':dfd['month'], 'mrevenue':dfd['mrevenue'], 'revenue':dfd['revenue'], 'lrev':dfd['lrev']})
            dfin01.to_csv('Parcial/Final/csv/App Revenue/AppRev001.csv', sep=";", index=True)
            
            plfit = px.scatter(x=dfd.index, y=dfd['lrev'])
            plfit.update_traces(line_color='#B21914', line_width=2.5)
            plfit.update_layout({'plot_bgcolor':'rgba(0,0,0,0)','paper_bgcolor':'rgba(0,0,0,0)'})
            st.plotly_chart(plfit)
            
            st.table(dfin01)
            
            cov1_01 = np.cov(dfin01.index, dfin01['revenue'])
            cs1_01 = sp(dfin01.index, dfin01['revenue'])
            cp1_01 = prs(dfin01.index, dfin01['revenue'])
            cov1_02 = np.cov(dfin01.index, dfin01['lrev'])
            cs1_02 = sp(dfin01.index, dfin01['lrev'])
            cp1_02 = prs(dfin01.index, dfin01['lrev'])
            coef01 = pd.DataFrame({'Covarianza (N)': [cov1_01,0], 'Coef.Spearman (N)': cs1_01, 'Coef.Pearson (N)': cp1_01, 'Covarianza (log)': [cov1_02,0], 'Coef.Spearman (log)': cs1_02, 'Coef.Pearson (log)': cp1_02})
            st.table(coef01)
            
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
            
            cov2_01 = np.cov(dfin02.index, dfin02['GenRevGT'])
            cs2_01 = sp(dfin02.index, dfin02['GenRevGT'])
            cp2_01 = prs(dfin02.index, dfin02['GenRevGT'])
            cov2_02 = np.cov(dfin02.index, dfin02['LGenRevGT'])
            cs2_02 = sp(dfin02.index, dfin02['LGenRevGT'])
            cp2_02 = prs(dfin02.index, dfin02['LGenRevGT'])
            coef02 = pd.DataFrame({'Covarianza (N)': [cov2_01,0], 'Coef.Spearman (N)': cs2_01, 'Coef.Pearson (N)': cp2_01, 'Covarianza (log)': [cov2_02,0], 'Coef.Spearman (log)': cs2_02, 'Coef.Pearson (log)': cp2_02})
            st.table(coef02)
            
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
            
            cov3_01 = np.cov(dfin03.index, dfin03['revenue'])
            cs3_01 = sp(dfin03.index, dfin03['revenue'])
            cp3_01 = prs(dfin03.index, dfin03['revenue'])
            cov3_02 = np.cov(dfin03.index, dfin03['lrev'])
            cs3_02 = sp(dfin03.index, dfin03['lrev'])
            cp3_02 = prs(dfin03.index, dfin03['lrev'])
            coef03 = pd.DataFrame({'Covarianza (N)': [cov3_01,0], 'Coef.Spearman (N)': cs3_01, 'Coef.Pearson (N)': cp3_01, 'Covarianza (log)': [cov3_02,0], 'Coef.Spearman (log)': cs3_02, 'Coef.Pearson (log)': cp3_02})
            st.table(coef03)