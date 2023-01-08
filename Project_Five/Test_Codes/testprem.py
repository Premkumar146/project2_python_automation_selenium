from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
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

    def test_personal(self, booting_function):
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
        self.driver.find_element(by=By.XPATH, value=data.Prem_Selectors.nickname_xpath).send_keys('ajith')
        self.driver.find_element(by=By.XPATH, value=data.Prem_Selectors.otherid_xpath).send_keys('0982')
        self.driver.find_element(by=By.XPATH, value=data.Prem_Selectors.dirverlicense_xpath).send_keys('TN38Z501906586')
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.Prem_Selectors.licenseexpiry_xpath).send_keys('2026-05-11')
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=data.Prem_Selectors.ssnnumber_xpath).send_keys('nil')
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=data.Prem_Selectors.sinnumber_xpath).send_keys('nil')
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=data.Prem_Selectors.nationality_xpath).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=data.Prem_Selectors.indian_xpath).send_keys('Indian')
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=data.Prem_Selectors.dob_xpath).send_keys('1997-05-11')
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=data.Prem_Selectors.gender_xpath).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=data.Prem_Selectors.military_xpath).send_keys('No')
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=data.Prem_Selectors.saveI_xpath).click()
        time.sleep(10)
        print("SUCCESSFULLY DONE PERSONAL DETAILS")