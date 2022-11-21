from selenium.webdriver.common.by import By
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://berrrloga.ru/')


class screenshots:

    element = browser.find_element(By.XPATH, '/html/body')
    element.screenshot("screenshot_full.png")