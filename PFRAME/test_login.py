from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time


def test_google():
    driver = webdriver.Chrome("C:\chromedriver\chromedriver_win32\chromedriver.exe")
    driver.implicitly_wait(10)
    driver.get('http://google.com')
    assert driver.title == "Google"
    time.sleep(25)
    driver.quit()

# def test_facebook():
#     driver = webdriver.Chrome("C:\chromedriver\chromedriver_win32\chromedriver.exe")
#     driver.implicitly_wait(10)
#     driver.get('http://facebook.com')
#     assert driver.title == "facebook -log in or sign up"
#     driver.quit()
#
# def test_insta():
#     driver = webdriver.Chrome("C:\chromedriver\chromedriver_win32\chromedriver.exe")
#     driver.implicitly_wait(10)
#     driver.get('http://instagram.com')
#     assert driver.title == "Instagram"
#     driver.quit()
#
# def test_gmail():
#     driver = webdriver.Chrome("C:\chromedriver\chromedriver_win32\chromedriver.exe")
#     driver.implicitly_wait(10)
#     driver.get('http://gmail.com')
#     assert driver.title == "gmail"
#     driver.quit()
