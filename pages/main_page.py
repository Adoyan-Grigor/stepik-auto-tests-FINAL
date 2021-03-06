#!/usr/bin/python3
from .base_page import BasePage
from selenium.webdriver.common.by import By

class MainPage(BasePage): 
    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()
    def should_be_login_link(self):
        self.browser.find_element(By.CSS_SELECTOR, "#login_link_invalid")
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True
    def should_be_login_link(self):
        assert self.is_element_present(By.CSS_SELECTOR, "#login_link_invalid"), "Login link is not presented"

