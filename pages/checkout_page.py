from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class CheckoutPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    checkout_text = "/html/body/div[2]/div/div[2]/div/div/div[1]/div/div[1]/div[1]/span"
    first_name_label = "//input[@name='contact-form_firstName']"
    last_name_label = "//input[@name='contact-form_lastName']"
    phone_label = "//input[@name='contact-form_phone'"
    delivery_button = ("/html/body/div[2]/div/div[2]/div/div/div[1]/div/div[1]/div[3]/div/div/div[2]/div/div[1]/div/"
                       "div[1]/div/label[2]")

    # Getters
    def get_checkout_text(self):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.checkout_text)))

    def get_first_name_label(self):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.first_name_label)))

    def get_last_name_label(self):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.last_name_label)))

    def get_phone_label(self):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.phone_label)))

    def get_delivery_button(self):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.delivery_button)))

    # Actions
    def input_first_name(self, first_name):
        self.get_first_name_label().send_keys(first_name)
        print('Input First Name')

    def input_last_name(self, last_name):
        self.get_first_name_label().send_keys(last_name)
        print('Input Last Name')

    def input_phone(self, phone):
        self.get_phone_label().send_keys(phone)
        print('Input Phone')

    def click_delivery_button(self):
        self.get_delivery_button().click()
        print('Selected Delivery Method')

    # Methods
    def confirm_order(self):
        print('[Step "Confirm Order"]')
        self.get_current_url()
        self.assert_word_check(self.get_checkout_text(), 'Оформление заказа')
        self.assert_url_check('https://www.citilink.ru/order/checkout/')
        self.input_first_name('Ivan')
        self.input_last_name('Ivanov')
        self.input_phone('+79853134750')
        self.click_delivery_button()
        print('Step "Confirm Order" Completed Successfully\n')
