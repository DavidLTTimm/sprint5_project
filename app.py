import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('./vehicles.csv')  # lendo os dados

st.header('Sprint 5 - Projeto\n')  # cria um cabeçalho

hist_button = st.button('Criar histograma.')  # cria um botão

disp_button = st.button('Criar grafico de dispersão.')  # cria um botão

fig = px.histogram(car_data, x="odometer")  # criar um histograma
fig.show()  # exibindo

# criar uma caixa de seleção
build_histogram = st.checkbox('Criar um histograma')
# criar uma caixa de seleção
build_disp_graf = st.checkbox('Criar um gráfico de dispersão')

# Caixas de seleção

if build_histogram:  # se a caixa de seleção for selecionada
    st.write('Criando um histograma para a coluna odometer')

    # cria um histograma
    fig = px.histogram(car_data, x="odometer")

    # exibe um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

if build_disp_graf:  # se a caixa de seleção for selecionada
    # escreve uma mensagem
    st.write(
        'Criando um grafico de dispersão para o conjunto de dados de anúncio de vendas de carros.')

    # criar um gráfico de dispersão
    fig = px.scatter(car_data, x="odometer", y="price")

    # exibe um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

# Se botões forem selecionados

if hist_button:  # se o botão for clicado
    # escreve uma mensagem
    st.write(
        'Criando um histograma para o conjunto de dados de anúncio de vendas de carros.')

    # cria um histograma
    fig = px.histogram(car_data, x="odometer")

    # exibe um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

if disp_button:  # se o botão for clicado
    # escreve uma mensagem
    st.write(
        'Criando um grafico de dispersão para o conjunto de dados de anúncio de vendas de carros.')

    # criar um gráfico de dispersão
    fig = px.scatter(car_data, x="odometer", y="price")

    # exibe um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)
