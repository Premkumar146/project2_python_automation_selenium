from selenium import webdriver
from selenium.webdriver.common.by import By
from Test_Data import data
import pytest
import time

class Test_Prem:
    url = "https://opensource-demo.orangehrmlive.com"
    
    # Booting Method for running the Python Tests
    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Chrome()
        yield
        self.driver.close()
    
    def test_get_title(self, booting_function):
        self.driver.get(self.url)
        assert self.driver.title == 'OrangeHRM'
        print("SUCCESS")
    
    def test_userstatus(self, booting_function):
        self.driver.get(self.url)
        time.sleep(5)
        self.driver.find_element(by=By.NAME, value=data.Prem_Selectors.input_box_username).send_keys(data.Prem_Data.username)
        self.driver.find_element(by=By.NAME, value=data.Prem_Selectors.input_box_password).send_keys(data.Prem_Data.password)
        self.driver.find_element(by=By.XPATH, value=data.Prem_Selectors.login_xpath).click()
        time.sleep(3)
        assert self.driver.title == 'OrangeHRM'
        self.driver.find_element(by=By.XPATH, value=data.Prem_Selectors.admin_xpath).click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.Prem_Selectors.name_xpath).send_keys('premKumarr')
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.Prem_Selectors.dropdown_xpath).click()
        time.sleep(5)
        element1=self.driver.find_element(by=By.XPATH, value=data.Prem_Selectors.dropadmin_xpath)
        time.sleep(3)
        self.driver.execute_script('arguments[0].innerHTML = "Admin";',element1)
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.Prem_Selectors.hint_xpath).send_keys('premk')
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.Prem_Selectors.dropstuts_xpath).click()
        time.sleep(3)
        element2=self.driver.find_element(by=By.XPATH, value=data.Prem_Selectors.dropenable_xpath)
        time.sleep(3)
        self.driver.execute_script('arguments[0].innerHTML = "Enabled";',element2)
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.Prem_Selectors.dropdown_xpath).click()
        time.sleep(5)
        element3=self.driver.find_element(by=By.XPATH, value=data.Prem_Selectors.dropess_xpath)
        time.sleep(3)
        self.driver.execute_script('arguments[0].innerHTML = "ESS";',element3)
        self.driver.find_element(by=By.XPATH, value=data.Prem_Selectors.dropstuts_xpath)
        time.sleep(5)
        element4=self.driver.find_element(by=By.XPATH, value=data.Prem_Selectors.dropdisable_xpath)
        time.sleep(3)
        self.driver.execute_script('arguments[0].innerHTML = "Disabled";',element4)
        time.sleep(4)
        self.driver.find_element(by=By.XPATH, value=data.Prem_Selectors.search_xpath).click()
        time.sleep(6)
        print("SUCCESSFULLY DONE USERROLE AND STATUS")

