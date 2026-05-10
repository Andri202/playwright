from playwright.sync_api import expect
from pages.login_page import LoginPage

def test_success_login(page):
   login = LoginPage(page)

   login.open()
   login.login("standard_user", "secret_sauce")
   expect(page).to_have_url("https://www.saucedemo.com/inventory.html")