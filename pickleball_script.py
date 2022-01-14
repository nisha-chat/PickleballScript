
#!/usr/bin/env python3

import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import pause
import datetime

# put fill file path to chromedriver
driver = webdriver.Chrome("/Users/your_laptop_username/Desktop/chromedriver")

driver.get('https://apm.activecommunities.com/citymb/ActiveNet_Home/makeOnlineQuickReservation.sdi')
driver.maximize_window()

username = driver.find_element_by_id("ctl05_ctlLoginLayout_txtUserName")
password = driver.find_element_by_id("ctl05_ctlLoginLayout_txtPassword")

# replace 2022, 1, 9 with tomorrow's date
target = datetime.datetime(2022,1,15,5,59,0)

now = datetime.datetime.now()
delta = target - now
if delta > datetime.timedelta(0):
    print('will sleep: %s' % delta)
    time.sleep(delta.total_seconds()/4)
    print('sleep for: %s' % ((delta.total_seconds())/4))
    time.sleep(delta.total_seconds()/4)
    print('sleep for: %s' % ((delta.total_seconds())/4))
    time.sleep(delta.total_seconds()/4)
    print('sleep for: %s' % ((delta.total_seconds())/4))
    time.sleep(delta.total_seconds()/4)

# replace username with your username and password with your password
username.send_keys("your username")
password.send_keys("your password")

driver.find_element_by_id("ctl05_ctlLoginLayout_btnLogin").click()
driver.implicitly_wait(5)

driver.execute_script("window.scrollTo(0, 1500)")
driver.implicitly_wait(5)
select = Select(driver.find_element_by_id('facilitygroup_id'))

select.select_by_visible_text('MH Paddleball/Pickleball Court')

select = Select(driver.find_element_by_id('begd'))
# replace 10 with the date for 4 days from tomorrow (tomorrow is the 7th so we put the 11th)
select.select_by_visible_text('19')

driver.find_element_by_class_name("button_wcag2").click();

driver.execute_script("window.scrollTo(0, 1500)")

participants = driver.find_element_by_xpath('//*[@id="availability_bodyhtml"]/table/tbody/tr[4]/td/table/tbody/tr/td/table/tbody/tr[2]/td[3]/input')
participants.send_keys("1")


participants = driver.find_element_by_name("aci_19392")
participants.send_keys("NC")

try:
    driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[3]/div[1]/table/tbody/tr[6]/td/div/form/table/tbody/tr[3]/td/div/div/table/tbody/tr[3]/td/table/tbody/tr/td/table/tbody/tr[4]/td/table/tbody/tr/td/table/tbody/tr[2]/td[14]/input").click()
except:
    print("5pm taken")
    try:
        driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[3]/div[1]/table/tbody/tr[6]/td/div/form/table/tbody/tr[3]/td/div/div/table/tbody/tr[3]/td/table/tbody/tr/td/table/tbody/tr[4]/td/table/tbody/tr/td/table/tbody/tr[2]/td[15]/input").click()
    except:
        print("6pm taken")
        try:
            driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[3]/div[1]/table/tbody/tr[6]/td/div/form/table/tbody/tr[3]/td/div/div/table/tbody/tr[3]/td/table/tbody/tr/td/table/tbody/tr[4]/td/table/tbody/tr/td/table/tbody/tr[2]/td[16]/input").click()
        except:
            print("7pm taken")

# replace 2022, 1, 9 with tomorrow's date
target = datetime.datetime(2022,1,15,6,0,0)

now = datetime.datetime.now()
delta = target - now
if delta > datetime.timedelta(0):
    time.sleep(delta.total_seconds())
    
driver.find_elements_by_class_name("button_wcag2")[1].click();

   
