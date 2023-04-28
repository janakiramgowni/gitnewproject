from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver=webdriver.Chrome("C:\chromedriver\chromedriver_win32\chromedriver.exe")
driver.get("https://www.facebook.com/")
driver.maximize_window()
driver.find_element(By.ID,"email").send_keys("gownijanakiram50@gmail.com")
driver.find_element(By.ID,"pass").send_keys("Djlucky986642@")
driver.find_element(By.NAME,"login").click()
time.sleep(15)
