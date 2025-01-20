
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Parámetros
x_0 = 0          # Población inicial
K = 1           # Capacidad de carga
r = 0           # Tasa de crecimiento
n = 0           # Número de pasos


# Inicialización
st.title("Simulador de la ecuación logística.")

x_0 = st.slider(label = "Seleccione la pobacion inicial", min_value = 0, max_value = 1000, value = 30, step = 1)
K = st.slider(label = "Seleccione la capacidad de carga", min_value = x_0, max_value = 100000, value = 100000, step = 10)
r = st.slider(label = "Selecccione la tasa de crecimiento", min_value = 0., max_value = 5., value = 1., step = 0.1)
n = st.slider(label = "Seleccione el número de pasos", min_value = 1, max_value = 100, value = 10, step = 1)


# Inicialización (variables de gráfico)
x = np.zeros(n)
x[0] = x_0 / K    # Escalar población inicial a proporción de K

# Cálculo
for i in range(1, n):
    if x[i-1] >= 0:
        x[i] = x[i-1] + r * x[i-1] * (1 - x[i-1])  # Ecuación logística discreta
    else:
        x[i-1] = 0
        x[i] = 0


st.subheader("Gráfico")
# Gráfico
plt.plot(range(n), x * K, marker='o', label="Población")
plt.axhline(K, color='red', linestyle='--', label="Capacidad de carga (K)")
plt.title("Dinámica poblacional")
plt.xlabel("Tiempo")
plt.ylabel("Población")
plt.legend()
st.pyplot(plt)

st.subheader("Resultados")
# Resultado
st.write("La población inicial es de", int(x_0), "individuos.")
for i in range(n):
    st.write("La población en el tiempo", i, "es de", int(x[i] * K), "individuos.")

