# coding:utf-8
from selenium import webdriver
import time
import configparser
import os


class BaseWebdriver(object):

    def __init__(self):
        driver_path = os.path.dirname(os.path.dirname(__file__)) + '/DriverDir/chromedriver.exe'
        self.driver = webdriver.Chrome(driver_path)

    def get(self, url):
        return self.driver.get(url)

    def element(self, name):
        by_list = ["xpath", "link text", "partial link text", "name", "tag name", "class name", "css selector", "id"]
        for by in by_list:
            if self.driver.find_elements(by, name):
                print(by)
                return self.driver.find_element(by, name)


class ConfigParser(object):

    def __init__(self):
        self.config = configparser.ConfigParser()
        file_path = 'config.ini'
        self.config.read(file_path)

    def get_element(self, option):
        return self.config.get('Element', option)
        # string = self.config.get('element', option)
        # r = string.split('>')
        # print(r)

    def get_start_url(self, option):
        return self.config.get('Start_url', option)

    def get_user_info(self, option):
        return self.config.get('User', option)


conf = ConfigParser()
s = conf.get_user_info('username')
print(type(s))
