
# General Use functions

def initial_treatment(filename, drop_cols = [], cols_lower = []):
    try:
        df = pd.read_csv(filename)
    except:
        df = pd.read_excel(filename, engine="openpyxl")

    df.columns = [x.lower() for x in df.columns]
    df = lower_cols(df, cols_lower)
    df = df.drop(drop_cols, axis=1)    
    return df

def lower_cols(df, col_names):
    try:
        for i in col_names:
            df[i] = df[i].str.lower()
        return df
    except:
        return df

def change_col_str(df, cols):
    for i in cols:
        df[i] = df[i].astype(str)
    return df