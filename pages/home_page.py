import time
from selenium.webdriver.common.by import By
from locators.home_page import HomePageLocators
from base.page_base import PageBase
import random
from dotenv import dotenv_values

config = dotenv_values('.env')


class HomePage(PageBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.homepagelocators = HomePageLocators()

    def get_account_headers(self):
        self.click_element(self.homepagelocators.accounts)
        headers = self.find_elements(self.homepagelocators.account_table_headers)
        headers_value = []
        for i in headers:
            headers_value.append(i.text)
        return headers_value

    def get_service_title(self):
        service = self.get_text_from_element(self.homepagelocators.services_title)
        return service

    def get_invoice_title(self):
        invoice = self.get_text_from_element(self.homepagelocators.invoice_title)
        return invoice

    def get_equipment_title(self):
        equipment = self.get_text_from_element(self.homepagelocators.equipment_title)
        return equipment

    def get_dashboard_title(self):
        dashboard_title = self.get_text_from_element(self.homepagelocators.dashboard_button)
        return dashboard_title

    def get_user_settings_table_headers(self):
        headers = self.find_elements(self.homepagelocators.user_settings_table_headers)
        headers_value = []
        for i in headers:
            headers_value.append(i.text)
        return headers_value

    def click_user_settings(self):
        time.sleep(5)
        self.click_element(self.homepagelocators.settings_arrow)
        self.click_element(self.homepagelocators.user_settings_button)

    def get_default_service_history_date_range_title(self):
        default_date_range_title = self.get_text_from_element(
            self.homepagelocators.default_service_history_date_range_title)
        return default_date_range_title

    def get_default_invoice_history_date_range_title(self):

        default_date_range_title = self.get_text_from_element(
            self.homepagelocators.default_invoice_history_date_range_title)
        return default_date_range_title

    def verify_success_message(self):
        time.sleep(3)
        success_message = self.get_text_from_element(self.homepagelocators.success_message)
        return success_message

    def enter_old_password(self, oldpassword):
        return self.send_keys_to_element(self.homepagelocators.old_password, oldpassword)

    def enter_new_password(self, newpassword):
        return self.send_keys_to_element(self.homepagelocators.new_password, newpassword)

    def enter_verify_password(self, verifypassword):
        return self.send_keys_to_element(self.homepagelocators.verify_password, verifypassword)

    def click_edit_password(self):
        self.click_element(self.homepagelocators.pssword_edit)

    def enter_password_values(self, oldpassword, newpassword, verifypassword):
        time.sleep(10)
        self.click_element(self.homepagelocators.pssword_edit)
        self.enter_old_password(oldpassword)
        time.sleep(4)
        self.enter_new_password(newpassword)
        time.sleep(4)
        self.enter_verify_password(verifypassword)
        time.sleep(4)
        self.click_element(self.homepagelocators.save_edit_password)

    def select_account(self, account_name):
        self.click_element(self.homepagelocators.accounts)
        time.sleep(3)
        self.click_element(self.homepagelocators.all_Accounts_Checkbox)
        time.sleep(3)
        self.click_element(self.homepagelocators.account_check_box.replace("<<account_name>>", account_name))
        self.click_element(self.homepagelocators.done_Accounts_button)
        time.sleep(3)

    def click_title_card(self, title_name):
        self.click_element(self.homepagelocators.title_card.replace("<<title_name>>", title_name))

    def select_account_type(self):
        time.sleep(5)
        self.click_element(self.homepagelocators.edit_contact_information)
        time.sleep(5)
        self.click_element(self.homepagelocators.account_type_arrow)
        time.sleep(5)
        self.click_element(self.homepagelocators.select_account_type)

    def edit_login_email(self, login_email):
        text_box = self.find_element(self.homepagelocators.edit_login_email)
        text_box.clear()
        self.send_keys_to_element(self.homepagelocators.edit_login_email, login_email)
        return login_email

    def edit_contact_email(self, contact_email):
        text_box = self.find_element(self.homepagelocators.edit_contact_email)
        text_box.clear()
        self.send_keys_to_element(self.homepagelocators.edit_contact_email, contact_email)
        return contact_email

    def edit_first_name(self, first_name):
        text_box = self.find_element(self.homepagelocators.edit_first_name)
        text_box.clear()
        self.send_keys_to_element(self.homepagelocators.edit_first_name, first_name)
        return first_name

    def edit_last_name(self, last_name):
        text_box = self.find_element(self.homepagelocators.edit_last_name)
        text_box.clear()
        self.send_keys_to_element(self.homepagelocators.edit_last_name, last_name)
        return last_name

    def edit_phone_number(self, phone_number):
        text_box = self.find_element(self.homepagelocators.edit_phone_number)
        text_box.clear()
        self.send_keys_to_element(self.homepagelocators.edit_phone_number, phone_number)
        return phone_number

    def edit_company_address(self, company_address):
        text_box = self.find_element(self.homepagelocators.edit_company_address)
        text_box.clear()
        self.send_keys_to_element(self.homepagelocators.edit_company_address, company_address)
        return company_address

    def edit_address_2(self, address_2):
        text_box = self.find_element(self.homepagelocators.edit_address_2)
        text_box.clear()
        self.send_keys_to_element(self.homepagelocators.edit_address_2, address_2)
        return address_2

    def edit_city(self, city):
        text_box = self.find_element(self.homepagelocators.edit_city)
        text_box.clear()
        self.send_keys_to_element(self.homepagelocators.edit_city, city)
        return city

    def edit_state(self, state):
        text_box = self.find_element(self.homepagelocators.edit_state)
        text_box.clear()
        self.send_keys_to_element(self.homepagelocators.edit_state, state)
        return state

    def edit_zip_code(self, zip_code):
        text_box = self.find_element(self.homepagelocators.edit_zip_code)
        text_box.clear()
        self.send_keys_to_element(self.homepagelocators.edit_zip_code, zip_code)
        return zip_code

    def click_save_button(self):
        self.click_element(self.homepagelocators.save_contact_information_button)

    def get_contact_information(self, contact_info_title):
        contact_info = self.get_text_from_element(
            self.homepagelocators.contact_information.replace("<<contact_info_title>>", contact_info_title))
        return contact_info

    def get_account_list(self):
        self.click_element(self.homepagelocators.account_bar_click)
        time.sleep(5)
        self.find_element(self.homepagelocators.accounts_table)
        column_index = 2
        column_xpath = f"//table[@id='account_tbl35']//tbody//tr/td[{column_index}]"
        column_elements = self.driver.find_elements(By.XPATH, column_xpath)
        column_data = [element.text for element in column_elements]
        print(column_data)
        random_acc_no = random.choice(column_data)
        print(random_acc_no)
        self.click_element(self.homepagelocators.done_Accounts_button)
        return random_acc_no

    def get_account_name_list(self):
        self.click_element(self.homepagelocators.account_bar_click)
        time.sleep(5)
        self.find_element(self.homepagelocators.accounts_table)
        column_index_1 = 3
        column_xpath = f"//table[@id='account_tbl35']//tbody//tr/td[{column_index_1}]"
        column_elements_1 = self.driver.find_elements(By.XPATH, column_xpath)
        column_data_1 = [element.text for element in column_elements_1]
        print(column_data_1)
        random_acc_name = random.choice(column_data_1)
        print(random_acc_name)
        self.click_element(self.homepagelocators.done_Accounts_button)
        return random_acc_name

    def select_random_account_checkbox(self):
        time.sleep(3)
        self.click_element(self.homepagelocators.accounts)
        self.find_element(self.homepagelocators.account_table_body)
        time.sleep(3)
        select_all_check_box = self.find_element(self.homepagelocators.all_Accounts_Checkbox_enable)
        if select_all_check_box.is_selected():
            print("select all check box is checked")
            self.click_element(self.homepagelocators.all_Accounts_Checkbox)
            time.sleep(3)
            check_box = self.find_elements(self.homepagelocators.accounts_table_checkboxes)
            time.sleep(3)
            select_random_account = random.choice(check_box)
            select_random_account.click()
            self.click_element(self.homepagelocators.done_Accounts_button)

        else:
            print("select all is unchecked")
            self.click_element(self.homepagelocators.all_Accounts_Checkbox)
            self.click_element(self.homepagelocators.all_Accounts_Checkbox)
            time.sleep(3)
            check_box = self.find_elements(self.homepagelocators.accounts_table_checkboxes)
            time.sleep(3)
            select_random_account = random.choice(check_box)
            select_random_account.click()
            self.click_element(self.homepagelocators.done_Accounts_button)
