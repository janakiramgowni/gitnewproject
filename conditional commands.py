from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from  selenium.webdriver.common.by import By

import time
driver =webdriver.Chrome(executable_path="C:\chromedriver\chromedriver_win32\chromedriver.exe")
driver=webdriver(service=serv_obj)
driver.get("https://www.facebook.com/")
driver.maximize_window()
time.sleep(5)
element=driver.find_element(By.NAME,"email")
print(element.is_displayed())  #returns true/false based of element status
print(element.is_enabled())  # retruns true/false
element1=driver.find_element(By.NAME,"pass")
print(element1.is_displayed())
element.send_keys("gownijanakiram50@gmail.com")
element1.send_keys("Djlucky986642@")
driver.find_element(By.NAME,"login").click()
time.sleep(20)
