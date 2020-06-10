# encoding:utf-8
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

driver.element('//button[text()="登录"]').click()
time.sleep(3)
if driver.is_exist(config.get_element('alert-title')):
    print('验证通过')
else:
    driver.get_screenshot()
    print('验证失败')
