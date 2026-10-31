from selenium.webdriver.common.by import By


class RegisterPageLocators:

    NAME_INPUT = (By.XPATH, "//div[label[text()='Имя']]/input")
    EMAIL_INPUT = (By.XPATH, "//div[label[text()='Email']]/input")
    PASSWORD_INPUT = (By.NAME, 'Пароль')
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".input__error")
    LOGIN_HEADER = (By.XPATH, "//h2[text()='Вход']")

class LoginPageLocators:

    EMAIL_INPUT = (By.XPATH, "//div[label[text()='Email']]/input")
    PASSWORD_INPUT = (By.NAME, 'Пароль')
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[text()='Войти']") # Ссылки "Войти" на страницах регистрации/восстановления

class ProfilePageLocator:

    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")

class MainPageLocators:

    MAIN_LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    PROFILE_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    LOGO_BUTTON = (By.CSS_SELECTOR, 'header nav a svg')
    MAIN_HEADER = (By.XPATH, "//h1[text()='Соберите бургер']")
    MAIN_SECTION = (By.XPATH, "//section[.//h1[text()='Соберите бургер']]")

    # Вкладки Конструктора

    BUNS_TAB = (By.XPATH, "//span[text()='Булки']")
    SAUCES_TAB =(By.XPATH, "//span[text()='Соусы']")
    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']")

    # Родительские вкладки конструктора для проверки статуса скролла

    BUNS_TAB_PARENT = (By.XPATH, "//span[text()='Булки']/..") 
    SAUCES_TAB_PARENT = (By.XPATH, "//span[text()='Соусы']/..")
    FILLINGS_TAB_PARENT = (By.XPATH, "//span[text()='Начинки']/..")
