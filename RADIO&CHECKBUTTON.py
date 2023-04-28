from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from  selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time
driver =webdriver.Chrome(executable_path="C:\chromedriver\chromedriver_win32\chromedriver.exe")
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
time.sleep(5)
# #status=driver.find_element(By.ID,"RESULT_RadioButton-7_0").is_selected()
# status2=driver.find_element(By.CLASS_NAME,"multiple_choice animate").is_selected()
# print(status2)

#how to selected boxes
driver.find_element(By.ID,"RESULT_CheckBox-8_0").click()