#Forma atual de usar a API usando .news

import yfinance as yf
import pandas as pd
from datetime import datetime
import json  # Para processar strings JSON
import streamlit as st

# Deixando mais dinâmico 
st.markdown('# Análise empresas')

st.text_input('Ticker Code', key='tickercode', value='GOOG')
st.markdown(f'## Últimas notícias da {st.session_state.tickercode}:')

# Como usar o yfinance
# ticker = 'AMZN' #codigo da empresa amazon, pode-se pesquisar no google o ticker de outras empresas

ticker = st.session_state.tickercode  # Pegando o ticker digitado no st.text_input

data = yf.Ticker(ticker)

# Lista de dicionários, podendo ser acessada com o nome do dicionário, podendo até mesmo pegar as notícias mais recentes
# r = data.news
# print(r) # mostrando as notícias mais recentes

news_raw = data.news  # Lista de dicionários

# Processando as notícias
noticias_processadas = []
if news_raw:
    for item in news_raw:
        content = item.get('content', {})
        titulo = content.get('title', 'Sem título')
        url = content.get('canonicalUrl', {}).get('url', 'Sem link')
        
        # Alguns campos não estão presentes — usar .get com fallback
        publisher = content.get('provider', {}).get('displayName', 'Desconhecido')
        related = content.get('relatedTickers', []) or item.get('relatedTickers', [])
        related = ', '.join(related) if related else 'Não informado'
        
        noticias_processadas.append({
            'title': titulo,
            'url': url,
            'publisher': publisher,
            'relatedTickers': related
        })

    # Exibir DataFrame no Streamlit
    df_news = pd.DataFrame(noticias_processadas)
    st.dataframe(df_news)
else:
    st.warning("Nenhuma notícia encontrada para este ticker.")

# ========== HISTÓRICO ==========
end_date = datetime.now().strftime('%Y-%m-%d')
# Pegando o histórico de ações com o período máximo possível
data_hist = data.history(period='max', start='2021-03-16', end=end_date, interval='5d')
data_hist = data_hist.reset_index()  # Resetando o index para pegar a data como coluna

st.markdown('# Construa seu gráfico')

# Selecionando os eixos do gráfico
ex = st.selectbox('Eixo x:', data_hist.columns)
ey = st.selectbox('Eixo y:', data_hist.columns)

st.markdown(f'## Gráfico de {ey} por {ex}')
# Mostrando o gráfico de fechamento no site Streamlit
st.line_chart(data_hist, x=ex, y=ey)

# Exibir os dados brutos do ticker
st.dataframe(data_hist)
