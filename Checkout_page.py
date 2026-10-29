from playwright.sync_api import Page

class Checkout:
    def __init__(self, page: Page):
        self.page = page 
        self.checkoutbtn = page.locator("#shopping_cart_container > a")
        self.addeditembtn = page.locator(".cart_item")


    def checkoutpage(self):
        self.checkoutbtn.click()

    def addeditem(self):
        return self.addeditembtn

    def remove_item(self, product_name):
        self.page.locator(f"#remove-{product_name}").click()
        


    


