
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
import os
from discord.ext import tasks


browser = webdriver.Chrome()
browser.get('https://clients.gorealytics.com/')
browser.set_window_size(1280, 1100)
sleep(5)

class Folders:
    os.mkdir('Screens')
    os.mkdir('Difference')

class Authorization:

    button = browser.find_element(By.XPATH, '/html/body/div/main/section/div/div[2]/div/div[3]/form/button/span[2]').click()
    e_mail = browser.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input').send_keys('zharkov@gorealytics.com')
    button_send_mail = browser.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button').click()
    sleep(1)
    password = browser.find_element(By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input').send_keys('93tuy457')
    send_password = browser.find_element(By.XPATH,'/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button').click()
    sleep(10)


class SelectDash:

    dash = browser.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div/div/div/table/tbody/tr[22]/td[1]').click()
    sleep(10)


class Screens:

    Leaderboard_scr = browser.save_screenshot("Leaderboard_ref.png")
    Overview_report = browser.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div/ul/li[3]/a/span[2]').click()
    sleep(5)
    Overview_report_scr = browser.save_screenshot('Overview_report_ref.png', )
    Attribute_analysis = browser.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div/ul/li[4]/a/span[2]').click()
    sleep(5)
    Attribute_analysis_scr = browser.save_screenshot('Attribute_analysis_ref.png')
    CSAT_analysis = browser.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div/ul/li[5]/a/span[2]').click()
    sleep(5)
    CSAT_analysis_scr = browser.save_screenshot('CSAT_analysis_ref.png')
    Brands_VS_Competitors = browser.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div/ul/li[6]/a/span[2]').click()
    sleep(5)
    Brands_VS_Competitors_scr = browser.save_screenshot('Brands_VS_Competitors_ref.png')
    Reviews = browser.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div/ul/li[7]/a/span[2]').click()
    sleep(10)
    Reviews_scr = browser.save_screenshot('Reviews_ref.png')


@tasks.loop(minutes=15.0)
async def my_task():
    def make_new_screens():
        Leaderboard_scr = browser.save_screenshot("Leaderboard_new.png")
        Overview_report = browser.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div/ul/li[3]/a/span[2]').click()
        sleep(5)
        Overview_report_scr = browser.save_screenshot('Overview_report_new.png', )
        Attribute_analysis = browser.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div/ul/li[4]/a/span[2]').click()
        sleep(5)
        Attribute_analysis_scr = browser.save_screenshot('Attribute_analysis_new.png')
        CSAT_analysis = browser.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div/ul/li[5]/a/span[2]').click()
        sleep(5)
        CSAT_analysis_scr = browser.save_screenshot('CSAT_analysis_new.png')
        Brands_VS_Competitors = browser.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div/ul/li[6]/a/span[2]').click()
        sleep(5)
        Brands_VS_Competitors_scr = browser.save_screenshot('Brands_VS_Competitors_new.png')
        Reviews = browser.find_element(By.XPATH, '//*[@id="app"]/div/div[1]/div/ul/li[7]/a/span[2]').click()
        sleep(10)
        Reviews_scr = browser.save_screenshot('Reviews_new.png')
    make_new_screens()




browser.close()
browser.quit()