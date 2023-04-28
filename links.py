from select import select
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from  selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


driver =webdriver.Chrome(executable_path="C:\chromedriver\chromedriver_win32\chromedriver.exe")
driver.get("https://netbanking.hdfcbank.com/netbanking/")
driver.maximize_window()
links=driver.find_elements(By.TAG_NAME,"a")
print(len(links))

for link in links:
    print(link.text)


driver.find_element(By.LINK_TEXT,"javascript:void(0)").click()