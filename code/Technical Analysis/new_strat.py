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

selected_50_200 = ema_filter_50_200(ticker_list, interval)
print(selected_50_200)

final_modrsi = []
for stockcode in selected_50_200:
    rsi_val, mod_rsi_val = rsi(stockcode, '1d', 14)
    final_modrsi.append(mod_rsi_val)
    print(final_modrsi)

print(final_modrsi)

final_df =df[df['Symbol'].isin(selected_50_200)].reset_index(drop = True)
final_df.head()

final_df['rsi'] = pd.DataFrame(final_modrsi)


final_df = final_df.sort_values('rsi').reset_index(drop=True)
final_df.to_csv('output.csv', index=0)




# charts.candle_stick(data, stockcode)