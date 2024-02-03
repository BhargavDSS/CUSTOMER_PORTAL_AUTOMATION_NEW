import time
from locators.login_page import LogInPageLocators
from base.page_base import PageBase


class LogInPage(PageBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.loginpagelocators = LogInPageLocators()

    def enter_user_name(self, username):
        time.sleep(3)
        enter_username = self.send_keys_to_element(self.loginpagelocators.email, username)
        first_name = username.split(".")[0]
        last_name = username.split(".")[1].split("@")[0]
        # username_value = last_name.capitalize() + " " + first_name.capitalize()
        return first_name.capitalize(), enter_username

    def enter_password(self, password):
        return self.send_keys_to_element(self.loginpagelocators.password, password)

    def click_on_login_button(self):
        return self.click_element(self.loginpagelocators.login_button)

    def enter_credentials(self, username, password):
        username = self.enter_user_name(username)
        self.enter_password(password)
        return username

    def verify_login_title(self):
        title = self.is_element_present(self.loginpagelocators.login_title)
        title_value = self.get_text_from_element(self.loginpagelocators.login_title)
        return title, title_value

    def verify_logged_in_user(self):
        username = self.is_element_present(self.loginpagelocators.username)
        username_value = self.get_text_from_element(self.loginpagelocators.username)
        return username, username_value

    def verifyloginfailed(self):
        try_again = self.is_element_present(self.loginpagelocators.try_again_button)
        request_account = self.is_element_present(self.loginpagelocators.request_account_button)
        return try_again, request_account

    def get_first_name(self):
        username = self.get_text_from_element(self.loginpagelocators.first_name)
        first_name = username.split(" ")[0]
        return first_name

    def logout(self):
        self.click_element(self.loginpagelocators.settings_arrow)
        self.click_element(self.loginpagelocators.logOut)
