from .base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver.common.by import By

class MainPage(BasePage):

    def go_to_login_page(self):
       login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
       login_link.click()

    def should_contain_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), \
               'Нет ссылки входа на главной странице!'
   
