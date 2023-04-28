import XLUtils

from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\chromedriver\chromedriver_win32\chromedriver.exe")

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

path="C:\fbtestcase.xlsx"

rows=XLUtils.getRowCount(path,'Sheet2')

for r in range(2,rows+1):
    username=XLUtils.readData(path,"Sheet2",r,1)
    password=XLUtils.readData(path,"Sheet2",r,2)

    driver.find_element(By.NAME,"username").send_keys("username")
    driver.find_element(By.NAME,"password").send_keys("password")
    driver.find_element(By.CLASS,"oxd-button oxd-button--medium oxd-button--main orangehrm-login-button").click()

     # if driver.title=="OrangeHRM:":
     #     print("test is passes")
     #     XLUtils.writeData(path,Sheet2,r,3,"test passed")
     # else:
     #     print("test failed")
     #     XLUtils.writeData(path,Sheet2,r,3,"test failed")
     #
     #     driver.find_element(By.NAME,"_2s25 _cy7").click()
     #
     #     driver.find_element(By.CLASS,"oxd-userdropdown-link").click()