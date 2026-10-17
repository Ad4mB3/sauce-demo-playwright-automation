from playwright.sync_api import Page, expect
from Checkout_page import Checkout
from Log_in_page import Loginpage
from home_page import Homepage

def test_checkoutpage(page: Page):
    """
    ověření funkčnosti tlačítka košíku (check out page )
    """ 
    page.goto("https://www.saucedemo.com/")
    Login_pagetst = Loginpage(page)
    Login_pagetst.fulllogin()
    checkout_page = Checkout(page)
    checkout_page.checkoutpage()
    expect(page).to_have_url("https://www.saucedemo.com/cart.html")

def test_cart_function (page: Page):
    """
        přidání věci do košíku a následné zkontrolování zda byl uložen 
    """ 
    page.goto("https://www.saucedemo.com/")
    login_page = Loginpage(page)
    login_page.fulllogin()
    home_page = Homepage(page)
    home_page.add_to_cart("sauce-labs-backpack") #přidání produktu do košíku 
    checkout_page = Checkout(page)
    checkout_page.checkoutpage()
    expect(checkout_page.addeditembtn).to_be_visible() #oveření že produkt je v košíku 

def test_removing_items(page: Page):
    page.goto("https://www.saucedemo.com/")
    login_page = Loginpage(page)
    login_page.fulllogin()
    home_page = Homepage(page)
    home_page.add_to_cart("sauce-labs-backpack") #přidání produktu do košíku 
    checkout_page = Checkout(page)
    checkout_page.checkoutpage()
    checkout_page.remove_item("sauce-labs-backpack")
    expect(checkout_page.addeditembtn).not_to_be_visible()




    
