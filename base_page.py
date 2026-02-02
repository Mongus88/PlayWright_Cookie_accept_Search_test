class BasePage:
    def __init__(self, page):
        self.page = page
        self.cookie_button = page.get_by_role("button", name="Elfogadom")
        self.search_field = page.locator("#filter_keyword")

    def open(self):
        self.page.goto("https://ambringa.com")

    def accept_cookies(self):
        if self.cookie_button.is_visible(timeout=2000):
            self.cookie_button.click()

    def search(self, keyword):
        self.search_field.fill(keyword)
        self.search_field.press("Enter")
