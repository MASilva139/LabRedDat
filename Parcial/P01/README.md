# Parcial 01: Parte Práctica

## *Graficadora de distribuciones binomiales*
**Instrucciones:** Realizar una página de Streamlit cuya función sea graficar una distribución binomial para algún n y p dados. Para realizarla deberán programar en Python una interfaz que solicite al usuario introducir los valores de n y p. Deben buscar documentación sobre los "input widgets" de Streamlit, elegir cual se adecua a esta aplicación y porgramar la interfaz en Streamlit, además deberán programar una función que realice el cálculo de la distribución y la grafique utilizando pyplot de matplotlib o plotly.express (pueden usar otro paquete si lo desean). Finalmente esta gráfica se debe de mostrar dentro de la página. Tomar en cuenta los posibles errores que un usuario podría cometer (como ingresar un valor de p mayor a 1) y realizar alguna implementación para evitar esos casos, además pueden limitar los posibles valores de n para que sean menores a 100 (para evitar casos con alta demanda computacional).

 Finalmente debe incluir un texto en la interfaz con una breve explicación sobre lo que se está realizando en su aplicación, además de una guía sobre como utilizarla. Además incluir un texto indicando por qué seleccionó ese tipo de widget para el desarrollo de su interfaz.

De incluirse valores por defecto en su interfaz, colocar los mismos que los utilizados en su examen teórico (n=1, p=1/2).

## *Evaluación*
* *Funcionalidad general de la aplicación*
* *Estructura y orden en el código*
* *Inclusión de comentarios en el código para la explicación del mismo*
* *Manejo de Git, GitHub y Deploy exitoso*

## Documentación
```
Librerías revisadas para el examen
├── Input widgets
│   └── https://docs.streamlit.io/library/api-reference/widgets
├── streamlit.number_input()
│   └── https://docs.streamlit.io/library/api-reference/widgets/st.number_input
├── streamlit.radio()
│   └── https://docs.streamlit.io/library/api-reference/widgets/st.radio
├── streamlit.selectbox()
│   └── https://docs.streamlit.io/library/api-reference/widgets/st.selectbox
├── streamlit.toggle()
│   └── https://docs.streamlit.io/library/api-reference/widgets/st.toggle
├── streamlit.slider()
│   └── https://docs.streamlit.io/library/api-reference/widgets/st.slider
├── streamlit.columns()
│   └── https://docs.streamlit.io/library/api-reference/layout/st.columns
├── Pyplot (tutorial)
│   └── matplotlib.pyplot.yscale()
│   └── matplotlib.scale()
│   └── mathplotlib.pyplot.subplot()
│       └── https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplot.html
└── Streamlit.table()
```
## Página
El link de la página de streamlit es:
* [Página de streamlit](https://f502-parcial01.streamlit.app/).

Debido a unos problemas se tardó un buen rato para arreglar el problema de las imágenes (causado por un .gitignore previamente hecho y que no se había tomado en consideración) que daba un error a la página a la hora de generar tanto las gráficas de las funciones binomiales (problema debido a que no leía la ubicación de las imágenes incertadas en la página, debido a que no aparecía la carpeta). Se consiguió arreglar el problema. 