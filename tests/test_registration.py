import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from tests.locators import RegisterPageLocators
from urls import Urls


class TestRegistration:

    def test_successfull_registration(self, driver, new_email, valid_password):

        driver.get(Urls.REGISTER_PAGE)

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(RegisterPageLocators.NAME_INPUT))
        driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys('Иван')
        driver.find_element(*RegisterPageLocators.EMAIL_INPUT ).send_keys(new_email)
        driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(valid_password)
        driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(RegisterPageLocators.LOGIN_HEADER))

        assert Urls.LOGIN_PAGE in driver.current_url

    def test_registration_with_short_password_shows_error(self, driver, new_email, short_password):

        driver.get(Urls.REGISTER_PAGE)

        driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys('Иван')
        driver.find_element(*RegisterPageLocators.EMAIL_INPUT ).send_keys(new_email)
        driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(short_password)
        driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

        error_message = driver.find_element(*RegisterPageLocators.ERROR_MESSAGE).text

        assert error_message == 'Некорректный пароль'
