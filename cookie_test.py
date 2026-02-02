from pages.base_page import BasePage
from playwright.sync_api import expect

def test_cookie_acceptance(page):

    bp = BasePage(page)
    bp.open()
    bp.accept_cookies()

    expect(page.get_by_role("button", name="Elfogadom")).to_be_hidden()
