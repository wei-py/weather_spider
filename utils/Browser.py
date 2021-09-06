# coding=utf-8
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options


class Bro():
    def __init__(self):
        self.chrome_options = Options()
        self.chrome_options.add_argument('--headless')
        self.chrome_options.add_argument('--disable-gpu')

    # 无头浏览器
    def headlessBro(self):
        bro = Chrome('/Applications/chromedriver',
                     chrome_options=self.chrome_options)
        return bro
