from selenium import webdriver
import time

driver = webdriver.Chrome("chromedriver")

driver.get('http://chevron.cloud.com/')
time.sleep(10)

employee_button = driver.find_element_by_xpath('/html/body/div[1]/main/div/div/div[2]/form/button[1]')
employee_button.click()
time.sleep(8)

user_id = driver.find_element_by_xpath('/html/body/div/form[1]/div/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/input[1]')
user_id.send_keys('bharatanand@chevron.com')

next_button = driver.find_element_by_xpath('/html/body/div/form[1]/div/div/div[1]/div[2]/div[2]/div/div/div/div[4]/div/div/div/div/input')
next_button.click()
time.sleep(5)

authentication_click = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div/div/div[2]/form/div/a[2]')
authentication_click.click()

otp_input = input('Enter otp ')
otp = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div/div[1]/div/form/div[4]/input')
otp.send_keys(otp_input)

otp_click = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[1]/div[2]/div/div[1]/div/form/div[7]/input')
otp_click.click()
time.sleep(5)


doc_present = int(input('Is doc present '))
if doc_present == 1:
    doc_skip = driver.find_element_by_xpath('/html/body/main/div/div[2]/div/div/button')
    doc_skip.click()
    time.sleep(2)

    doc_yes = driver.find_element_by_xpath('/html/body/main/div/div[4]/div/button[2]')
    doc_yes.click()
    time.sleep(10)

conf_yes = driver.find_element_by_xpath('/html/body/div/form/div[1]/div/div[1]/div[2]/div/div[2]/div/div[3]/div[2]/div/div/div[2]/input')
conf_yes.click()
time.sleep(15)

detect_ws = driver.find_element_by_xpath('/html/body/div/section/div[2]/div/div/div[1]/div[2]/section/button/div')
detect_ws.click()

loop = int(input('start loop ? '))
if loop == 1:
    for i in range(500000):
        driver.refresh()
        time.sleep(300)
