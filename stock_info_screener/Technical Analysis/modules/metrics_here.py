from .imports import *

def rsi(stockcode, interval, points):
    a = {'5m':'60d',
     '15m':'60d',
     '1d':'max',
     '1wk':'max', 
     '1mo':'max'}
    df = yf.download(tickers=stockcode+'.NS', period=a[interval], interval=interval)
    df = df[df['Close'].notna()]
    df = df.reset_index()
    if interval in ['5m', '15m']:
        df = df[['Datetime', 'Close']]
    else:
        df = df[['Date', 'Close']]
    # df = df[df['Close'].notna()]
    df['diff'] = df['Close'].diff(periods = 1)

    df['gain'] = df[df['diff']>0][['diff']]
    df['gain'] = df['gain'].fillna(0)

    df['loss'] = df[df['diff']<0][['diff']]
    df['loss'] = df['loss'].fillna(0)

    df['mean_gain'] = df['gain'].rolling(points).sum()
    df['mean_gain'] = df['mean_gain']/points

    df['mean_loss'] = df['loss'].rolling(points).sum()
    df['mean_loss'] = df['mean_loss']/(-1*points)

    df['rs'] = df['mean_gain']/ df['mean_loss']
    df['rsi'] = 100 - (100/(1+df['rs']))
    df = df[df['mean_gain'].notna()].reset_index(drop = True)
    if len(df) == 0:
        return np.nan, np.nan
    else:
        mean_gain = []
        mean_gain.append(np.array(df['mean_gain'])[0])
        for i in np.array(df['gain'])[1:]:
            mean_gain.append((mean_gain[-1]*(points-1) + i)/points)

        df['mod_mgain'] = pd.DataFrame(mean_gain)

        mean_loss = []
        mean_loss.append(np.array(df['mean_loss'])[0])
        for i in np.array(df['loss'])[1:]:
            mean_loss.append((mean_loss[-1]*(points-1) - i)/points)

        df['mod_mloss'] = pd.DataFrame(mean_loss)

        df['mod_rs'] = df['mod_mgain']/ df['mod_mloss']
        df['mod_rsi'] = 100 - (100/(1+df['mod_rs']))
        return df[-1:]['rsi'].values[0], df[-1:]['mod_rsi'].values[0]



def ema_filter_50_200(ticker_list, interval):
    selected_50_200 = []
    for stockcode in ticker_list:
        print(stockcode)
        try:
            a = {'5m':'60d',
                '15m':'60d',
                '1d':'300d',
                '1wk':'max', 
                '1mo':'max'}
            data = yf.download(tickers=stockcode+'.NS', period=a[interval], interval=interval)
            data['EMA9'] = data['Close'].ewm(span=9, adjust=False).mean()
            data['EMA50'] = data['Close'].ewm(span=50, adjust=False).mean()
            data['EMA200'] = data['Close'].ewm(span=200, adjust=False).mean()
            data = data.drop(['Open', 'High', 'Low', 'Volume', 'Adj Close'], axis = 1)
            if (data['EMA50'][-1] <= (data['EMA200'][-1]*1.01)) & ((data['EMA9'][-1] - data['EMA9'][-3])>0):
                selected_50_200.append(stockcode)
        except IndexError:
            continue
    return selected_50_200

def ema_filter_50_200_back(ticker_list, interval, start_date, end_date):
    selected_50_200 = []
    for stockcode in ticker_list:
        print(stockcode)
        try:
            a = {'5m':'60d',
                '15m':'60d',
                '1d':'300d',
                '1wk':'max', 
                '1mo':'max'}
            data = yf.download(tickers=stockcode+'.NS', interval=interval, start=start_date, end=end_date)
            print(data.head())
            print(data.tail())
            data['EMA9'] = data['Close'].ewm(span=9, adjust=False).mean()
            data['EMA50'] = data['Close'].ewm(span=50, adjust=False).mean()
            data['EMA200'] = data['Close'].ewm(span=200, adjust=False).mean()
            data = data.drop(['Open', 'High', 'Low', 'Volume', 'Adj Close'], axis = 1)
            if (data['EMA50'][-1] <= (data['EMA200'][-1]*1.01)) & ((data['EMA9'][-1] - data['EMA9'][-3])>0):
                selected_50_200.append(stockcode)
        except IndexError:
            continue
    return selected_50_200


def rsi_back(stockcode, interval, points, start_date, end_date):
    a = {'5m':'60d',
     '15m':'60d',
     '1d':'max',
     '1wk':'max', 
     '1mo':'max'}
    df = yf.download(tickers=stockcode+'.NS', interval=interval, start=start_date, end=end_date)
    df = df[df['Close'].notna()]
    df = df.reset_index()
    if interval in ['5m', '15m']:
        df = df[['Datetime', 'Close']]
    else:
        df = df[['Date', 'Close']]
    # df = df[df['Close'].notna()]
    df['diff'] = df['Close'].diff(periods = 1)

    df['gain'] = df[df['diff']>0][['diff']]
    df['gain'] = df['gain'].fillna(0)

    df['loss'] = df[df['diff']<0][['diff']]
    df['loss'] = df['loss'].fillna(0)

    df['mean_gain'] = df['gain'].rolling(points).sum()
    df['mean_gain'] = df['mean_gain']/points

    df['mean_loss'] = df['loss'].rolling(points).sum()
    df['mean_loss'] = df['mean_loss']/(-1*points)

    df['rs'] = df['mean_gain']/ df['mean_loss']
    df['rsi'] = 100 - (100/(1+df['rs']))
    df = df[df['mean_gain'].notna()].reset_index(drop = True)
    if len(df) == 0:
        return np.nan, np.nan
    else:
        mean_gain = []
        mean_gain.append(np.array(df['mean_gain'])[0])
        for i in np.array(df['gain'])[1:]:
            mean_gain.append((mean_gain[-1]*(points-1) + i)/points)

        df['mod_mgain'] = pd.DataFrame(mean_gain)

        mean_loss = []
        mean_loss.append(np.array(df['mean_loss'])[0])
        for i in np.array(df['loss'])[1:]:
            mean_loss.append((mean_loss[-1]*(points-1) - i)/points)

        df['mod_mloss'] = pd.DataFrame(mean_loss)

        df['mod_rs'] = df['mod_mgain']/ df['mod_mloss']
        df['mod_rsi'] = 100 - (100/(1+df['mod_rs']))
        return df[-1:]['rsi'].values[0], df[-1:]['mod_rsi'].values[0]