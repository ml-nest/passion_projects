import pandas as pd
import numpy as np
import yfinance as yf
from IPython.display import clear_output


portfolio_per = pd.read_excel('input/inputs.xlsx', engine="openpyxl",sheet_name='portfolio_per')
cash_investments = pd.read_excel('input/inputs.xlsx', engine="openpyxl",sheet_name='cash_investments')
eq = pd.read_excel('input/holdings-RR5003.xlsx', engine="openpyxl",sheet_name='Equity')
mf = pd.read_excel('input/holdings-RR5003.xlsx', engine="openpyxl",sheet_name='Mutual Funds')

def fun1(x): 
    print(x)   
    data = yf.download(tickers=x, period='10d', interval='1d').reset_index()
    try:
        a = data['Close'].iloc[-1]
    except:
        a = np.nan
    try:
        b = data['Close'].iloc[-1] - data['Close'].iloc[-2]
    except:
        b = np.nan
    try:
        c = (data['Close'].iloc[-1] - data['Close'].iloc[-2])*100 / data['Close'].iloc[-2]
    except:
        c = np.nan
    return a, b, c


def data_manipulation(eq, type_df):
    eq = eq.iloc[21:,1:]
    new_header = eq.iloc[0] #grab the first row for the header
    eq = eq[1:] #take the data less the header row
    eq.columns = new_header #set the header row as the df header

    if type_df == 'eq':
        eq = eq.drop(['ISIN', 'Sector','Quantity Discrepant','Quantity Long Term', 'Quantity Pledged (Margin)','Quantity Pledged (Loan)', 'Previous Closing Price','Unrealized P&L', 'Unrealized P&L Pct.'], axis=1)
        eq = pd.merge(eq,pd.read_excel('input/inputs.xlsx', engine="openpyxl",sheet_name='equity_ticker'), how='outer', on='Symbol')
    else:
        eq = eq.drop(['ISIN','Instrument Type', 'Quantity Discrepant', 'Quantity Pledged (Margin)',
            'Quantity Pledged (Loan)', 'Previous Closing Price',
            'Unrealized P&L', 'Unrealized P&L Pct.'], axis=1)
        eq = pd.merge(eq,pd.read_excel('input/inputs.xlsx', engine="openpyxl",sheet_name='mf_ticker'), how='left', on='Symbol')

    print(eq[['Symbol', 'ticker']])

    a = eq.apply(lambda x: fun1(x['ticker']), axis=1)
    eq = pd.concat([eq,pd.DataFrame(a.tolist(), columns=['closing_price', 'Today(P&L)', 'Today(P&L%)'])], axis = 1)

    eq['Today(P&L)'] = eq['Today(P&L)'] * eq['Quantity Available']

    eq['invested'] = eq['Average Price'] * eq['Quantity Available']
    eq['current_value'] = eq['closing_price'] * eq['Quantity Available']
    eq['p&l'] = eq['current_value'] - eq['invested']
    eq['p_tage'] = eq['p&l']*100/ eq['invested']
    clear_output()
    return eq



eq = data_manipulation(eq, 'eq')
# Taking out the re-balancing data
re_balance = eq[eq['ideal_prop'].notna()]
del eq['ideal_prop']
eq = eq[eq['Quantity Available'].notna()]
mf = data_manipulation(mf, 'mf')
investments = pd.concat([mf, eq])

temp = investments.copy()
temp = pd.concat([temp, cash_investments]).reset_index(drop = True)
export = temp.copy()
temp['inv_type'].iloc[temp['inv_type'].isin(['index', 'stock'])] = 'equity'
temp = temp.groupby(['inv_type', 'risk_type'])['invested', 'current_value', 'Today(P&L)', 'p&l'].agg('sum').reset_index()
temp['per_increase_today'] = temp['Today(P&L)']*100 / temp['current_value']
temp['net_p&l(%)'] = temp['p&l']*100 / temp['invested']
curr_val = pd.merge(portfolio_per, temp, on=['inv_type', 'risk_type'], how='outer')
curr_val['current_asset_allocated(%)'] = (curr_val['current_value'] *100/ (curr_val['current_value'].sum()))

re_balance = re_balance[['Symbol', 'ideal_prop', 'Quantity Available','closing_price','current_value']]
re_balance = re_balance.fillna(0)

re_balance['ideal_composition'] = re_balance['current_value'].sum() * re_balance['ideal_prop']/100

re_balance['ideal_quantity'] = np.floor(re_balance['ideal_composition']/ re_balance['closing_price'])

re_balance['buy'] = re_balance['ideal_quantity'] - re_balance['Quantity Available']



from openpyxl import load_workbook
path = "final.xlsx"
book = load_workbook(path)
book.remove(book['agg_sheet'])
book.remove(book['equity'])
book.remove(book['mf'])
book.remove(book['cash_investments'])
book.remove(book['re_balance'])
writer = pd.ExcelWriter(path, engine = 'openpyxl')
writer.book = book
curr_val.to_excel(writer, sheet_name = 'agg_sheet', index=False)
eq.to_excel(writer, sheet_name = 'equity', index=False)
mf.to_excel(writer, sheet_name = 'mf', index=False)
cash_investments.to_excel(writer, sheet_name = 'cash_investments', index=False)
re_balance.to_excel(writer, sheet_name = 're_balance', index=False)
writer.save()
writer.close()
writer.handles = None