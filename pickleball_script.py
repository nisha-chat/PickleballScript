
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
from datetime import datetime

# put fill file path to chromedriver
driver = webdriver.Chrome("/Users/insert_laptop_username/Desktop/chromedriver")

driver.get('https://apm.activecommunities.com/citymb/ActiveNet_Home/makeOnlineQuickReservation.sdi')
driver.maximize_window()

username = driver.find_element_by_id("ctl05_ctlLoginLayout_txtUserName")
password = driver.find_element_by_id("ctl05_ctlLoginLayout_txtPassword")

# replace username with your username and password with your password
username.send_keys("put your username here")
password.send_keys("put your password password here")

driver.find_element_by_id("ctl05_ctlLoginLayout_btnLogin").click()
driver.implicitly_wait(5)

driver.execute_script("window.scrollTo(0, 1500)")
driver.implicitly_wait(5)
select = Select(driver.find_element_by_id('facilitygroup_id'))

select.select_by_visible_text('MH Pickleball ONLY')

select = Select(driver.find_element_by_id('begd'))
# replace 10 with the date in 4 days (tomorrow is the 6th so we put the 10th)
select.select_by_visible_text('10')

driver.find_element_by_class_name("button_wcag2").click();

driver.execute_script("window.scrollTo(0, 1500)")

participants = driver.find_element_by_xpath('//*[@id="availability_bodyhtml"]/table/tbody/tr[4]/td/table/tbody/tr/td/table/tbody/tr[2]/td[3]/input')
participants.send_keys("1")


participants = driver.find_element_by_name("aci_19392")
participants.send_keys("NC")


# try:
#     driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[3]/div[1]/table/tbody/tr[6]/td/div/form/table/tbody/tr[3]/td/div/div/table/tbody/tr[3]/td/table/tbody/tr/td/table/tbody/tr[4]/td/table/tbody/tr/td/table/tbody/tr[2]/td[5]/input").click()
# except:
#     print("8am taken")

# try:
#     driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[3]/div[1]/table/tbody/tr[6]/td/div/form/table/tbody/tr[3]/td/div/div/table/tbody/tr[3]/td/table/tbody/tr/td/table/tbody/tr[4]/td/table/tbody/tr/td/table/tbody/tr[2]/td[6]/input").click()
# except:
#     print("9am taken")

# try:
#     driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[3]/div[1]/table/tbody/tr[6]/td/div/form/table/tbody/tr[3]/td/div/div/table/tbody/tr[3]/td/table/tbody/tr/td/table/tbody/tr[4]/td/table/tbody/tr/td/table/tbody/tr[2]/td[7]/input").click()
# except:
#     print("10am taken")

# try:
#     driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[3]/div[1]/table/tbody/tr[6]/td/div/form/table/tbody/tr[3]/td/div/div/table/tbody/tr[3]/td/table/tbody/tr/td/table/tbody/tr[4]/td/table/tbody/tr/td/table/tbody/tr[2]/td[8]/input").click()
# except:
#     print("11am taken")

try:
    driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[3]/div[1]/table/tbody/tr[6]/td/div/form/table/tbody/tr[3]/td/div/div/table/tbody/tr[3]/td/table/tbody/tr/td/table/tbody/tr[4]/td/table/tbody/tr/td/table/tbody/tr[2]/td[9]/input").click();
except:
    print("12pm taken")
    try:
        driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[3]/div[1]/table/tbody/tr[6]/td/div/form/table/tbody/tr[3]/td/div/div/table/tbody/tr[3]/td/table/tbody/tr/td/table/tbody/tr[4]/td/table/tbody/tr/td/table/tbody/tr[2]/td[10]/input").click()
    except:
        print("1pm taken")
        try:
            driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[3]/div[1]/table/tbody/tr[6]/td/div/form/table/tbody/tr[3]/td/div/div/table/tbody/tr[3]/td/table/tbody/tr/td/table/tbody/tr[4]/td/table/tbody/tr/td/table/tbody/tr[2]/td[11]/input").click()
        except:
            print("2pm taken")
                try:
                    driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[3]/div[1]/table/tbody/tr[6]/td/div/form/table/tbody/tr[3]/td/div/div/table/tbody/tr[3]/td/table/tbody/tr/td/table/tbody/tr[4]/td/table/tbody/tr/td/table/tbody/tr[2]/td[12]/input").click()
                except:
                    print("3pm taken")
                    try:
                        driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[3]/div[1]/table/tbody/tr[6]/td/div/form/table/tbody/tr[3]/td/div/div/table/tbody/tr[3]/td/table/tbody/tr/td/table/tbody/tr[4]/td/table/tbody/tr/td/table/tbody/tr[2]/td[13]/input").click()
                    except:
                        print("4pm taken")
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
                                    try:
                                        select = Select(driver.find_element_by_id('facilitygroup_id'))
                                        select.select_by_visible_text('MH Paddleball/Pickleball Court')
                                        select = Select(driver.find_element_by_id('begd'))
                                        select.select_by_visible_text('10')
                                        driver.find_element_by_class_name("button_wcag2").click();
                                        driver.execute_script("window.scrollTo(0, 1500)")
                                        participants = driver.find_element_by_xpath('//*[@id="availability_bodyhtml"]/table/tbody/tr[4]/td/table/tbody/tr/td/table/tbody/tr[2]/td[3]/input')
                                        participants.send_keys("1")
                                        participants = driver.find_element_by_name("aci_19392")
                                        participants.send_keys("NC")
                                        try:
                                            driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[3]/div[1]/table/tbody/tr[6]/td/div/form/table/tbody/tr[3]/td/div/div/table/tbody/tr[3]/td/table/tbody/tr/td/table/tbody/tr[4]/td/table/tbody/tr/td/table/tbody/tr[2]/td[9]/input").click();
                                        except:
                                            print("12pm taken")
                                            try:
                                                driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[3]/div[1]/table/tbody/tr[6]/td/div/form/table/tbody/tr[3]/td/div/div/table/tbody/tr[3]/td/table/tbody/tr/td/table/tbody/tr[4]/td/table/tbody/tr/td/table/tbody/tr[2]/td[10]/input").click()
                                            except:
                                                print("1pm taken")
                                                try:
                                                    driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[3]/div[1]/table/tbody/tr[6]/td/div/form/table/tbody/tr[3]/td/div/div/table/tbody/tr[3]/td/table/tbody/tr/td/table/tbody/tr[4]/td/table/tbody/tr/td/table/tbody/tr[2]/td[11]/input").click()
                                                except:
                                                    print("2pm taken")
                                                        try:
                                                            driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[3]/div[1]/table/tbody/tr[6]/td/div/form/table/tbody/tr[3]/td/div/div/table/tbody/tr[3]/td/table/tbody/tr/td/table/tbody/tr[4]/td/table/tbody/tr/td/table/tbody/tr[2]/td[12]/input").click()
                                                        except:
                                                            print("3pm taken")
                                                            try:
                                                                driver.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[3]/div[1]/table/tbody/tr[6]/td/div/form/table/tbody/tr[3]/td/div/div/table/tbody/tr[3]/td/table/tbody/tr/td/table/tbody/tr[4]/td/table/tbody/tr/td/table/tbody/tr[2]/td[13]/input").click()
                                                            except:
                                                                print("4pm taken")
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

# replace middle two numbers with tomorrow morning's month and day (respectively)
pause.until(datetime(2022, 1, 6, 6))
driver.find_elements_by_class_name("button_wcag2")[1].click();





   