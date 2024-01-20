from Config.config import TestData
from Pages.HomePage import HomePage
from Tests.test_base import BaseTest
from Pages.LoginPage import LoginPage
import time


class Test_Home(BaseTest):

    def test_create_new_post(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.toggle_menu_hamburger()
        homePage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        homePage.click_create_post_button()
        flag = homePage.get_header_value() == TestData.CREATE_NEW_POST_HEADER
        self.loginPage.do_logout()
        assert flag

    def test_homepage_after_admin_login(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.toggle_menu_hamburger()
        homePage = self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        flag = homePage.is_visible(homePage.CREATE_POST_BUTTON)
        self.loginPage.do_logout()
        assert flag

    def test_5_hamburger_buttons(self):
        homePage = HomePage(self.driver)
        homePage.toggle_menu_hamburger()
        homePage.toggle_menu_hamburger()
        counts = homePage.count_of_hamburger_buttons()
        assert counts in TestData.COUNT_OF_HAMBURGER_BUTTONS

    def test_header_with_title(self):
        homePage = HomePage(self.driver)
        a = TestData.PAGE_TITLE
        b = homePage.get_homepage_title(a)
        c = homePage.get_header_value()
        assert a == b == c


