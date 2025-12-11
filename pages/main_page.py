from playwright.sync_api import Page, expect

class MainPage:
    def __init__(self, page: Page):
        self.page = page

    def open(self, url: str):
        self.page.goto(url, timeout=30000)

    def click(self, selector: str):
        self.page.locator(selector).click(timeout=10000)

    def scroll_to_section(self, selector: str):
        self.page.locator(selector).scroll_into_view_if_needed()

    def check_section_visibility(self, selector: str):
        section = self.page.locator(selector)
        expect(section).to_have_count(1, timeout=5000)
        section.scroll_into_view_if_needed()
        expect(section).to_be_visible(timeout=10000)

    def click_menu_item(self, name: str):
        self.page.get_by_role("link", name=name).click()

    def anchor_in_url(self, anchor: str):
        assert anchor in self.page.url, f"Anchor '{anchor}' not found in URL"

    def section_exists(self, locator: str):
        assert self.page.locator(locator).count() > 0
