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
data = pd.read_csv('Parcial/Final02/csv/fusion_experiment.csv')
df = pd.DataFrame(data)
df_lim = df.head(200)


################################################################################################################################
###########################                            Parte Escrita                                 ###########################
################################################################################################################################
def app():
    with open('Proyectos/P04/form01.css') as f:
        css = f.read()

    # Añade tu CSS
    st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)
    
    st.title('Decaimiento de Cesio-137')
    
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
            st.markdown("## Index - Magnetic Field Fluctuations")
            def fit(x):
                A = 0.001
                x = np.array(x, dtype=int)
                return A*x
            fit = np.vectorize(fit)
            
            value_range = np.arange(201)
    
            plot_fit = px.scatter(x=df.index, y=df["Magnetic Field Fluctuations"], range_x=(0,100))
            
            plot_fit.update_traces(line_color='#B21914', line_width=2.5)
            plot_fit.update_layout({'plot_bgcolor':'rgba(0,0,0,0)','paper_bgcolor':'rgba(0,0,0,0)'})
            
            st.plotly_chart(plot_fit)
                
            st.markdown("## Index - Target Density")
            plot_fit2 = px.scatter(x=df.index, y=df["Target Density"], range_x=(0,100))
            plot_fit2.update_traces(line_color='#B21914', line_width=2.5)
            plot_fit2.update_layout({'plot_bgcolor':'rgba(0,0,0,0)','paper_bgcolor':'rgba(0,0,0,0)'})
            st.plotly_chart(plot_fit2)
            
            st.markdown("## Index - Energy Input")
            plot_fit3 = px.scatter(x=df.index, y=df["Energy Input"], range_x=(0,100))
            plot_fit3.update_traces(line_color='#B21914', line_width=2.5)
            plot_fit3.update_layout({'plot_bgcolor':'rgba(0,0,0,0)','paper_bgcolor':'rgba(0,0,0,0)'})
            st.plotly_chart(plot_fit3)
            
            st.markdown("## Energy Input - Target Density")
            plot_fit4 = px.scatter(x=df_lim['Energy Input'], y=df_lim["Target Density"])
            plot_fit4.update_traces(line_color='#B21914', line_width=2.5)
            plot_fit4.update_layout({'plot_bgcolor':'rgba(0,0,0,0)','paper_bgcolor':'rgba(0,0,0,0)'})
            st.plotly_chart(plot_fit4)
            
            st.markdown("## Index - Injection Energy")
            plot_fit5 = px.scatter(x=df.index, y=df["Injection Energy"], range_x=(0,100))
            plot_fit5.update_traces(line_color='#B21914', line_width=2.5)
            plot_fit5.update_layout({'plot_bgcolor':'rgba(0,0,0,0)','paper_bgcolor':'rgba(0,0,0,0)'})
            st.plotly_chart(plot_fit5)
            
            st.markdown("## Index - Beam Symmetry")
            plot_fit6 = px.scatter(x=df.index, y=df["Beam Symmetry"], range_x=(0,100))
            plot_fit6.update_traces(line_color='#B21914', line_width=2.5)
            plot_fit6.update_layout({'plot_bgcolor':'rgba(0,0,0,0)','paper_bgcolor':'rgba(0,0,0,0)'})
            st.plotly_chart(plot_fit6)
            
            st.markdown("## Injection Energy - Beam Symmetry")
            plot_fit4 = px.scatter(x=df_lim['Beam Symmetry'], y=df_lim["Injection Energy"], log_x=False, log_y=False)
            plot_fit4.update_traces(line_color='#B21914', line_width=2.5)
            plot_fit4.update_layout({'plot_bgcolor':'rgba(0,0,0,0)','paper_bgcolor':'rgba(0,0,0,0)'})
            st.plotly_chart(plot_fit4)
            
            st.markdown("## Leakage - Plasma Instabilities")
            plot_fit5 = px.scatter(x=df_lim['Leakage'], y=df_lim["Plasma Instabilities"], log_x=False, log_y=False)
            plot_fit5.update_traces(line_color='#B21914', line_width=2.5)
            plot_fit5.update_layout({'plot_bgcolor':'rgba(0,0,0,0)','paper_bgcolor':'rgba(0,0,0,0)'})
            st.plotly_chart(plot_fit5)
            
            st.markdown("## Leakage - Neutron Yield")
            plot_fit6 = px.scatter(y=df_lim['Leakage'], x=df_lim["Neutron Yield"], log_x=False, log_y=False)
            plot_fit6.update_traces(line_color='#B21914', line_width=2.5)
            plot_fit6.update_layout({'plot_bgcolor':'rgba(0,0,0,0)','paper_bgcolor':'rgba(0,0,0,0)'})
            st.plotly_chart(plot_fit6)
            
                
        if resultados == "Tabla 01":
            st.markdown("### Datos de las gráficas")
            st.markdown(df_lim.to_markdown())
            