import numpy as np
import pandas as pd
import plotly.express as px
from scipy import stats
from scipy.optimize import curve_fit
from scipy.special import comb
import streamlit as st
import matplotlib.pyplot as plt
import math

def app():
    def fit_function(x, n, p):
        n = int(n)
        x = np.array(x, dtype=int)
        combi = comb(n,x)
        px = p**x
        qnx = (1-p)**(n-x)
        return combi*px*qnx

    data = pd.read_csv('Proyectos/P01/Binomial-fichas.csv')
    print(data)
    df = pd.DataFrame(data)
    value_range = range(0, 11)
    group = df['GM'].value_counts().reindex(value_range, fill_value=0)
    group_2 = pd.Series.to_numpy(group)
    binomial = px.bar(group)
    st.plotly_chart(binomial)

    p0= [10, 1/2]
    res, cov = curve_fit(fit_function, np.array(value_range), group_2, p0=p0)
    print(res)
    print(cov)

    fig, ax = plt.subplots()
    ax.bar(value_range, group)
    ax.plot(value_range, fit_function(value_range, *res)*105, color="Black")

    st.pyplot(fig)