#This script contain all the functions required to pull values from the screener.in website

import pandas as pd

def getting_headers(html):
    # Subsetting for quaterly results
    sub_html = html[html.find('<h2')+4:]
    title = sub_html[:sub_html.find('</h2>')]
    temp = sub_html[sub_html.find('<h2'):]
    sub_html = sub_html[:sub_html.find('<h2')]

    if title != 'Peer comparison':

        # getting the headers
        breaker = "thead"

        start_text, end_text = "<"+breaker+">", "</"+breaker+">"
        headings = sub_html[sub_html.find(start_text)+len(start_text):sub_html.find(end_text)]

        breaker = "th"
        start_text, end_text = "<"+breaker+">", "</"+breaker+">"
        headings = headings[headings.find(end_text)+len(end_text):]
        
        heading_val = []
        for i in range(100):
            val = headings[headings.find(start_text)+len(start_text):headings.find(end_text)]
            headings = headings[headings.find(end_text)+len(end_text):]
            heading_val.append(val)
            if headings.find(start_text) == -1:
                break
        return heading_val, sub_html, temp, title
    else:
        return 'a','a',temp, title




def results(temp, start_text, end_text):    
    val1 = temp[temp.find(start_text)+len(start_text):temp.find(end_text)]
    temp = temp[temp.find(end_text)+len(end_text):]
    return val1, temp

def func(html, find_text, breaker, headings_value):
    position = html.find(find_text)
    if position == -1:
        headings = []
        for i in range(len(headings_value)):
            headings.append("")
        temp = html[:]
    else:
        temp = html[position:]
        temp = temp[temp.find("/"+breaker+">")+len("</"+breaker+">"):]

        start_text, end_text = "<"+breaker+">", "</"+breaker+">"

        headings = []
        for i in range(len(headings_value)):
            q, temp = results(temp, start_text, end_text)
            headings.append(q)
    return headings, temp

import numpy as np

def string_to_float(list1):    
    for i in range(len(list1)):
        if list1[i] == '':
            list1[i] = np.nan
        else:
            list1[i] = list1[i].replace(",","")
            list1[i] = float(list1[i].replace("%",""))
    return list1


def row_return(temp):
  rows = []
  temp1 = temp
  while temp1.find('<td class="text">') > 0:
    temp1 = temp1[temp1.find('<td class="text">'):]
    a = temp1[:temp1.find("</td>")]

    if a.find("&nbsp") != -1:
      a = a[a.find('this)">\n ')+8:a.find("&nbsp")]
    else:
      a = a[a.find('\n          \n')+12:]
      a = a[:a.find('\n          \n')]
    a = a.strip()
    rows.append(a)
    temp1 = temp1[temp1.find("</td>"):]
  return rows

def table_return(temp):
    headings_value, temp, rest, title = getting_headers(temp)
    if title == 'class="margin-0">Shareholding Pattern':
        title = 'Shareholding Pattern'
    elif title == 'class="margin-0">Documents':
        title = 'Peer comparison'
    if title != 'Peer comparison':
        try:
            qr_index = row_return(temp)
            quarter_results = pd.DataFrame(columns = headings_value)

            for i in qr_index:
                values, temp = func(temp, i, "td", headings_value)
                quarter_results.loc[i] = string_to_float(values)
                
            return quarter_results,rest, title.strip()
        except:
            return np.nan,rest,title.strip()
    else:
        return np.nan,rest,title.strip()
