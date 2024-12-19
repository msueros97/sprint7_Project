import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')

st.header('Análisis de la Distribución de Vehicles')
hist_button = st.button('Construir histograma') # crear un botón
scat_button = st.button('Construir Gráfico de Dispersión')

if hist_button: # al hacer clic en el botón
    
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

if scat_button:
    # escribir un mensaje
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    
    # crear un gráfico de dispersión
    graph = px.scatter(car_data, x='odometer',y='price',title='Gráfico de Dispersión')

    # mostrar el gráfico
    st.plotly_chart(graph, use_container_width=True)