import pytest
import random
import string
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    
    driver_instance = webdriver.Chrome(options=options)
    driver_instance.implicitly_wait(5)

    return driver_instance

@pytest.fixture
def new_email():
    random_digits = random.randint(100, 999)
    return f'lidia_smirnova_54_{random_digits}@yandex.ru'

@pytest.fixture
def valid_password():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(6))

@pytest.fixture
def short_password():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(5))

@pytest.fixture
def pre_registration(driver, new_email, valid_password):

    driver.get('https://stellarburgers.education-services.ru/register')

    driver.find_element(By.XPATH, "//div[label[text()='Имя']]/input").send_keys('Иван')
    driver.find_element(By.XPATH, "//div[label[text()='Email']]/input").send_keys(new_email)
    driver.find_element(By.NAME, 'Пароль').send_keys(valid_password)
    driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']").click()

    return {"email": new_email, "password": valid_password}

@pytest.fixture
def authorization(driver, pre_registration):

    driver.get('https://stellarburgers.education-services.ru/login')

    driver.find_element(By.XPATH, "//div[label[text()='Email']]/input").send_keys(pre_registration["email"])
    driver.find_element(By.NAME, 'Пароль').send_keys(pre_registration["password"])
    driver.find_element(By.XPATH, "//button[text()='Войти']").click()

    return pre_registration
