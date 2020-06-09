from selenium import webdriver
import os
import time

from selenium.webdriver.common.by import By

from LoginModule.base import drivers


#
# def element(name):
#     if driver.find_element_by_class_name(name):
#         return driver.find_element_by_class_name(name)
#     elif driver.find_element_by_xpath(name):
#         print(222)
#         return driver.find_element_by_xpath(name)

def element(name):
    # by_list = ['By.ID', 'By.CLASS_NAME']
    f = driver.find_elements(By.CLASS_NAME,name)
    print(f)


driver = drivers()
driver.get('https://www.csdn.net/')

element('userinfo')

# time.sleep(2)
# element('//*[@id="app"]/div/div/div[1]/div[2]/div[5]/ul/li[2]/a')

# driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div[2]/div[5]/ul/li[2]/a').click()
# print(driver)
# driver.find_element_by_name('all').send_keys('chongqing115@126.com')
# driver.find_element_by_name('pwd').send_keys('123qweasdzxc')
# driver.find_element_by_xpath('//*[@id="app"]/div/div/div[1]/div[2]/div[5]/div/div[6]/div/button').click()
