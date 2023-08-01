import datetime


class Base:
    def __init__(self, driver):
        self.driver = driver

    # Method Get Current Url
    def get_current_url(self):
        get_url = self.driver.current_url
        print(f'Current URL is "{get_url}"')

    # Method Assert Url Check
    def assert_url_check(self, result):
        get_url = self.driver.current_url
        assert get_url == result

    # Method Assert Word Check
    def assert_word_check(self, word, result):
        value_word = word.text
        assert value_word == result
        print('All Correct')

    # Method Screenshot
    def take_screenshot(self):
        current_moment = datetime.datetime.now().strftime("%Y.%m.%d-%H.%M.%S")
        name_screenshot = f'screenshot_{current_moment}.png'
        self.driver.save_screenshot(f'.\\screen\\{name_screenshot}')
