from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd
import warnings
warnings.filterwarnings("ignore")


data = pd.read_csv('pass.csv')

print(data.head(3))


driver = webdriver.Chrome("chromedriver")


driver.get('http://192.168.0.2/user/ip.php')
time.sleep(20)