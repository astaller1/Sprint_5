import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestProfile:

    def test_click_on_profile_redirects_to_user_profile(self, driver, authorization): 

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h1[text()='Соберите бургер']")))
        driver.find_element(By.XPATH, "//p[text()='Личный Кабинет']").click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[text()='Выход']")))

        assert '/profile' in driver.current_url
        driver.quit()
        
    def test_click_constructor_redirects_to_main(self, driver, authorization):

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h1[text()='Соберите бургер']")))
        driver.find_element(By.XPATH, "//p[text()='Личный Кабинет']").click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[text()='Выход']")))
        driver.find_element(By.XPATH, "//p[text()='Конструктор']").click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h1[text()='Соберите бургер']")))

        assert 'https://stellarburgers.education-services.ru' in driver.current_url
        driver.quit()

    def test_click_logo_redirect_to_main(self, driver, authorization):

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h1[text()='Соберите бургер']")))
        driver.find_element(By.XPATH, "//p[text()='Личный Кабинет']").click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[text()='Выход']")))
        driver.find_element(By.CSS_SELECTOR, 'header nav a svg').click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h1[text()='Соберите бургер']")))

        assert 'https://stellarburgers.education-services.ru' in driver.current_url
        driver.quit()

    def test_successfull_quit_account(self, driver, authorization):

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h1[text()='Соберите бургер']")))
        driver.find_element(By.XPATH, "//p[text()='Личный Кабинет']").click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[text()='Выход']")))
        driver.find_element(By.XPATH, "//button[text()='Выход']").click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[text()='Войти']")))

        assert '/login' in driver.current_url
        driver.quit()
