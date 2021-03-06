# encoding:utf-8
import configparser
import os

from selenium import webdriver
from datetime import datetime


class BaseWebdriver(object):

    def __init__(self):
        self.by_list = ["xpath", "link text", "partial link text", "name", "tag name", "class name", "css selector",
                        "id"]
        driver_path = os.path.dirname(os.path.dirname(__file__)) + '/DriverDir/chromedriver'
        self.driver = webdriver.Chrome(driver_path)

    def get(self, url):
        return self.driver.get(url)

    def element(self, name):
        for by in self.by_list:
            if self.driver.find_elements(by, name):
                return self.driver.find_element(by, name)

    def is_exist(self, name):
        ele_list = [self.driver.find_elements(i, name) for i in self.by_list]
        for i in ele_list:
            if len(i) > 0:
                return True
        return False

    def get_screenshot(self):
        time = datetime.now().strftime('%Y%m%d%H%M%S')
        self.driver.save_screenshot(time + '.png')


class ConfigParser(object):

    def __init__(self):
        self.config = configparser.ConfigParser()
        file_path = 'config.ini'
        self.config.read(file_path)

    def get_element(self, option):
        return self.config.get('Element', option)

    def get_start_url(self, option):
        return self.config.get('Start_url', option)

    def get_user_info(self, option):
        return self.config.get('User', option)
