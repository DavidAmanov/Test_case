import pytest
from playwright.sync_api import sync_playwright

def screenshot_header():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page =  browser.new_page()
        page.goto('https://www.avito.ru/avito-care/eco-impact')
        element_handle = page.query_selector('.desktop-content-HDB3N')
        element_handle.screenshot(path='task_2/screenshots/Header.png')
        browser.close()

screenshot_header()

def screenshot_six_cards():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page =  browser.new_page()
        page.goto('https://www.avito.ru/avito-care/eco-impact')
        element_handle = page.query_selector('.desktop-impact-items-F7T6E')
        element_handle.screenshot(path='task_2/screenshots/Cards.png')
        browser.close()

screenshot_six_cards()