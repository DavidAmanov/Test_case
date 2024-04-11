import pytest
from playwright.sync_api import sync_playwright

@pytest.mark.parametrize(('element', 'screenshot_name'), [('.desktop-content-HDB3N', 'eco-impact-1'), ('.desktop-impact-items-F7T6E', 'eco-impact-2')])
def test_screenshot(element, screenshot_name):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page =  browser.new_page()
        page.goto('https://www.avito.ru/avito-care/eco-impact')
        element_handle = page.query_selector(element)
        assert element_handle, f"Элемент {element} не найден"
        element_handle.screenshot(path=f'output/{screenshot_name}.png')
        browser.close()

