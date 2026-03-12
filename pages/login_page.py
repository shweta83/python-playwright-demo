
class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username = page.get_by_name("user-name")
        self.password = page.get_by_name("password")
        self.login_button = page.get_by_name("login-button")

    def load(self):
        self.page.goto("https://www.saucedemo.com")

    def login(self,user,password):
        self.username.fill(user)
        self.password.fill(password)
        self.login_button.click()

