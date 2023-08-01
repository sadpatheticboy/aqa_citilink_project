from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class WishlistPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    wishlist_button = "/html/body/div[2]/div/div[3]/div/div[2]/div/div/div[2]/div[2]/a[1]/div"
    clear_wishlist_button = "/html/body/div[2]/div[2]/main/div/div[2]/section/div[1]/div[2]/aside/div/button"
    wishlist_text = "//h2[@class='FavouritesAdvantagesItem__title']"

    # Getters
    def get_wishlist_button(self):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.wishlist_button)))

    def get_clear_wishlist_button(self):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.clear_wishlist_button)))

    def get_wishlist_text(self):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.wishlist_text)))

    # Actions
    def click_wishlist_button(self):
        self.get_wishlist_button().click()
        print(f'Clicked The Wishlist Button')

    def click_clear_wishlist_button(self):
        self.get_clear_wishlist_button().click()
        print(f'Clicked The Clear Wishlist Button')

    # Methods
    def clear_wishlist(self):
        print('[Step "Clear Wishlist"]')
        self.get_current_url()
        self.click_wishlist_button()
        self.assert_url_check('https://www.citilink.ru/profile/wishlist/')
        self.click_clear_wishlist_button()
        self.assert_word_check(self.get_wishlist_text(), 'Список очищен')
        print('Step "Clear Wishlist" Completed Successfully\n')

    def buy_all_favorites(self):
        pass
