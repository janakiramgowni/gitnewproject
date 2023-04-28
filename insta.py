from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver=webdriver.Chrome("C:\chromedriver\chromedriver_win32\chromedriver")
driver.get("https://www.instagram.com/")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.NAME,"username").send_keys("gownijanakiram50@gmail.com")
time.sleep(2)
driver.find_element(By.NAME,"password").send_keys("Djlucky986642@")
time.sleep(2)
driver.find_element(By.CLASS_NAME,"sqdOP L3NKy y3zKF").click()
time.sleep(15)