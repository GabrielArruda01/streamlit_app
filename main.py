import streamlit as st
import pandas as pd
import appdirs as ad
ad.user_cache_dir = lambda *args: "/tmp"
import yfinance as yf

st.title("Finance Dashboard")

tickers = ('BTC-USD', 'ETH-USD', 'SOL-USD', 'XRP-USD', 'DOT-USD', 'ADA-USD', 'CDI', '^BVSP', '^GSPC', '^IXIC')

dropdown = st.multiselect('Escolha seus ativos',
                          tickers)
start = st.date_input('Inicio', value = pd.to_datetime('2015-01-01'))
end = st.date_input('Fim', value = pd.to_datetime('today'))

def relativeret(df):
    relative = df.pct_change()
    cumret = (1+relative).cumprod() - 1
    cumret = cumret.fillna(0)
    return cumret

if len(dropdown) > 0:
    df = relativeret(yf.download(dropdown, start, end)['Adj Close'])
    st.header('Retornos do {}'.format(dropdown))
    st.line_chart(df)


