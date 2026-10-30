import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestLogin:

    def test_successfull_login_through_main_page_login_button(self, driver, pre_registration):

        driver.get('https://stellarburgers.education-services.ru')

        driver.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click()
        driver.find_element(By.XPATH, "//div[label[text()='Email']]/input").send_keys(pre_registration["email"])
        driver.find_element(By.NAME, 'Пароль').send_keys(pre_registration["password"])
        driver.find_element(By.XPATH, "//button[text()='Войти']").click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "//section[.//h1[text()='Соберите бургер']]")))

        assert 'https://stellarburgers.education-services.ru' in driver.current_url
        driver.quit()

    def test_successfull_login_through_profile_button(self, driver, pre_registration):

        driver.get('https://stellarburgers.education-services.ru')
        
        driver.find_element(By.XPATH, "//p[text()='Личный Кабинет']").click() 
        driver.find_element(By.XPATH, "//div[label[text()='Email']]/input").send_keys(pre_registration["email"])
        driver.find_element(By.NAME, 'Пароль').send_keys(pre_registration["password"])
        driver.find_element(By.XPATH, "//button[text()='Войти']").click() 

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "//section[.//h1[text()='Соберите бургер']]")))
        
        assert 'https://stellarburgers.education-services.ru' in driver.current_url
        driver.quit()

    def test_successfull_login_through_button_on_registration_page(self, driver, pre_registration):

        driver.get('https://stellarburgers.education-services.ru/register')

        driver.find_element(By.XPATH, "//a[text()='Войти']").click()
        driver.find_element(By.XPATH, "//div[label[text()='Email']]/input").send_keys(pre_registration["email"])
        driver.find_element(By.NAME, 'Пароль').send_keys(pre_registration["password"])
        driver.find_element(By.XPATH, "//button[text()='Войти']").click() 

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "//section[.//h1[text()='Соберите бургер']]")))
        
        assert 'https://stellarburgers.education-services.ru' in driver.current_url
        driver.quit()

    def test_successfull_login_through_forgot_password_page(self, driver, pre_registration):

        driver.get('https://stellarburgers.education-services.ru/forgot-password')

        driver.find_element(By.XPATH, "//a[text()='Войти']").click()
        driver.find_element(By.XPATH, "//div[label[text()='Email']]/input").send_keys(pre_registration["email"])
        driver.find_element(By.NAME, 'Пароль').send_keys(pre_registration["password"])
        driver.find_element(By.XPATH, "//button[text()='Войти']").click() 

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "//section[.//h1[text()='Соберите бургер']]")))

        assert 'https://stellarburgers.education-services.ru' in driver.current_url
        driver.quit()
