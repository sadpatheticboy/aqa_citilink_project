from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from base.base_class import Base


class MainPage(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    search_label = "//input[@name='text']"
    filter_by_price_button = "//button[@data-meta-value='price']"
    filter_by_price_slider = ('/html/body/div[2]/div/main/div[1]/div/div[2]/section/div[1]/div/div/div/div[3]/div/'
                              'div[3]/div[2]/div[3]/div/div[5]')
    add_to_favorites_button = "//button[@class='etd7ecp0 app-catalog-11xrwzj e8hswel0']"

    # Getters
    def get_search_label(self):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.search_label)))

    def get_filter_by_price(self):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.filter_by_price_button)))

    def get_filter_by_price_slider(self):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.filter_by_price_slider)))

    def get_add_to_favorites_button(self):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.add_to_favorites_button)))

    # Actions
    def input_text(self, some_text):
        self.get_search_label().send_keys(some_text)
        print(f'Input Text "{some_text}"')

    def start_search(self):
        self.get_search_label().send_keys(Keys.RETURN)
        print('Pressed "Return"')

    def click_filter_by_price_button(self):
        self.get_filter_by_price().click()
        print('Pressed Filter The Price Button')

    def slide_filter_by_price_slider(self):
        action = ActionChains(self.driver)
        slide = self.get_filter_by_price_slider()
        action.click_and_hold(slide).move_by_offset(-500, 0).perform()

    def click_add_to_favorites_button(self):
        self.get_add_to_favorites_button().click()
        print('Pressed Add To Favorite Button')

    # Methods
    def search_product(self):
        print('[Step "Search"]')
        self.get_current_url()
        self.input_text('Процессор AMD Ryzen 9')
        self.start_search()
        self.click_filter_by_price_button()
        self.get_filter_by_price_slider()
        self.click_add_to_favorites_button()
        print('Login Search Completed Successfully\n')
