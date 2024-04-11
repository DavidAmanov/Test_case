import pytest
from playwright.sync_api import sync_playwright

@pytest.mark.header_screenshot
def screenshot_header():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page =  browser.new_page()
        page.goto('https://www.avito.ru/avito-care/eco-impact')
        element_handle = page.query_selector('.desktop-content-HDB3N')
        assert element_handle, "Элемент заголовка не найден"
        element_handle.screenshot(path='task_2/output/Header.png')
        browser.close()



@pytest.mark.header_screenshot
def screenshot_six_cards():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page =  browser.new_page()
        page.goto('https://www.avito.ru/avito-care/eco-impact')
        element_handle = page.query_selector('.desktop-impact-items-F7T6E')
        assert element_handle, "Элементы карточек не найдены"
        element_handle.screenshot(path='task_2/output/Cards.png')
        browser.close()

