from Config.config import TestData
from Pages.BasePage import *


class HomePage(BasePage):
    """ By Locators - OB (Object Repository) """
    HEADER_TEXT = (By.XPATH, "//div[contains(@class, 'heading')]/h1")
    HAMBURGER_BUTTONS = (By.XPATH, '//ul//li[@class="nav-item"]')
    CREATE_POST_BUTTON = (By.XPATH, "//a[@class='btn btn-primary float-right' and @href='/new-post']")

    """ constructor of the page class """

    def __init__(self, driver):
        super().__init__(driver)
        driver.get(TestData.BASE_URL)

    """ Page Action Methods for Home Page"""

    def get_homepage_title(self, title):
        """this is used to get the page tite"""
        return self.get_title(title)

    def count_of_hamburger_buttons(self):
        """this is used to get a count of the hamburger buttons"""
        return self.get_count_of_items(self.HAMBURGER_BUTTONS)

    def get_header_value(self):
        """this is used to get the home page header title value"""
        if self.is_visible(self.HEADER_TEXT):
            return self.get_element_text(self.HEADER_TEXT)

    def click_create_post_button(self):
        self.do_click(self.CREATE_POST_BUTTON)


