import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from tests.locators import MainPageLocators, ProfilePageLocator, LoginPageLocators
from urls import Urls


class TestProfile:

    def test_click_on_profile_redirects_to_user_profile(self, driver, authorization): 

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(MainPageLocators.MAIN_HEADER))
        driver.find_element(*MainPageLocators.PROFILE_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(ProfilePageLocator.LOGOUT_BUTTON))

        assert Urls.PROFILE_PAGE in driver.current_url
        
    def test_click_constructor_redirects_to_main(self, driver, authorization):

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(MainPageLocators.MAIN_HEADER))
        driver.find_element(*MainPageLocators.PROFILE_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(ProfilePageLocator.LOGOUT_BUTTON))
        driver.find_element(*MainPageLocators.CONSTRUCTOR_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(MainPageLocators.MAIN_HEADER))

        assert Urls.MAIN_PAGE in driver.current_url

    def test_click_logo_redirect_to_main(self, driver, authorization):

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(MainPageLocators.MAIN_HEADER))
        driver.find_element(*MainPageLocators.PROFILE_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(ProfilePageLocator.LOGOUT_BUTTON))
        driver.find_element(*MainPageLocators.LOGO_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(MainPageLocators.MAIN_HEADER))

        assert Urls.MAIN_PAGE in driver.current_url

    def test_successfull_quit_account(self, driver, authorization):

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(MainPageLocators.MAIN_HEADER))
        driver.find_element(*MainPageLocators.PROFILE_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(ProfilePageLocator.LOGOUT_BUTTON))
        driver.find_element(*ProfilePageLocator.LOGOUT_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(LoginPageLocators.LOGIN_BUTTON))

        assert Urls.LOGIN_PAGE in driver.current_url
