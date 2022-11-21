

from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep

browser = webdriver.Chrome()
browser.get('https://clients.gorealytics.com/')
#html = browser.find_element(By.TAG_NAME, 'html')
button = browser.find_element(By.XPATH, '/html/body/div/main/section/div/div[2]/div/div[3]/form/button/span[2]').click()
e_mail = browser.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input').send_keys('zharkov@gorealytics.com')
#html.send_keys(Keys.ENTER)
button_send_mail = browser.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button').click()
#password = browser.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input').send_keys('93tuy457')
#send_password = browser.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button').click()
sleep(10)
#html.send_keys(Keys.ENTER)
browser.close()