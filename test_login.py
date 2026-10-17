from playwright.sync_api import Page,expect
from Log_in_page import Loginpage

def test_sucesful_login(page: Page):
    """
    test úspěšného přihlášení
    """
    
    page.goto("https://www.saucedemo.com/")
    login_page = Loginpage(page)

    #přihlášení do sauce demo a ověření url
    login_page.login("standard_user", "secret_sauce") 
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

def test_unsucesful_login(page: Page):
    """
    test nůspěšného přihlášení (špatné iputy)
    """

    page.goto("https://www.saucedemo.com/")

    login_page = Loginpage(page)
    login_page.login("nobody", "123")
    expect(login_page.login_error()).to_be_visible()

def test_empty_login(page: Page):
    """
    test neůspěšného přihlášení (prázdné hodnoty)
    """

    page.goto("https://www.saucedemo.com/")

    login_page = Loginpage(page)
    login_page.login("", "")
    expect(login_page.login_error()).to_be_visible()




