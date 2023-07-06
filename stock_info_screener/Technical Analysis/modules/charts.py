from .imports import *


def candle_stick(stockcode, interval):
    a = {'5m':'60d',
     '15m':'60d',
     '1d':'max',
     '1wk':'max', 
     '1mo':'max'}
    data = yf.download(tickers=stockcode+'.NS', start='2019-08-13', end='2022-01-03', interval=interval).reset_index()
    #declare figure
    fig = go.Figure()

    #Candlestick
    fig.add_trace(go.Candlestick(x=data['Date'],
                    open=data['Open'],
                    high=data['High'],
                    low=data['Low'],
                    close=data['Close'], name = 'market data'))

    fig.update_xaxes(
        rangeslider_visible=True,
        rangebreaks=[{ 'pattern': 'day of week', 'bounds': [6, 1]}
        ]
    )

    # Add titles
    fig.update_layout(
        title=stockcode,
        yaxis_title='Stock Price (Rupee per Share)')

    #Show
    fig.show()