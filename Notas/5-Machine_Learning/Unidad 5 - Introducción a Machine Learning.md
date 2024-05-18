# Unidad 5 - Introducción a Machine Learning

## Conceptos generales

* **TD:** Training Dataset -> Set de datos de entrenamiento.

```python
td = [(x_1,y_1),(x_2,y_2),...,(x_n,y_n)]
```

* **f(x):** Predictor -> Predictor

* **L:** Learner -> Aprendiz

* **x:** Input -> Dato de entrada

* **y:** Label -> Etiqueta

* **$\phi(x)$:** Feature Vector ->Vector de características: Es un vector que describe al input.

* **$E(x)\rightarrow\phi(x)$:** Feature extractor -> estractor de características 
  
  ### Ejemplo:
  
  Input: correo
  
  ```python
  features = {'length','contains @','contains .com','amnt of non alfanumeric','len text'}
  ```

* **$\mathbf{W}$:** Weigth vector -> Vector de peso: Es un vector con la misma cantidad de dim que el Feature Vector entrenado para que al realizar un producto punto entre estos se obtenga el score para obtener la etiqueta.

## Feature extractor

$$
E(x): \text{lo que sea} \rightarrow \mathbb{R}^n\\
x \rightarrow \phi(x)
$$

## Score

$$
score(x,W) = W \cdot \phi(x)
$$

## Entrenamientos comunes

### Clasificación

Clasifica los objetos. Un ejemplo común son los correos clasificados entre correos con spam y sin spam.

En el caso de una clasificación de dos posibles salidas, se tiene:

$$
sign(score) =
\begin{cases}
+\text{ si }score>0\\
?\text{ si }score=0\\
-\text{ si }score<0
\end{cases}
$$



# Fuentes interesantes:

* Tensorflow: [Basic classification: Classify images of clothing &nbsp;|&nbsp; TensorFlow Core](https://www.tensorflow.org/tutorials/keras/classification)










