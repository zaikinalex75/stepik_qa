import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from .pages.main_page import MainPage

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    main_page = MainPage(browser, link)
    main_page.open()
    main_page.should_contain_login_link()
