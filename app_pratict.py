import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

#crear un data frame de productos
st.title("Hello mi primer Streamt")
st.write("Practica  1")

data={
    'Producto':["laptop","Smartphone","Monitor","Tablet","Teclado"],
    'Precio':[1000,500,300,200,50],
    'Cantidad':[10,20,15,5,30]
}

df=pd.DataFrame(data)
st.subheader("Data Frame de Productos")
st.write(df)
st.bar_chart(df.set_index("Producto"))
st.write("Graficas")
st.header("Graficas de Precios de Productos")
fig, aux  =plt.subplots()
aux.bar(df['Producto'],df['Precio'], color ="green")
aux.set_xlabel("Producto")
aux.set_ylabel("Precio")
st.pyplot(fig)

fig = px.bar(
    df,
    x="Producto",
    y="Cantidad",
    title="Ventas por Producto"
)

st.plotly_chart(fig)

st.header("Graficas de Cantidad de Productos")