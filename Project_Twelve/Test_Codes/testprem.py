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


    def test_get_title(self, booting_function):
        self.driver.get(self.url)
        assert self.driver.title == 'OrangeHRM'
        print("SUCCESS")    

    def test_salary(self, booting_function):
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
        self.driver.find_element(by=By.XPATH, value=data.Prem_Selectors.salary_xpath).click()
        time.sleep(8)
        self.driver.find_element(by=By.XPATH, value=data.Prem_Selectors.addbutton_xpath).click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.Prem_Selectors.salarycomponent_xpath).send_keys('basic salary')
        self.driver.find_element(by=By.XPATH, value=data.Prem_Selectors.dropdown_xpath).click()
        time.sleep(5)
        e0=self.driver.find_element(by=By.XPATH, value=data.Prem_Selectors.selectinput_xpath)
        time.sleep(3)
        self.driver.execute_script('arguments[0].innerHTML = "Grade 3";',e0)
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.Prem_Selectors.dropdown2_xpath).click()
        time.sleep(3)
        e1=self.driver.find_element(by=By.XPATH, value=data.Prem_Selectors.selectinput2_xpath)
        self.driver.execute_script('arguments[0].innerHTML = "Monthly";',e1)
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.Prem_Selectors.currencydropdown_xpath).click()
        time.sleep(3)
        e2=self.driver.find_element(by=By.XPATH, value=data.Prem_Selectors.selectinput3_xpath)
        time.sleep(3)
        self.driver.execute_script('arguments[0].innerHTML = "United States Dollar";',e2)
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.Prem_Selectors.amount_xpath).send_keys('50000')
        self.driver.find_element(by=By.XPATH, value=data.Prem_Selectors.comments_xpath).send_keys('--')
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.Prem_Selectors.radiobutton_xpath).click()
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.Prem_Selectors.accountno_xpath).send_keys('122408956894')
        self.driver.find_element(by=By.XPATH, value=data.Prem_Selectors.ACtypedropdown_xpath).click()
        time.sleep(3)
        e3=self.driver.find_element(by=By.XPATH, value=data.Prem_Selectors.selectinput4_xpath)
        time.sleep(3)
        self.driver.execute_script('arguments[0].innerHTML = "Checking";',e3)
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.Prem_Selectors.routingnumber_xpath).send_keys('122408956')
        time.sleep(4)
        self.driver.find_element(by=By.XPATH, value=data.Prem_Selectors.Amount_xpath).send_keys('200000')
        time.sleep(5)
        self.driver.find_element(by=By.XPATH, value=data.Prem_Selectors.Savebutton_xpath).click()
        time.sleep(7)
        print("successfully updates the salary details")