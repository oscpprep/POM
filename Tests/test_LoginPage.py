from Config.config import TestData
from Tests.test_base import BaseTest
from Pages.LoginPage import LoginPage


class Test_Login(BaseTest):

    def test_register_link_visible(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.toggle_menu_hamburger()
        flag = self.loginPage.does_register_link_exist()
        assert flag

    def test_login_page_title(self):
        self.loginPage = LoginPage(self.driver)
        title = self.loginPage.get_title(TestData.PAGE_TITLE)
        assert title == TestData.PAGE_TITLE

    def test_login(self):
        self.loginPage = LoginPage(self.driver)
        self.loginPage.toggle_menu_hamburger()
        self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)


