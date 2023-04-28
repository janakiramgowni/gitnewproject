from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from  selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time
driver =webdriver.Chrome(executable_path="C:\chromedriver\chromedriver_win32\chromedriver.exe")
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
time.sleep(5)
#how to find how many input boxes present in webpage
inputboxes=driver.find_elements(By.CLASS_NAME,"text_field")
print(len(inputboxes))
#how to provide value to text inputboxes
#inputboxes=driver.find_elements(By.CLASS_NAME,"text_field").send_keys("janaki")

inputboxes2=driver.find_elements(By.CLASS_NAME,"text_field").is_displayed()
print(inputboxes2.is_displayed)