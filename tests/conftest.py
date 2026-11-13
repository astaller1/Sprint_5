import random
import string
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import RegisterPageLocators, LoginPageLocators, MainPageLocators, ProfilePageLocator
from urls import Urls
from data import UserData


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    driver_instance = webdriver.Chrome(options=options)
    driver_instance.implicitly_wait(5)

    yield driver_instance

    driver_instance.quit()


@pytest.fixture
def new_email():
    random_digits = random.randint(100, 999)
    return f'{UserData.email_prefix}{random_digits}{UserData.email_domain}'


@pytest.fixture
def valid_password():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(6))


@pytest.fixture
def short_password():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(5))


@pytest.fixture(scope='session')
def fixed_session_user():
    random_digits = random.randint(100, 999)
    email = f'{UserData.email_prefix}{random_digits}{UserData.email_domain}'
    password = UserData.default_password

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)

    driver.get(Urls.REGISTER_PAGE)
    driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys(UserData.default_name)
    driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(email)
    driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(RegisterPageLocators.LOGIN_HEADER))
    driver.quit()

    return {'email': email, 'password': password}


@pytest.fixture
def authorization(driver, fixed_session_user):
    driver.get(Urls.LOGIN_PAGE)

    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(fixed_session_user["email"])
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(fixed_session_user["password"])
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()

    return fixed_session_user


@pytest.fixture
def open_profile(driver, authorization):
    WebDriverWait(driver, 5).until(
        expected_conditions.visibility_of_element_located(MainPageLocators.MAIN_HEADER))
    driver.find_element(*MainPageLocators.PROFILE_BUTTON).click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(ProfilePageLocator.LOGOUT_BUTTON))
 