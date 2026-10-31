import pytest
import random
import string
from selenium import webdriver
from tests.locators import RegisterPageLocators, LoginPageLocators
from urls import Urls


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    
    driver_instance = webdriver.Chrome(options=options)
    driver_instance.implicitly_wait(5)

    yield driver_instance

    driver_instance.quit

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
def fixed_session_user(driver, new_email, valid_password):

    driver.get(Urls.REGISTER_PAGE)

    driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys('Иван')
    driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(new_email)
    driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(valid_password)
    driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

    return {"email": new_email, "password": valid_password}

@pytest.fixture(scope='session')
def fixed_session_user():

    random_digits = random.randint(100, 999)
    email = f'lidia_smirnova_54_{random_digits}@yandex.ru'
    password = 'abc123'

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)

    driver.get(Urls.REGISTER_PAGE)
    driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys('Иван')
    driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()
    driver.quit()

    return {'email': email, 'password': password}

@pytest.fixture
def authorization(driver, fixed_session_user):

    driver.get(Urls.LOGIN_PAGE)

    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(fixed_session_user["email"])
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(fixed_session_user["password"])
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    return fixed_session_user