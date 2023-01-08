from selenium import webdriver
from selenium.webdriver.common.by import By
from Test_Data import data
import pytest
import time

class Test_Prem:
    url = "https://opensource-demo.orangehrmlive.com"

    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Chrome()
        yield
        self.driver.close()

    def test_contact(self, booting_function):
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(5)
        self.driver.find_element(by=By.NAME, value=data.Prem_Selectors.input_box_username).send_keys(data.Prem_Data.username)
        self.driver.find_element(by=By.NAME, value=data.Prem_Selectors.input_box_password).send_keys(data.Prem_Data.password)
        self.driver.find_element(by=By.XPATH, value=data.Prem_Selectors.login_xpath).click()
        assert self.driver.title == 'OrangeHRM'
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.Prem_Selectors.pim_xpath).click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.Prem_Selectors.add_xpath).click()
        time.sleep(5)
        self.driver.find_element(by=By.NAME, value=data.Prem_Selectors.input_box_firstName).send_keys(data.Prem_Data.firstName)
        self.driver.find_element(by=By.NAME, value=data.Prem_Selectors.input_box_lastName).send_keys(data.Prem_Data.lastName)
        self.driver.find_element(by=By.XPATH, value=data.Prem_Selectors.save_xpath).click()
        time.sleep(8)
        self.driver.find_element(by=By.XPATH, value=data.Prem_Selectors.contactdetails_xpath).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=data.Prem_Selectors.street1_xpath).send_keys('16b')
        self.driver.find_element(by=By.XPATH, value=data.Prem_Selectors.street2_xpath).send_keys('T nagar')
        self.driver.find_element(by=By.XPATH, value=data.Prem_Selectors.city_xpath).send_keys('chennai')
        self.driver.find_element(by=By.XPATH, value=data.Prem_Selectors.state_xpath).send_keys('Tamilnadu')
        self.driver.find_element(by=By.XPATH, value=data.Prem_Selectors.postalcode_xpath).send_keys('600028')
        self.driver.find_element(by=By.XPATH, value=data.Prem_Selectors.Country_xpath).click
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.Prem_Selectors.india_xpath).click()
        self.driver.find_element(by=By.XPATH, value=data.Prem_Selectors.telephone_xpath).send_keys('04285-225664')
        self.driver.find_element(by=By.XPATH, value=data.Prem_Selectors.mobile_xpath).send_keys('9245698115')
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.Prem_Selectors.work_xpath).send_keys('-')
        self.driver.find_element(by=By.XPATH, value=data.Prem_Selectors.workemail_xpath).send_keys('kumargfhsn@gmail.com')
        self.driver.find_element(by=By.XPATH, value=data.Prem_Selectors.othermail_xpath).send_keys('kumar25a@gmail.com')
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.Prem_Selectors.Save_xpath).click()
        time.sleep(5)
        print("SUCCESSFULLY DONE COTACT DETAIL")