from pages.base_page import BasePage
from playwright.sync_api import expect

def test_search_test(page):

    bp = BasePage(page)
    bp.open()
    bp.accept_cookies()
    bp.search(keyword="44681079")

    expect(page).to_have_url("https://www.ambringa.hu/tukor-vakitasmentes-krom-300x105mm-270908-10117?keyword=44681079")
