import yfinance as yf
import pandas as pd

import streamlit as st

#Deixando mais dinamico 
st.markdown('# Análise empresas')

st.text_input('Ticker Code', key = 'tickercode')
st.markdown('## Notícias')

#Como usar o yfinance
#ticker = 'AMZN' #codigo da empresa amazon, pode-se pesquiar no google o ticker de outras empresas

ticker = st.session_state.tickercode # Pegando o ticker digitado no st.text_input

data = yf.Ticker(ticker)

#Lista de dicionarios, podendo ser acessada com o nome do dicionario, podendo ate mesmo pegar as notcias mais recentes
# r = data.news
# print(r) #mostrando as noticias mais recentes

data_news = pd.DataFrame(data.news) #transformando a lista de dicionarios em um dataframe
st.dataframe(data_news)

#PEGAR O HISTORICO DELE
data_hist = data.history(period='max', start='2019-03-16', end='2023-03-16', interval='5d') # Pegando o maximo de range possivel, sempre deixar o perido como maximo.
data_hist = data_hist.reset_index() # Resetando o index para pegar a data ser tratada como uma coluna

# Mostrando o grafico de fechamento no site streamlit
st.line_chart(data_hist, x = 'Date', y = 'Close')
#mostrando os dados do ticker
print(data_hist)