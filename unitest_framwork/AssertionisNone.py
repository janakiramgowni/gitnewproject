import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def testname(self):
        driver=webdriver.Chrome(executable_path="C:\chromedriver\chromedriver_win32\chromedriver.exe")
        #driver=None
    #assertisNone
        #self.assertIsNone(driver)
    #assertisNotNone
        self.assertIsNotNone(driver)

if __name__=="__main__":
    unittest.main()