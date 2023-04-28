from select import select
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

import time
driver = webdriver.Chrome(executable_path="C:\chromedriver\chromedriver_win32\chromedriver.exe")
#driver.get("https://www.facebook.com/")
driver.get("https://www.facebook.com/campaign/landing.php?campaign_id=14884913640&extra_1=s%7Cc%7C589460569891%7Cb%7Cfacebook%20signin%7C&placement=&creative=589460569891&keyword=facebook%20signin&partner_id=googlesem&extra_2=campaignid%3D14884913640%26adgroupid%3D128696221832%26matchtype%3Db%26network%3Dg%26source%3Dnotmobile%26search_or_content%3Ds%26device%3Dc%26devicemodel%3D%26adposition%3D%26target%3D%26targetid%3Dkwd-3821998899%26loc_physical_ms%3D1007768%26loc_interest_ms%3D%26feeditemid%3D%26param1%3D%26param2%3D&gclid=EAIaIQobChMItaDx7uvM_gIVWBVyCh05vQK4EAAYASAAEgIz3PD_BwE")
driver.maximize_window()
time.sleep(5)
element =driver.find_element(By.ID,"day")
drop_down=Select(element)
#select by visible text
drop_down.select_by_visible_text("15")
time.sleep(4)
month = driver.find_element(By.ID,"month")
drop1=Select(month)
drop1.select_by_index("5")
time.sleep(4)
year=driver.find_element(By.ID,"year")
drop2=Select(year)
drop2.select_by_value("1997")
time.sleep(20)