import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from tests.locators import LoginPageLocators, MainPageLocators
from urls import Urls

class TestLogin:

    def test_successfull_login_through_main_page_login_button(self, driver, fixed_session_user):

        driver.get(Urls.MAIN_PAGE)

        driver.find_element(*MainPageLocators.MAIN_LOGIN_BUTTON).click()
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(fixed_session_user["email"])
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(fixed_session_user["password"])
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(MainPageLocators.MAIN_SECTION))

        assert Urls.MAIN_PAGE in driver.current_url

    def test_successfull_login_through_profile_button(self, driver, fixed_session_user):

        driver.get(Urls.MAIN_PAGE)
        
        driver.find_element(*MainPageLocators.PROFILE_BUTTON).click() 
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(fixed_session_user["email"])
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(fixed_session_user["password"])
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click() 

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(MainPageLocators.MAIN_SECTION))
        
        assert Urls.MAIN_PAGE in driver.current_url

    def test_successfull_login_through_button_on_registration_page(self, driver, fixed_session_user):

        driver.get(Urls.REGISTER_PAGE)

        driver.find_element(*LoginPageLocators.FORGOT_PASSWORD_LINK).click()
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(fixed_session_user["email"])
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(fixed_session_user["password"])
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click() 

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(MainPageLocators.MAIN_SECTION))
        
        assert Urls.MAIN_PAGE in driver.current_url

    def test_successfull_login_through_forgot_password_page(self, driver, fixed_session_user):

        driver.get(Urls.FORGOT_PASSWORD_PAGE)

        driver.find_element(*LoginPageLocators.FORGOT_PASSWORD_LINK).click()
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(fixed_session_user["email"])
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(fixed_session_user["password"])
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click() 

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(MainPageLocators.MAIN_SECTION))

        assert Urls.MAIN_PAGE in driver.current_url
