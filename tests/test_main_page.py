import allure
import pytest


URL = 'https://newsapi.org/'

MENU_LINKS = {
    "News sources": "sources"
}


@allure.feature("Main page navigation")
@pytest.mark.parametrize("name,locator", MENU_LINKS.items())
def test_menu_links_anchor(main_page, name, locator):
    main_page.open(URL)

    with allure.step(f"Click section '{name}'"):
        main_page.page.get_by_role("link", name=name, exact=True).click(force=True, timeout=10000)

    with allure.step(f"Verify anchor '{locator}' in URL"):
        main_page.anchor_in_url(locator)


@pytest.mark.parametrize("name,locator", MENU_LINKS.items())
def test_menu_links_section_exist(main_page, name, locator):
    main_page.open(URL)

    with allure.step(f"Click section '{name}'"):
        main_page.page.get_by_role("link", name=name, exact=True).click(force=True, timeout=10000)

    with allure.step(f"Verify section '{name}' exists in DOM"):
        main_page.section_exists(locator)


@pytest.mark.parametrize("name,locator", MENU_LINKS.items())
def test_menu_links_visible(main_page, name, locator):
    main_page.open(URL)

    with allure.step(f"Click section '{name}'"):
        main_page.page.get_by_role("link", name=name, exact=True).click(force=True, timeout=10000)

    with allure.step(f"Verify section '{name} is visible after scroll"):
        main_page.check_section_visibility(locator)
