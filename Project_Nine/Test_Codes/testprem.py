from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from Test_Data import data
import pytest
import time

class Test_Hari:
    url = "https://opensource-demo.orangehrmlive.com"

    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Chrome()
        yield
        self.driver.close()

    def test_contract(self, booting_function):
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
        time.sleep(10)
        self.driver.find_element(by=By.XPATH, value=data.Prem_Selectors.job_xpath).click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.Prem_Selectors.joiningdate_xpath).send_keys('2019-05-16')
        time.sleep(5)

        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.Prem_Selectors.contractend_xpath).click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.Prem_Selectors.savebutton_xpath).click()
        time.sleep(5)
        print("SUCCESSFULLY FILL CONTRACT DEATAIL")