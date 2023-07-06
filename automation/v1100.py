from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd
import warnings
warnings.filterwarnings("ignore")


driver = webdriver.Chrome("chromedriver")

df = pd.DataFrame(columns = ['id', 'name', 'phone', 'email', 'address', 'dob'])


for i in range(39307, 39400):

    driver.get('http://117.201.254.210:8380/opac/myaccount/myAccount.html')
    time.sleep(2)

    user_id = driver.find_element_by_xpath("/html/body/div[5]/div/form/input[1]")
    user_id.send_keys(str(i))

    next_button = driver.find_element_by_xpath('/html/body/div[5]/div/form/input[4]')
    next_button.click()
    time.sleep(1)
    
    driver.get('http://117.201.254.210:8380/opac/myaccount/myProfile.html')

    

    content = driver.page_source
    soup = BeautifulSoup(content)
    try:
        table = soup.find('div', attrs = {'id':'myProfilePanel'}) 


        name = table.find('p', attrs = {'id':'nameId'}).get_text()
        member_type = table.find('p', attrs = {'id':'classId'}).get_text()
        idVal = table.find('p', attrs = {'id':'idVal'}).get_text()
        mobile = table.find('p', attrs = {'id':'mobileId'}).get_text()

        dic_1 = {'id': i, 'name': name.strip(), 'phone': mobile.strip()}

        j = 0
        for k in table.find_all('p', attrs = {'id':'Label50'}):
            if j == 0:
                dic_1['email'] = k.get_text().strip()
            if j == 1:
                dic_1['address'] = k.get_text().strip()
            if j == 3:
                dic_1['dob'] = k.get_text().strip()
            j = j+1

        df = df.append(dic_1,ignore_index = True)

        print(df.tail(1))

        df.to_csv('data_2.csv', index=False)
        
        next_button = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div[1]/span[1]')
        next_button.click()
        time.sleep(1)
    except:
        continue