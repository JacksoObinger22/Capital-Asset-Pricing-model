import numpy as np
import pandas as pd
import streamlit as st
import preprocessor
import helper
import matplotlib.pyplot as plt
import plotly.express as px
import yfinance as yf
import plotly.graph_objects as go

st.title('Capital Asset Pricing Model (CAPM)')
st.write('This app calculates the expected return of a portfolio  using the Capital Asset Pricing Model (CAPM).')
tickit_input = st.text_input('Enter the tickers of the stocks in your portfolio separated by commas (e.g. AAPL,MSFT,GOOGL):')
start_date = st.date_input('Enter the start date:')
end_date = st.date_input('Enter the end date:')
if st.button('Get Data'):
    data = preprocessor.fetching_data(tickit_input, start_date, end_date)
    st.write(f'Data  from {start_date} to {end_date}')
    st.table(data.head())
    normalized_data = preprocessor.Normalizing(data)
    st.plotly_chart(helper.interative_plot(normalized_data, 'Normalized Prices'), use_container_width=True)
    stocks_daily_return = preprocessor.daily_return(data)
   # Calculate beta of all stocks
    beta, alpha = helper.calculate_beta_alpha(stocks_daily_return)
    #sp500 return
    rm = round(stocks_daily_return['sp500'].mean() * 252, 3)
    st.header('Market Return (RM) Sp500:')
    st.subheader(rm)
    st.write('The CAPM formula is:')
    st.latex(r'ER_i = R_f + \beta_i(ER_m - R_f)')
    ticker = '^TNX'
    data = yf.download(ticker, start=start_date, end=end_date)['Adj Close'].mean()
    rf = data / 100
    st.subheader('Risk-Free Rate (Rf):')
    st.write(str(rf))
    keys = list(beta.keys())
    ER = {}
    for i in keys:
        ER[i] = rf + (beta[i] * (rm - rf))
    for i in keys:
        st.write('Expected Return Based on CAPM for {} is {}%'.format(i, round(ER[i], 3)))
    fig = go.Figure([go.Bar(x=list(beta.keys()), y=list(beta.values()))])
    fig.update_layout(title_text='Beta Values for Stocks',xaxis_title='Stock Tickers',
yaxis_title='Beta Values',template='plotly_dark',width=800,height=500)
    st.plotly_chart(fig, use_container_width=True)
    # alpha values
    st.subheader('Alpha Values for Stocks')
    fig = go.Figure([go.Bar(x=list(alpha.keys()), y=list(alpha.values()))])
    fig.update_layout(title_text='Alpha Values for Stocks', xaxis_title='Stock Tickers',
                      yaxis_title='ALpha Values', template='plotly_dark', width=80, height=500)
    st.plotly_chart(fig, use_container_width=True)

    #portfolio weights
    st.subheader('Portfolio Weights')
    st.write('assuming equal weights for all stocks')
    portfolio_weights = 1 / len(keys) * np.ones(len(keys))
    portfolio_weight_all = round(sum(list(ER.values()) * portfolio_weights), 3)
    st.write('Expected Return Based on CAPM for Portfolio is {}%'.format(portfolio_weight_all))
    # plot of portfolio return and market return
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=list(ER.keys()), y=list(ER.values()), mode='lines+markers', name='Expected Return'))
    fig.add_trace(go.Scatter(x=list(ER.keys()), y=[rm] * len(ER), mode='lines', name='Market Return'))
    fig.update_layout(title_text='Portfolio Return vs Market Return', xaxis_title='Stock Tickers',
                      yaxis_title='Return', template='plotly_dark', width=800, height=500)
    st.plotly_chart(fig, use_container_width=True)
   # plot of total portfolio return and market return
    fig=px.pie(values=[portfolio_weight_all,rm],names=['Portfolio Return','Market Return'],title='Portfolio Return vs Market Return')
    st.plotly_chart(fig,use_container_width=True)
    #plot of regression line
    Returns = pd.DataFrame(ER.values(), keys)
    Returns.sort_values(by=0, ascending=False, inplace=True)
    #plot returns
    st.subheader('Returns')
    fig = go.Figure([go.Bar(x=Returns.index, y=Returns[0])])
    fig.update_layout(title_text='Returns for Stocks', xaxis_title='Stock Tickers',
                      yaxis_title='Returns', template='plotly_dark', width=800, height=500)
    st.plotly_chart(fig, use_container_width=True)
    # table of retrun alpha and beta
    st.subheader('Returns, Alpha and Beta')
    Returns.rename(columns={0: 'Return'}, inplace=True)
    Returns['Alpha'] = list(alpha.values())
    Returns['Beta'] = list(beta.values())
    st.table(Returns)




































