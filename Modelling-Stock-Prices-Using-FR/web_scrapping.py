#This script contain all the functions required to pull values from the screener.in websitee


def getting_headers(html, text1, text2):
    
    # Subsetting for quaterly results
    sub_html = html[html.find(text1):html.find(text2)]
    temp = html[html.find(text2):]
    
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
    return heading_val, sub_html, temp



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