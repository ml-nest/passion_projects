import pandas as pd
import pdb
import api
import pickle
import time
a = 820

while a < 2000:
    dfs = pd.read_excel("MCAP31032021_0.xlsx", sheet_name="31-Mar-2021", engine="openpyxl")
    dfs = dfs.loc[dfs['Symbol'].notna()]
    company_names = dfs['Symbol'][a:a+20]
    # pdb.set_trace()

    data_dic = {}
    for i in company_names:
        if i == "MAGMA":
            i = "POONAWALLA"
        if i == "ORIENTREF":
            i = "RHIM"
        if i == "ANGELBRKG":
            i = "ANGELONE"
        if i == "3IINFOTECH":
            i = "3IINFOLTD"
        if i == "RTNINFRA":
            i = "RTNINDIA"
        print(i)
        data_dic[i] = api.output_dic(i)

    a_file = open("output\data_"+str(a)+"_"+str(a+20)+".pkl", "wb")
    pickle.dump(data_dic, a_file)
    a_file.close()
    time.sleep(5)
    a = a+20
    # print(data_dic[i])
    print(a)