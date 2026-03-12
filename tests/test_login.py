from pages.login_page import LoginPage

def test_successful_login(page):
    login = LoginPage(page)
    login.load()
    login.login("standard_user","secret_sauce")
    assert page.locator(".inventory_list").is_visible()

