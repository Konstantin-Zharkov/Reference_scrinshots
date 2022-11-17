
from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get('https://clients.gorealytics.com/')
html = browser.find_element(By.TAG_NAME, 'html')
button = browser.find_element(By.XPATH, '/html/body/div/main/section/div/div[2]/div/div[3]/form/button/span[2]').click()
e_mail = browser.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input').send_keys('el3206306252@gmail.com')
html.send_keys(Keys.ENTER)
password = browser.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input').send_keys('3141592qwerty')
#send_mail = browser.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span').click()

html.send_keys(Keys.ENTER)






