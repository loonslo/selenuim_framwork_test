from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time


def drivers():
    driver_path = os.path.dirname(os.path.dirname(__file__)) + '/DriverDir/chromedriver'
    driver = webdriver.Chrome(driver_path)
    return driver
