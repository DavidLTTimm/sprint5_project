import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('../vehicles.csv')  # lendo os dados

hist_button = st.button('Criar histograma.')  # cria um botão

disp_button = st.button('Criar grafico de dispersão.')  # cria um botão

fig = px.histogram(car_data, x="odometer")  # criar um histograma
fig.show()  # exibindo

st.header('Sprint 5 - Projeto\n')  # cria um cabeçalho

if hist_button:  # se o botão for clicado
    # escreve uma mensagem
    st.write(
        'Criando um histograma para o conjunto de dados de anúncio de vendas de carros.')

    # cria um histograma
    fig = px.histograma(car_data, x='odometer')

    # exibe um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

if disp_button:  # se o botão for clicado
    # escreve uma mensagem
    st.write(
        'Criando um grafico de dispersão para o conjunto de dados de anúncio de vendas de carros.')

    # cria um histograma
    # criar um gráfico de dispersão
    fig = px.scatter(car_data, x="odometer", y="price")

    # exibe um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)
