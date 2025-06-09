import numpy as np
import pandas as pd
import streamlit as st
import preprocessor
import helper
import matplotlib.pyplot as plt
import plotly.express as px
import yfinance as yf
import plotly.graph_objects as go

st.title('Modelo de Precificação de Ativos de Capital (CAPM)')
st.write('Este aplicativo calcula o retorno esperado de uma carteira usando o Modelo de Precificação de Ativos de Capital (CAPM).')

tickit_input = st.text_input('Digite os códigos das ações da sua carteira separados por vírgulas (ex: AAPL,MSFT,GOOGL):')
start_date = st.date_input('Informe a data de início:')
end_date = st.date_input('Informe a data de término:')

if st.button('Obter Dados'):
    data = preprocessor.fetching_data(tickit_input, start_date, end_date)
    st.write(f'Dados de {start_date} até {end_date}')
    st.table(data.head())

    normalized_data = preprocessor.Normalizing(data)
    st.plotly_chart(helper.interative_plot(normalized_data, 'Preços Normalizados'), use_container_width=True)

    stocks_daily_return = preprocessor.daily_return(data)

    # Calcular beta de todas as ações
    beta, alpha = helper.calculate_beta_alpha(stocks_daily_return)

    # Retorno do mercado (SP500)
    rm = round(stocks_daily_return['sp500'].mean() * 252, 3)
    st.header('Retorno do Mercado (RM) - S&P 500:')
    st.subheader(rm)

    st.write('A fórmula do CAPM é:')
    st.latex(r'ER_i = R_f + \beta_i(ER_m - R_f)')

    # Taxa livre de risco
    ticker = '^TNX'
    data = yf.download(ticker, start=start_date, end=end_date)['Adj Close'].mean()
    rf = data / 100
    st.subheader('Taxa Livre de Risco (Rf):')
    st.write(str(rf))

    keys = list(beta.keys())
    ER = {}
    for i in keys:
        ER[i] = rf + (beta[i] * (rm - rf))

    for i in keys:
        st.write('Retorno Esperado pelo CAPM para {} é de {}%'.format(i, round(ER[i], 3)))

    fig = go.Figure([go.Bar(x=list(beta.keys()), y=list(beta.values()))])
    fig.update_layout(title_text='Valores de Beta por Ação', xaxis_title='Códigos das Ações',
                      yaxis_title='Valores de Beta', template='plotly_dark', width=800, height=500)
    st.plotly_chart(fig, use_container_width=True)

    # Valores de alpha
    st.subheader('Valores de Alpha por Ação')
    fig = go.Figure([go.Bar(x=list(alpha.keys()), y=list(alpha.values()))])
    fig.update_layout(title_text='Valores de Alpha por Ação', xaxis_title='Códigos das Ações',
                      yaxis_title='Valores de Alpha', template='plotly_dark', width=800, height=500)
    st.plotly_chart(fig, use_container_width=True)

    # Pesos da carteira
    st.subheader('Pesos da Carteira')
    st.write('Assumindo pesos iguais para todas as ações')
    portfolio_weights = 1 / len(keys) * np.ones(len(keys))
    portfolio_weight_all = round(sum(list(ER.values()) * portfolio_weights), 3)
    st.write('Retorno Esperado da Carteira com base no CAPM é de {}%'.format(portfolio_weight_all))

    # Gráfico: retorno da carteira vs retorno do mercado
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=list(ER.keys()), y=list(ER.values()), mode='lines+markers', name='Retorno Esperado'))
    fig.add_trace(go.Scatter(x=list(ER.keys()), y=[rm] * len(ER), mode='lines', name='Retorno do Mercado'))
    fig.update_layout(title_text='Retorno da Carteira vs Retorno do Mercado', xaxis_title='Códigos das Ações',
                      yaxis_title='Retorno', template='plotly_dark', width=800, height=500)
    st.plotly_chart(fig, use_container_width=True)

    # Gráfico: retorno total da carteira vs retorno do mercado
    fig = px.pie(values=[portfolio_weight_all, rm], names=['Retorno da Carteira', 'Retorno do Mercado'], 
                 title='Retorno da Carteira vs Retorno do Mercado')
    st.plotly_chart(fig, use_container_width=True)

    # Gráfico de retornos
    Returns = pd.DataFrame(ER.values(), keys)
    Returns.sort_values(by=0, ascending=False, inplace=True)

    st.subheader('Retornos')
    fig = go.Figure([go.Bar(x=Returns.index, y=Returns[0])])
    fig.update_layout(title_text='Retornos por Ação', xaxis_title='Códigos das Ações',
                      yaxis_title='Retorno', template='plotly_dark', width=800, height=500)
    st.plotly_chart(fig, use_container_width=True)

    # Tabela: retorno, alpha e beta
    st.subheader('Retorno, Alpha e Beta')
    Returns.rename(columns={0: 'Retorno'}, inplace=True)
    Returns['Alpha'] = list(alpha.values())
    Returns['Beta'] = list(beta.values())
    st.table(Returns)
