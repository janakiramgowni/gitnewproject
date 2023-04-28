from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver=webdriver.Chrome("C:\chromedriver\chromedriver_win32\chromedriver.exe")
driver.get("https://www.google.com/")
driver.maximize_window()
# driver.get("https://www.facebook.com/login/")
# driver.find_element(By.LINK_TEXT,"Sign up for Facebook").click()
# driver.find_element(By.NAME,"firstname").send_keys("Gowni")
# driver.find_element(By.NAME,"lastname").send_keys("Vijay")
# driver.find_element(By.NAME,"reg_email__").send_keys("9019160106")
# driver.find_element(By.NAME,"reg_passwd__").send_keys("vijay@111")
# driver.find_element(By.NAME,"websubmit").click()
# time.sleep(20)
driver.find_element(By.NAME,"q").send_keys("Mahesh babu")
time.sleep(5)
driver.find_element(By.NAME,"btnK").click()
time.sleep(5)
driver.back()
driver.find_element(By.NAME,"q").clear()
time.sleep(5)
driver.find_element(By.NAME,"q").send_keys("Virat Kohli")
time.sleep(5)
driver.find_element(By.NAME,"btnK").click()
time.sleep(10)



