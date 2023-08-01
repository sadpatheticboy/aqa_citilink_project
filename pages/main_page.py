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
    cookie_button = "//button[@class='e4uhfkv0 css-1jfe691 e4mggex0']"
    search_label = "//input[@name='text']"
    filter_by_price_button = "//button[@data-meta-value='price']"
    filter_by_price_slider = ('/html/body/div[2]/div/main/div[1]/div/div[2]/section/div[1]/div/div/div/div[3]/div/'
                              'div[3]/div[2]/div[3]/div/div[5]')
    add_to_favorites_button = "//button[@class='etd7ecp0 app-catalog-11xrwzj e8hswel0']"
    link_jobs_button = "/html/body/div[2]/div/main/div[2]/div/div[2]/div[2]/ul[3]/li[6]/a"
    county_button = "//button[@class='e1x3msk40 css-wsr9k9 etyxved0']"

    # Getters
    def get_cookie_button(self):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.cookie_button)))

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

    def get_link_jobs_button(self):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.link_jobs_button)))

    def get_county_button(self):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.county_button)))

    # Actions
    def click_cookie_button(self):
        self.get_cookie_button().click()
        print(f'Clicked The Cookie Button')

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

    def click_link_jobs_button(self):
        self.get_link_jobs_button().click()
        print('Clicked Link Jobs Button')

    # Methods
    def search_product(self):
        print('[Step "Search"]')
        self.get_current_url()
        self.input_text('Процессор AMD Ryzen 9')
        self.start_search()
        self.click_filter_by_price_button()
        self.get_filter_by_price_slider()
        self.click_add_to_favorites_button()
        print('Step Search Completed Successfully\n')

    def open_link_jobs(self):
        print('[Step Link "jobs"]')
        self.click_cookie_button()
        self.click_link_jobs_button()
        self.assert_url_check('https://job.citilink.ru/')
        print('Step Link "Jobs" Completed Successfully\n')
