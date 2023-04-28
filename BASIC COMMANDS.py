from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver =webdriver.Chrome(executable_path="C:\chromedriver\chromedriver_win32\chromedriver.exe")
driver.get("https://www.facebook.com/")

print(driver.title)   #returns the title of the page
print(driver.current_url)
time.sleep(5)
driver.close()
