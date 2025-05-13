#Forma antiga de usar a API usando .news

import yfinance as yf
import pandas as pd
from datetime import datetime
import json  # Para processar strings JSON
import streamlit as st

#Deixando mais dinamico 
st.markdown('# Análise empresas')

st.text_input('Ticker Code', key = 'tickercode', value = 'GOOG')
st.markdown(f'## Ultimas notícias da {st.session_state.tickercode}:')

#Como usar o yfinance
#ticker = 'AMZN' #codigo da empresa amazon, pode-se pesquiar no google o ticker de outras empresas

ticker = st.session_state.tickercode # Pegando o ticker digitado no st.text_input

data = yf.Ticker(ticker)

#Lista de dicionarios, podendo ser acessada com o nome do dicionario, podendo ate mesmo pegar as notcias mais recentes
# r = data.news
# print(r) #mostrando as noticias mais recentes

data_news = pd.DataFrame(data.news) #transformando a lista de dicionarios em um dataframe
st.dataframe(data_news) #mostrando as noticias mais recentes

#Filtrando as noticias mais relevantes
data_news2 = data_news[['title','publisher','link','relatedTickers']] #pegando apenas as colunas que queremos
st.dataframe(data_news2)

    
end_date = datetime.now().strftime('%Y-%m-%d') #pegando a data atual usando a biblioteca datetime
#PEGAR O HISTORICO DELE
data_hist = data.history(period='max', start='2021-03-16', end=end_date, interval='5d') # Pegando o maximo de range possivel, sempre deixar o perido como maximo.
data_hist = data_hist.reset_index() # Resetando o index para pegar a data ser tratada como uma coluna

st.markdown('# Construa seu gráfico')

ex = st.selectbox('Eixo x:', data_hist.columns)
ey = st.selectbox('Eixo y:', data_hist.columns)

st.markdown(f'## Gáfico Close {ey} x {ex} Date')
# Mostrando o grafico de fechamento no site streamlit
st.line_chart(data_hist, x = ex, y = ey)
#mostrando os dados do ticker
print(data_hist)