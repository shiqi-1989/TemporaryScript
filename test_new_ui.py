from playwright.sync_api import sync_playwright

url = "http://10.1.114.124:3000/"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=5000)
    page = browser.new_page()
    page.goto(url)
    print(page.title())
    handle = page.query_selector("text=登  录 ")
    handle.hover()
    handle.click()
    browser.close()
