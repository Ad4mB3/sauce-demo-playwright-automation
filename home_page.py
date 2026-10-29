from playwright.sync_api import Page

class Homepage:
    def __init__(self, page: Page):
        self.page = page 
        self.sorting = page.locator("[data-test='product-sort-container']")
        self.logoutbtn = page.locator("#logout_sidebar_link")
        self.menubbtn = page.locator("#react-burger-menu-btn")
        self.aboutbtn = page.locator("#about_sidebar_link")
        self.allitemsbtn = page.locator("#inventory_sidebar_link")
        

    def logout(self):
        self.menubbtn.click()
        self.logoutbtn.click()
        

    def add_to_cart(self, productname):
        self.page.locator(f"[data-test='add-to-cart-{productname}']").click()

    def about_info(self):
        self.menubbtn.click()
        self.aboutbtn.click()

    def all_items(self):
        self.page.get_by_text("Sauce Labs Backpack").click()
        self.menubbtn.click()
        self.allitemsbtn.click()

    def removebutton(self, productname):
        return self.page.locator(f"[data-test='remove-{productname}']")
        
