from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver=webdriver.Chrome("C:\chromedriver\chromedriver_win32\chromedriver.exe")
driver.get("https://www.google.com/")
driver.maximize_window()
driver.find_element(By.NAME,"q").send_keys("Mahesh babu")
time.sleep(5)
driver.find_element(By.NAME,"btnK").click()
time.sleep(5)
print(driver.title)
print(driver.current_url)