from playwright.sync_api import Page, expect
from home_page import Homepage
from Log_in_page import Loginpage

def test_adding_into_cart(page: Page):
    """
    test přidání do košíku
    """
    page.goto("https://www.saucedemo.com/")
    test_page = Loginpage(page)
    test_page.fulllogin()
    test_homepage = Homepage(page)

    product = "sauce-labs-backpack"
    test_homepage.add_to_cart(product)
    expect(test_homepage.removebutton(product)).to_be_visible()

  
def test_sucesful_logout(page: Page):
    """
    test úspěšného odhlášení 
    """
    page.goto("https://www.saucedemo.com/")
    logout_page = Loginpage(page)
    logout_page.fulllogin()
    logout_pagehm = Homepage(page)
    logout_pagehm.logout()
    expect(page).to_have_url("https://www.saucedemo.com/")


def test_about_info(page: Page):
    """
    test úspěšného prokliknutí na about page
    """
    page.goto("https://www.saucedemo.com/")
    about_page = Loginpage(page)
    about_page.fulllogin()
    about_pagehm = Homepage(page)
    about_pagehm.about_info()   
    expect(page).to_have_url("https://saucelabs.com/")

def test_all_items(page: Page):
    """
    test funkčnosti tlačítka All items v menu 
    """
    page.goto("https://www.saucedemo.com/")
    all_items = Loginpage(page)
    all_items.fulllogin()
    all_itemshm = Homepage(page)
    all_itemshm.all_items() 
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")






    