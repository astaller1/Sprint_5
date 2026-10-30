import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestRegistration:

    def test_successfull_registration(self, driver, new_email, valid_password):

        driver.get('https://stellarburgers.education-services.ru/register')

        driver.find_element(By.XPATH, "//div[label[text()='Имя']]/input").send_keys('Иван')
        driver.find_element(By.XPATH, "//div[label[text()='Email']]/input").send_keys(new_email)
        driver.find_element(By.NAME, 'Пароль').send_keys(valid_password)
        driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']").click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "//h2[text()='Вход']")))

        assert "/login" in driver.current_url
        driver.quit()

    def test_registration_with_short_password_shows_error(self, driver, new_email, short_password):

        driver.get('https://stellarburgers.education-services.ru/register')

        driver.find_element(By.XPATH, "//div[label[text()='Имя']]/input").send_keys('Иван')
        driver.find_element(By.XPATH, "//div[label[text()='Email']]/input").send_keys(new_email)
        driver.find_element(By.NAME, 'Пароль').send_keys(short_password)
        driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']").click()

        error_message = driver.find_element(By.CSS_SELECTOR, ".input__error").text

        assert error_message == 'Некорректный пароль'
        driver.quit()
