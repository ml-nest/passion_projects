from selenium import webdriver
import time

driver = webdriver.Chrome("chromedriver")

driver.get('https://www.instagram.com/')
time.sleep(2)

def input_value(xpath, value):
    user_id = driver.find_element_by_xpath(xpath)
    user_id.send_keys(value)

def on_click(xpath):
    login_click = driver.find_element_by_xpath(xpath)
    login_click.click()

input_value("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input", 'bharatspaceanand@gmail.com')
input_value("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input", '01729417185274')
on_click('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]')
time.sleep(3)
on_click('/html/body/div[1]/section/main/div/div/div/div/button')
time.sleep(3)
on_click('/html/body/div[4]/div/div/div/div[3]/button[2]')
time.sleep(3)

# following starts
import pandas as pd
df = pd.read_csv('usernames.csv')
followthem = list(df['0'])
for id in followthem:
    driver.get('https://www.instagram.com/'+id+'/')
    time.sleep(3)
    try:
        on_click('/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div/button')
        time.sleep(3)
    except:
        try:
            on_click('/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div/div/span/span[1]/button')
            time.sleep(3)
        except:
            pass    
# on_click('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a') #click followers
# time.sleep(2)

# # following all followers
# for i in range(1,160):
#     on_click('/html/body/div[5]/div/div/div[2]/ul/div/li['+str(i)+']/div/div[3]/button')
#     time.sleep(1)
#     try:
#         on_click('/html/body/div[6]/div/div/div/div[3]/button[2]')
#         time.sleep(1)
#     except:
#         pass

exit()