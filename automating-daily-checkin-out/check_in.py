from selenium import webdriver
import time

driver = webdriver.Chrome("chromedriver")

driver.get('https://bharat.anand:Chevron@1234@munet.mu-sigma.com/Enterpriseview.aspx?html.app=EMuSigmaQMS1744d1')
time.sleep(2)

location = driver.find_element_by_xpath('/html/body/form/div[3]/div[4]/div/div/div[4]/div/div[3]/div/div/div[2]/div/div/div/table/tbody/tr/td/table/tbody/tr[2]/td/div/div/div/div/div[3]/div/table/tbody/tr[1]/td/div/div/div/span[1]/input')
location.click()
time.sleep(2)

loc_conf = driver.find_element_by_xpath('/html/body/form/div[3]/div[4]/div/div/div[4]/div/div[3]/div/div/div[2]/div/div/div/table/tbody/tr/td/table/tbody/tr[2]/td/div/div/div/div/div[3]/div/table/tbody/tr[1]/td/div/div/div/div[2]/div/div/div')
loc_conf.click()
time.sleep(2)

initiate_chkin = driver.find_element_by_xpath('/html/body/form/div[3]/div[4]/div/div/div[4]/div/div[3]/div/div/div[2]/div/div/div/table/tbody/tr/td/table/tbody/tr[2]/td/div/div/div/div/div[3]/div/table/tbody/tr[2]/td/div/div/div/div[3]/div/div')
initiate_chkin.click()
