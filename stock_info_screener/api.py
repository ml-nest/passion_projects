from urllib.request import urlopen
import web_scrapping as ws
import pandas as pd
import numpy as np

def output_dic(company_name):
  link = "https://www.screener.in/company/"+company_name+"/consolidated/"

  page = urlopen(link)

  html_bytes = page.read()
  rest = html_bytes.decode("utf-8")

  dic = {}
  for i in range(10):
    results,rest, title = ws.table_return(rest)
    if (title != 'Peer comparison') and (len(title) !=0):
      dic[title] = results

  return dic
