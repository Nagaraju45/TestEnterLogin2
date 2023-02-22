import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from base.base_driver_2 import BaseDriver
from utilities.utils import Utils


class LoginLaunchPage(BaseDriver):

    log = Utils.custom_logger()
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    TRY_IT_FREE = "//a[@aria-label='Start my free trial with Salesforce CRM']"
    FIRST_NAME_FIELD = "//input[starts-with(@id, 'UserFirstName')]"
    LAST_NAME_FIELD = "//input[contains(@id, 'Last')]"
    EMAIL_FIELD = "//input[@name='UserEmail']"
    JOB_TITLE_SELECT = "UserTitle"
    COMPANY_NAME_FIELD = "//input[@name='CompanyName']"
    COMPANY_EMPLOYEES_SELECT = "CompanyEmployees"
    PHONE_NO_FIELD = "//input[@name='UserPhone']"
    COUNT_COUNTRIES = "//select[starts-with(@id, 'CompanyCountry')]//option"
    COMPANY_COUNTRY_SELECT = "CompanyCountry"
    CHECK_BOX_CLICK = "//div[@class='msaCheckbox checkboxInput section']//div[@class='checkbox-ui']"
    LINK_CLICK = "//a[text()='Main Services Agreement']"
    CHECK_BOX_2_CLICK = "//div[@class='show']//div[@class='checkbox-ui']"

    def get_try_free(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.TRY_IT_FREE)
    def get_first_name(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.FIRST_NAME_FIELD)
    def get_last_name(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.LAST_NAME_FIELD)
    def get_email(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.EMAIL_FIELD)
    def get_job_title(self):
        return self.wait_until_element_is_clickable(By.NAME, self.JOB_TITLE_SELECT)
    def get_company_name(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.COMPANY_NAME_FIELD)
    def get_company_employees(self):
        return self.wait_until_element_is_clickable(By.NAME, self.COMPANY_EMPLOYEES_SELECT)
    def get_phone_no(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.PHONE_NO_FIELD)
    def get_count_countries(self):
        return self.wait_for_presence_of_all_elements(By.XPATH, self.COUNT_COUNTRIES)
    def get_company_country_select(self):
        return self.wait_until_element_is_clickable(By.NAME, self.COMPANY_COUNTRY_SELECT)
    def get_checkbox_click(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.CHECK_BOX_CLICK)
    def get_link_click(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.LINK_CLICK)
    def get_checkbox_2_click(self):
        return self.wait_until_element_is_clickable(By.XPATH, self.CHECK_BOX_2_CLICK)

    def click_try_it_free_button(self):
        self.get_try_free().click()
        parent_window = self.driver.current_window_handle
        all_han = self.driver.window_handles
        new_han = [x for x in all_han if x != parent_window][0]
        self.driver.switch_to.window(parent_window)
        # self.driver.close()
        self.driver.switch_to.window(new_han)

    def enter_first_name(self, first_name):
        # first_name = self.driver.find_element(By.XPATH, "//input[starts-with(@id, 'UserFirstName')]")
        self.get_first_name().click()
        self.get_first_name().send_keys(first_name)
        self.get_first_name().send_keys(Keys.TAB)
        self.log.info("First Name Completed")
    def enter_last_name(self, last_name):
        # last_name = self.driver.find_element('xpath', "//input[contains(@id, 'Last')]")
        self.get_last_name().click()
        self.get_last_name().send_keys(last_name)
        self.get_last_name().send_keys(Keys.TAB)
        self.log.info("Last Name Completed")
    def enter_email(self, email):
        # e_mail = self.driver.find_element('xpath', "//input[@name='UserEmail']")
        self.get_email().click()
        self.get_email().send_keys(email)
        self.get_email().send_keys(Keys.TAB)
        self.log.info("Email Completed")
    def select_job_title(self, job_title2):
        # job_title = self.driver.find_element('name', "UserTitle")
        job_title = self.get_job_title()
        sel_title = Select(job_title)
        sel_title.select_by_visible_text(job_title2)
        job_title.send_keys(Keys.TAB)
        self.log.info("Job Title Selected")
    def enter_company_name(self, company_name):
        # company_name = self.driver.find_element('xpath', "//input[@name='CompanyName']")
        self.get_company_name().click()
        self.get_company_name().send_keys(company_name)
        self.get_company_name().send_keys(Keys.TAB)
        self.log.info("Company Name Completed")
    def select_company_employees(self, no_of_emp):
        # company_emp = self.driver.find_element('name', "CompanyEmployees")
        company_emp = self.get_company_employees()
        com_emp = Select(company_emp)
        # com_emp.select_by_value(no_of_employees)
        no_of_employees = int(no_of_emp)
        if no_of_employees <= 9:
            com_emp.select_by_value("9")
        elif no_of_employees > 15 and no_of_employees <= 100:
            com_emp.select_by_value("75")
        elif no_of_employees > 100 and no_of_employees <= 500:
            com_emp.select_by_value("250")
        elif no_of_employees > 500 and no_of_employees <= 1500:
            com_emp.select_by_value("950")
        else:
            com_emp.select_by_value("1600")
        company_emp.send_keys(Keys.TAB)
        self.log.info("Employees Selected")
    def enter_phone_no(self, phone_no):
        # user_phone_no = self.driver.find_element('xpath', "//input[@name='UserPhone']")
        self.get_phone_no().click()
        self.get_phone_no().send_keys(phone_no)
        self.get_phone_no().send_keys(Keys.TAB)
        self.log.info("Phone No. Completed")
    def total_no_of_countries(self):
        # no_of_countries = self.driver.find_elements('xpath', "//select[starts-with(@id, 'CompanyCountry')]//option")
        no_of_countries = self.get_count_countries()
        print("\nTotal Countries:", len(no_of_countries))
    def select_company_country(self, country):
        # com_country = self.driver.find_element('name', "CompanyCountry")
        com_country = self.get_company_country_select()
        select_country = Select(com_country)
        select_country.select_by_visible_text(country)
        self.log.info("Country Selected")
    def click_check_box(self):
        # check_box = self.driver.find_element('xpath', "//div[@class='msaCheckbox checkboxInput section']//div[@class='checkbox-ui']")
        check_box = self.get_checkbox_click()
        check_box.click()
        self.log.info("First Checkbox Completed")
    def click_link(self):
        # all_windows = self.driver.window_handles
        parent_window = self.driver.current_window_handle
        # click_link = self.driver.find_element('xpath', "//a[text()='Main Services Agreement']")
        click_link = self.get_link_click()
        click_link.click()
        time.sleep(3)
        # for handle in all_windows:
        #     if handle != parent_window:
        #         time.sleep(2)
        #           self.driver.switch_to.window()
        #         self.driver.close()
        all_han = self.driver.window_handles
        new_han = [x for x in all_han if x != parent_window][0]
        self.driver.switch_to.window(new_han)
        self.driver.close()
        self.driver.switch_to.window(parent_window)
        time.sleep(2)
        self.log.info("Click Link Completed")

    def click_check_box_2(self):
        # check_box2 = self.driver.find_element("xpath", "//div[@class='show']//div[@class='checkbox-ui']")
        check_box2 = self.get_checkbox_2_click()
        check_box2.click()
        time.sleep(3)
        self.log.info("Second Checkbox Completed")

    def enter_data_to_fields(self, f_n, l_n, email, job_title, com_name, no_of_com_emp, ph_no, com_country):
        self.click_try_it_free_button()
        self.enter_first_name(f_n)
        self.enter_last_name(l_n)
        self.enter_email(email)
        self.select_job_title(job_title)
        self.enter_company_name(com_name)
        self.select_company_employees(no_of_com_emp)
        self.enter_phone_no(ph_no)
        self.total_no_of_countries()
        self.select_company_country(com_country)
        if com_country == "India":
            self.click_check_box()
            self.click_link()
        else:
            self.click_check_box()
            self.click_link()
            self.click_check_box_2()
        self.log.info("Successfully done...")

