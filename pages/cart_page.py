from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class CartPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    clear_cart_button = "/html/body/div[2]/div/main/div[1]/div[2]/section/div[2]/div/div[1]/div[2]/button[2]"
    cart_word = "/html/body/div[2]/div/main/div[1]/div[2]/div/div[1]/span"

    # Getters
    def get_clear_cart_button(self):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.clear_cart_button)))

    def get_cart_word(self):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.cart_word)))

    # Actions
    def click_clear_cart_button(self):
        self.get_clear_cart_button().click()
        print('Clicked Clear Cart Button')

    # Methods
    def clear_cart(self):
        print('[Step "Clear Cart"]')
        self.get_current_url()
        self.assert_url_check('https://www.citilink.ru/order/')
        self.click_clear_cart_button()
        self.assert_word_check(self.get_cart_word(), 'В корзине нет товаров')
        print('Step "Clear Cart" Completed Successfully\n')

    # def add_wishlist_to_cart(self):
    #     print('[Step "Trasfer To Cart"]')
    #     self.get_current_url()
    #     self.click_wishlist_button()
    #     self.assert_url_check('https://www.citilink.ru/profile/wishlist/')
    #     self.click_add_to_cart_from_wishlist_button()
    #     self.assert_word_check(self.get_cart_icon_text(), self.get_wishlist_icon_text().text)
    #     print('Step "Clear Wishlist" Completed Successfully\n')
