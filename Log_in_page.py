from playwright.sync_api import Page

class Loginpage:
    def __init__(self, page):
        self.page = page
        self.username_input = page.locator("#user-name")
        self.password_input = page.locator("#password")
        self.loginbutton = page.locator("#login-button")
        self.loginerrorbttn = page.locator("[data-test='error']")
    

    def login(self, jmeno, heslo):
        self.username_input.fill(jmeno)
        self.password_input.fill(heslo)
        self.loginbutton.click()

    def login_error(self):
        return self.loginerrorbttn

        
    def fulllogin(self):
        self.username_input.fill("standard_user")
        self.password_input.fill("secret_sauce")
        self.loginbutton.click()


    
    
    
