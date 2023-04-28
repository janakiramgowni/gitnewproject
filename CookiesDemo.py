from selenium import webdriver

driver =webdriver.Chrome(executable_path="C:\chromedriver\chromedriver_win32\chromedriver.exe")
driver.get("https://www.amazon.in/")

driver.maximize_window()
#capture all cookies
cookies=driver.get_cookies()
print(len(cookies))   # printno of cookies
print(cookies)     #print all the cookie pairs

# adding new cookie to the browser
cookie={'name':"mycookie","value":"12345"}
driver.add_cookie(cookie)
cookies=driver.get_cookies()
print(len(cookies))   # printno of cookies after adding new cookie
print(cookies)     #print all the cookie pairs
# deleting cookie

driver.delete_cookie('mycookie')
cookies=driver.get_cookies()
print(len(cookies))   # printno of cookies
print(cookies)     #print all the cookie pairs  after deleting new cookie

# deleting all cookies
driver.delete_all_cookies()
cookies=driver.get_cookies()
print(len(cookies))
print(cookies)

