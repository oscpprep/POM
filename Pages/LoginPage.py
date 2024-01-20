from Config.config import TestData
from Pages.BasePage import *
from Pages.HomePage import HomePage


class LoginPage(BasePage):
    """ By Locators - OB (Object Repository) """
    EMAIL = (By.ID, "email")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "log_in")
    LOGIN_LINK = (By.XPATH, '//*[@id="navbarResponsive"]/ul/li[2]/a')
    SIGNUP_BUTTON = (By.ID, "sign_up")
    REGISTER_LINK = (By.XPATH, '//*[@id="navbarResponsive"]/ul/li[3]/a')
    LOGOUT_LINK = (By.XPATH, "/html/body/nav/div/div/ul/li[2]/a")

    """ constructor of the page class """

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    """ Page Action Methods for Log In Page"""

    def get_login_page_title(self, title):
        """this is used to get the page tite"""
        return self.get_title(title)

    def does_logout_button_exist(self):
        """this is used to check if logout button for successful login"""
        return self.is_visible(self.LOGOUT_LINK)

    def does_register_link_exist(self):
        """this is used to check sign up link"""
        return self.is_visible(self.REGISTER_LINK)

    def do_login(self, username, password):
        """this is used to log in to the blog app"""
        self.do_click(self.LOGIN_LINK)
        self.do_send_keys(self.EMAIL, username)
        self.do_send_keys(self.PASSWORD, password)
        self.do_click(self.LOGIN_BUTTON)
        return HomePage(self.driver)

    def do_logout(self):
        try:
            self.do_click(self.LOGOUT_LINK)
            self.driver.get(TestData.BASE_URL + "/logout")
            success_logout = True
        except:
            success_logout = False
            pass
        return success_logout

