import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from tests.locators import MainPageLocators
from urls import Urls


class TestConstructor:

    def test_click_buns_scrolls_to_buns(self, driver):

        driver.get(Urls.MAIN_PAGE)

        driver.find_element(*MainPageLocators.SAUCES_TAB).click()
        WebDriverWait(driver, 5).until(expected_conditions.text_to_be_present_in_element_attribute(MainPageLocators.SAUCES_TAB_PARENT, 'class', 'tab_tab_type_current'))
        driver.find_element(*MainPageLocators.BUNS_TAB).click()

        assert WebDriverWait(driver, 5).until(expected_conditions.text_to_be_present_in_element_attribute(MainPageLocators.BUNS_TAB_PARENT, 'class', 'tab_tab_type_current'))

    def test_click_sauces_scrolls_to_sauces(self, driver):

        driver.get(Urls.MAIN_PAGE)

        driver.find_element(*MainPageLocators.SAUCES_TAB).click()
        
        assert WebDriverWait(driver, 5).until(expected_conditions.text_to_be_present_in_element_attribute(MainPageLocators.SAUCES_TAB_PARENT, 'class', 'tab_tab_type_current'))

    def test_click_fillings_scrolls_to_fillins(self, driver):

        driver.get(Urls.MAIN_PAGE)

        driver.find_element(*MainPageLocators.FILLINGS_TAB).click()
                
        assert WebDriverWait(driver, 5).until(expected_conditions.text_to_be_present_in_element_attribute(MainPageLocators.FILLINGS_TAB_PARENT, 'class', 'tab_tab_type_current'))
