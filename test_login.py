import pytest
from playwright.sync_api import sync_playwright
from login_page import LoginPage

#@pytest.fixture
#def page():
 #   with sync_playwright() as p:
  #      browser = p.chromium.launch(headless = False)
   #     page = browser.new_page()
    #    yield page
     #   browser.close()

def test_locked_out_user(page):
    #with sync_playwright() as p:
        #browser = p.chromium.launch(headless=False)
        #page = browser.new_page()
        login_page = LoginPage(page)
        login_page.goto()
        login_page.login("locked_out_user","secret_sauce")
        #page.goto("https://www.saucedemo.com")
        #page.fill("#user-name","locked_out_user")
        #page.fill("#password","secret_sauce")
        #page.click("#login-button")
        assert page.locator(".error-message-container").is_visible()
        #print("Login Successful!")
        #browser.close()

def test_login_product(page):
    #with sync_playwright() as p:
        #browser = p.chromium.launch(headless=False)
        #page = browser.new_page()
        login_page = LoginPage(page)
        login_page.goto()
        login_page.login("standard_user", "secret_sauce")
        #page.goto("https://www.saucedemo.com")
        #page.fill("#user-name","standard_user")
        #page.fill("#password","secret_sauce")
        #page.click("#login-button")
        assert page.locator(".title").text_content()=="Products"
        #print("Login Successful!")
        #browser.close()

def test_cart_is_visible(page):
    #with sync_playwright() as p:
     #   browser = p.chromium.launch(headless=False)
      #  page = browser.new_page()
        login_page = LoginPage(page)
        login_page.goto()
        login_page.login("standard_user","secret_sauce")
        #page.goto("https://www.saucedemo.com")
        #page.fill("#user-name","standard_user")
        #page.fill("#password","secret_sauce")
        #page.click("#login-button")
        assert page.locator(".shopping_cart_link").is_visible()
       # browser.close()

def test_add_to_cart(page):
    #with sync_playwright() as p:
     #   browser = p.chromium.launch(headless=False)
      #  page = browser.new_page()
        login_page = LoginPage(page)
        login_page.goto()
        login_page.login("standard_user","secret_sauce")
        #page.goto("https://www.saucedemo.com")
        #page.fill("#user-name","standard_user")
        #page.fill("#password","secret_sauce")
        #page.click("#login-button")
        page.click(".btn_inventory")
        assert page.locator(".shopping_cart_badge").text_content() == "1"
       # browser.close()

def test_cart_url(page):
    #with sync_playwright() as p:
     #   browser = p.chromium.launch(headless=False)
      #  page = browser.new_page()
        login_page = LoginPage(page)
        login_page.goto()
        login_page.login("standard_user","secret_sauce")
        #page.goto("https://www.saucedemo.com")
        #page.fill("#user-name","standard_user")
        #page.fill("#password","secret_sauce")
        #page.click("#login-button")
        page.click(".shopping_cart_link")
        assert "cart" in page.url
       # browser.close()

@pytest.mark.parametrize("username, expected_result", [
    ("standard_user", "success"),
    ("locked_out_user", "blocked"),
])
def test_login_outcomes(page , username, expected_result):
    #with sync_playwright() as p:
     #   browser = p.chromium.launch(headless=False)
      #  page = browser.new_page()
        login_page = LoginPage(page)
        login_page.goto()
        login_page.login(username, "secret_sauce")
        if expected_result == "success":
            assert page.locator(".title").text_content() == "Products"
        else:
            assert page.locator(".error-message-container").is_visible()
       # browser.close()

