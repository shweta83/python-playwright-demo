
def test_add_to_cart(page):
    page.goto("https://www.saucedemo.com")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("text=Add to cart")
    cart_count = page.locator(".shopping_cart_badge").text_content()
    assert cart_count == "1"

