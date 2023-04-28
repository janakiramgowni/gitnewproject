from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver=webdriver.Chrome("C:\chromedriver\chromedriver_win32\chromedriver.exe")
driver.get("https://www.google.com/")
driver.maximize_window()
driver.get("https://www.flipkart.com")
time.sleep(5)
driver.find_element(By.CLASS_NAME,"_3704LK").send_keys("cricket bat")
#driver.find_element(By.XPATH,"//button[@type='submit']//*[name()='svg']//*[name()='g' and contains(@fill,'#2874F1')]//*[name()='path']").click()
time.sleep(10)