import pytest, requests, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


""" This class is the parent of all pages """
""" it contains all the generic methods and utilities for all the pages"""


class BasePage:
    """ By Locators - OB (Object Repository) """
    MENU_HAMBURGER = (By.XPATH, "/html/body/nav/div/button")
    """ constructor of the page class """
    def __init__(self, driver):
        self.driver = driver
    """ Page Action Methods for Base Page"""
    def do_click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def do_send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title

    def get_count_of_items(self, by_locator):
        return len(WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(by_locator)))

    def toggle_menu_hamburger(self):
        """this is used to toggler the hamburger menu if it exists"""
        try:
            self.do_click(self.MENU_HAMBURGER)
        except:
            pass