# coding:utf-8
import time

from LoginModule.base import BaseWebdriver, ConfigParser

driver = BaseWebdriver()
config = ConfigParser()
driver.get(config.get_start_url('start_url'))
driver.element(config.get_element('login_index')).click()
time.sleep(2)
driver.element(config.get_element('account_button')).click()
driver.element(config.get_element('user_name')).send_keys(config.get_user_info('username'))
driver.element(config.get_element('user_pass')).send_keys(config.get_user_info('password'))

print(config.get_element('login_button'))
# driver.element(ConfigParser().get_element('login_button')).click()
print(type('//button[text()="登录"]'))
driver.element('//button[text()="登录"]').click()


