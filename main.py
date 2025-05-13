import yfinance as yf
import pandas as pd

#Como usar o yfinance
ticker = 'AMZN' #codigo da empresa amazon, pode-se pesquiar no google o ticker de outras empresas

data = yf.Ticker(ticker)

#Lista de dicionarios, podendo ser acessada com o nome do dicionario, podendo ate mesmo pegar as notcias mais recentes
r = data.news
print(r) #mostrando as noticias mais recentes

#PEGAR O HISTORICO DELE
data_hist = data.history(period='max', start='2019-03-16', end='2023-03-16', interval='5d') #pegando o maximo de range possivel, sempre deixar o perido como maximo.

#print(data) #mostrando os dados do ticker
print(data_hist)