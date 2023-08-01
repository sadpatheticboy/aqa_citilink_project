from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.wishlist_page import WishlistPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_clear_cart():
    # Подключение к Chrome
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_experimental_option("detach", True)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.page_load_strategy = 'eager'
    path_chrome = Service(executable_path='D:/Necessary/QA/drivers/chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=path_chrome)

    print('\nStart Test\n')

    lp = LoginPage(driver)
    lp.authorization()

    mp = MainPage(driver)
    mp.search_product()

    wp = WishlistPage(driver)
    wp.add_wishlist_to_cart()

    cp = CartPage(driver)
    cp.go_to_checkout()

    chechoutp = CheckoutPage(driver)
    chechoutp.confirm_order()

    print('Test Successfuly FInished\n')
    # driver.quit()
