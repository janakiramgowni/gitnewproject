from select import select
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

import time

driver = webdriver.Chrome(executable_path="C:\chromedriver\chromedriver_win32\chromedriver.exe")
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
time.sleep(5)
element = driver.find_element(By.ID, "RESULT_RadioButton-9")
drop = select(element)
# select by visible
drop.select_by_visible_text("Morning")  # morning

# select by index
# drop.select_by_index(2)  #afternoon
# select by value
# drop.select_by_value("Radio-2") #evng
