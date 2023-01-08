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

    def test_login(self, booting_function):
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
        time.sleep(4)
        self.driver.find_element(by=By.XPATH, value=data.Prem_Selectors.createbutton_xpath).click()
        time.sleep(10)
        self.driver.find_element(by=By.XPATH, value=data.Prem_Selectors.Username_xpath).send_keys('Premkumar R')
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.Prem_Selectors.Password_xpath).send_keys('Premkumar@1')
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.Prem_Selectors.confirmpassword_xpath).send_keys('Premkumar@1')
        time.sleep(10)
        self.driver.find_element(by=By.XPATH, value=data.Prem_Selectors.save_xpath).click()
        time.sleep(15)
        print("SUCCESSFULLY CREAT LOGIN AND ADD EMPLOYEE")