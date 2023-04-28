from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver =webdriver.Chrome(executable_path="C:\chromedriver\chromedriver_win32\chromedriver.exe")
driver.get("http://newtours.demoaut.com/")
driver.maximize_window()
time.sleep(5)
print(driver.title)
driver.get("https://www.facebook.com/")
print(driver.title)
driver.back()
print(driver.title)
driver.forward()
print(driver.title)
driver.close()

