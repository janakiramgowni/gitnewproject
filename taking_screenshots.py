import time

from selenium import webdriver

driver = webdriver.Chrome("C:\chromedriver\chromedriver_win32\chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
time.sleep(10)
driver.maximize_window()
# driver.save_screenshot("C:\screenshots\homepage.png")
driver.get_screenshot_as_file("C:\screenshots\homepage2.jpg")
