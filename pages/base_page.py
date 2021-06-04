#!/usr/bin/python3
from selenium import webdriver
browser = webdriver.Chrome()
class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self): 
        self.browser.get(self.url)



