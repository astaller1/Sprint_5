import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestConstructor:

    def test_click_buns_scrolls_to_buns(self, driver):

        driver.get('https://stellarburgers.education-services.ru')

        driver.find_element(By.XPATH, "//span[text()='Соусы']").click()
        WebDriverWait(driver, 5).until(expected_conditions.text_to_be_present_in_element_attribute((By.XPATH, "//span[text()='Соусы']/.."), 'class', 'tab_tab_type_current'))
        driver.find_element(By.XPATH, "//span[text()='Булки']").click()

        assert WebDriverWait(driver, 5).until(expected_conditions.text_to_be_present_in_element_attribute((By.XPATH, "//span[text()='Булки']/.."), 'class', 'tab_tab_type_current'))
        driver.quit()

    def test_click_sauces_scrolls_to_sauces(self, driver):

        driver.get('https://stellarburgers.education-services.ru')

        driver.find_element(By.XPATH, "//span[text()='Соусы']").click()
        
        assert WebDriverWait(driver, 5).until(expected_conditions.text_to_be_present_in_element_attribute((By.XPATH, "//span[text()='Соусы']/.."), 'class', 'tab_tab_type_current'))
        driver.quit()

    def test_click_fillings_scrolls_to_fillins(self, driver):

        driver.get('https://stellarburgers.education-services.ru')

        driver.find_element(By.XPATH, "//span[text()='Начинки']").click()
                
        assert WebDriverWait(driver, 5).until(expected_conditions.text_to_be_present_in_element_attribute((By.XPATH, "//span[text()='Начинки']/.."), 'class', 'tab_tab_type_current'))
        driver.quit()
