from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from pages.login_page import LoginPage


def test_some():
    # Подключение к Chrome
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_experimental_option("detach", True)
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.page_load_strategy = 'eager'
    # capabilities = DesiredCapabilities.CHROME.copy()
    # capabilities['pageLoadStrategy'] = 'eager'
    path_chrome = Service(executable_path='D:/Necessary/QA/drivers/chromedriver.exe')
    driver = webdriver.Chrome(options=options, service=path_chrome)
    # driver = webdriver.Chrome(options=options, service=path_chrome, desired_capabilities=capabilities)

    # options = Options()
    # options.add_experimental_option('ecludeSwitches', ['enable-logging'])
    # path_chrome = Service('D:/Necessary/QA/drivers/chromedriver.exe')
    # driver = webdriver.Chrome(service=path_chrome, chrome_options=options)
    # driver = webdriver.ChromeOptions()
    # driver.add_experimental_option('detach', True)
    # path_chrome = Service('D:/Necessary/QA/drivers/chromedriver.exe')
    # capabilities = DesiredCapabilities.CHROME.copy()
    # capabilities['pageLoadStrategy'] = 'eager'
    # driver = webdriver.Chrome(service=path_chrome, options=driver, desired_capabilities=capabilities)

    print('\nStart Test')

    lp = LoginPage(driver)
    lp.authorization()
