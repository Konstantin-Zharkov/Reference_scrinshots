from selenium import webdriver
import time
from selenium.webdriver.common.by import By


link = 'https://clients.gorealytics.com/'
browser = webdriver.Chrome()
browser.get(link)

browser.quit()
