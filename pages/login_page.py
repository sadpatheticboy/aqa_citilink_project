from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class LoginPage(Base):
    # Base URL
    url = "https://www.citilink.ru/login/"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    login_label = ("//input[@class=' InputBox__input js--InputBox__input  "
                   "LoginPageLayout__input_login__container-input']")
    password_label = ("//input[@class=' InputBox__input js--InputBox__input  "
                      "LoginPageLayout__input_password js--InputPassword InputPassword__container-input']")
    login_button = "//button[@id='formSubmit']"

    # Getters
    def get_login_label(self):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.login_label)))

    def get_password_label(self):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.password_label)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.login_button)))

    # Actions
    def input_login(self, login_input):
        self.get_login_label().send_keys(login_input)
        print(f'Input Login "{login_input}"')

    def input_password(self, paswword_input):
        self.get_password_label().send_keys(paswword_input)
        print(f'Input Password "{paswword_input}"')

    def click_login_button(self):
        self.get_login_button().click()
        print('Click Login Button')

    # Methods
    def authorization(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()

        print('[Step "Login"]')
        self.input_login('bal-tim@mail.ru')
        self.input_password('@f6XB6soqB')
        self.click_login_button()
        self.assert_url_check('https://www.citilink.ru/?_action=login&_success_login=1')
        print('Login Step Completed Successfully\n')

    # username = "//input[@id='user-name']"
    # password = "//input[@id='password']"
    # login_button = "//input[@id='login-button']"
    # main_word = "//span[@class='title']"
    #
    # # Getters
    # def get_username(self):
    #     return WebDriverWait(self.driver, 10).until(
    #         expected_conditions.element_to_be_clickable((By.XPATH, self.username)))
    #
    # def get_password(self):
    #     return WebDriverWait(self.driver, 10).until(
    #         expected_conditions.element_to_be_clickable((By.XPATH, self.password)))
    #
    # def get_login_button(self):
    #     return WebDriverWait(self.driver, 10).until(
    #         expected_conditions.element_to_be_clickable((By.XPATH, self.login_button)))
    #
    # def get_main_word(self):
    #     return WebDriverWait(self.driver, 10).until(
    #         expected_conditions.element_to_be_clickable((By.XPATH, self.main_word)))
    #
    # # Actions
    # def input_username(self, username_input):
    #     self.get_username().send_keys(username_input)
    #     print('Input Username')
    #
    # def input_password(self, password_input):
    #     self.get_password().send_keys(password_input)
    #     print('Input Password')
    #
    # def click_login_button(self):
    #     self.get_login_button().click()
    #     print('Click Login Button')
    #
    # # Methods
    # def authorization(self):
    #     self.driver.get(self.url)
    #     self.driver.maximize_window()
    #     self.get_current_url()
    #     self.input_username('standard_user')
    #     self.input_password('secret_sauce')
    #     self.click_login_button()
    #     self.assert_word_check(self.get_main_word(), 'Products')
