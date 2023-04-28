import unittest
from selenium import webdriver

class Test(unittest.TestCase):
    def testname(self):
        driver=webdriver.Chrome(executable_path="C:\chromedriver\chromedriver_win32\chromedriver.exe")
        driver.get("https://www.google.com/")
        titleofWebPage=driver.title
        #assertEqual
        #self.assertEqual("Google",titleofWebPage,"webpage title is not same")
        self.assertNotEqual("Google123",titleofWebPage)
if __name__=="__main__":
    unittest.main()