from modules.imports import *
from modules.metrics_here import *
from modules.api import *
# # url = 'https://www1.nseindia.com/content/indices/ind_nifty500list.csv'
# # df = pd.read_csv(url)

df = pd.read_excel("../MCAP31032021_0.xlsx", sheet_name="31-Mar-2021", engine="openpyxl")
df = df.loc[df['Symbol'].notna()]
df = df[df['Sr. No.'] < 300]
df['mcap_1000cr'] = df['Market capitalization \n(Rs in Lakhs)'].astype(int)/(100*1000)

# Filtering for mcap gt than 15 thousand cr.
df = df[df['mcap_1000cr'] > 15]


# Getting only the names output
ticker_list = list(df['Symbol'])

interval = '1d'

selected_50_200 = ema_filter_50_200_back(ticker_list, interval, '2020-08-13', '2021-09-25')
print(selected_50_200)

final_modrsi = []
for stockcode in selected_50_200:
    rsi_val, mod_rsi_val = rsi_back(stockcode, '1d', 14, '1996-08-13', '2021-09-25')
    final_modrsi.append(mod_rsi_val)
    print(stockcode)

print(final_modrsi)


final_df =df[df['Symbol'].isin(selected_50_200)].reset_index(drop = True)
final_df.head()

final_df['rsi'] = pd.DataFrame(final_modrsi)
value_1_list, value_2_list = [],[]

per_10, per_15, per_20, neg_3, neg_5 = [],[],[],[],[]


def daysto_reach_target(target_val):
    try:
        value_2['target'] = 0
        value_2['target'].loc[value_2['Close'] >= target_val] = 1
        x = value_2[value_2['target'] >0]['Date'].values[0] - value_2['Date'].values[0]
        days = x.astype('timedelta64[D]')
        return days / np.timedelta64(1, 'D')
    except:
        return 0

def daysto_reach_ntarget(target_val):
    try:
        value_2['target'] = 0
        value_2['target'].loc[value_2['Close'] < target_val] = 1
        x = value_2[value_2['target'] >0]['Date'].values[0] - value_2['Date'].values[0]
        days = x.astype('timedelta64[D]')
        return days / np.timedelta64(1, 'D')
    except:
        return 9999

final_df = final_df[final_df['rsi'] <= 60]


for stockcode in list(final_df['Symbol']):
    print(stockcode)
    value_1 = yf.download(tickers= stockcode +'.NS', interval='1d', start='2021-09-20', end='2021-09-25')['Close'].values[0]
    value_2 = yf.download(tickers= stockcode +'.NS', interval='1d', start='2021-09-25', end='2022-01-03')['Close'].reset_index()
    value_1_list.append(value_1)
    per_10.append(daysto_reach_target(1.10*value_1))
    per_15.append(daysto_reach_target(1.15*value_1))
    per_20.append(daysto_reach_target(1.20*value_1))
    neg_3.append(daysto_reach_ntarget(0.97*value_1))
    neg_5.append(daysto_reach_ntarget(0.95*value_1))


# for stockcode in selected_50_200:
#     print(stockcode)
#     value_1 = yf.download(tickers= stockcode+'.NS', interval='1d', start='2019-08-9', end='2019-08-13')['Close'].values[0]
#     value_2 = yf.download(tickers= stockcode+'.NS', interval='1d', start='2019-10-11', end='2019-10-13')['Close'].values[-1]
#     value_1_list.append(value_1)
#     value_2_list.append(value_2)

final_df['invested'] = pd.DataFrame(value_1_list)
final_df['per_10'] = pd.DataFrame(per_10)  
final_df['per_15'] = pd.DataFrame(per_15)  
final_df['per_20'] = pd.DataFrame(per_20)  
final_df['neg_3'] = pd.DataFrame(neg_3)  
final_df['neg_5'] = pd.DataFrame(neg_5)   


final_df = final_df.sort_values('rsi').reset_index(drop=True)
final_df.to_csv('output_backtesting.csv', index=0)

# charts.candle_stick(data, stockcode)