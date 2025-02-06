'''import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://playwright.dev/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Playwright"))

def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")

    # Click the get started link.
    page.get_by_role("link", name="Get started").click()

    # Expects page to have a heading with the name of Installation.
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()'''


'''
import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)#can be used in headless mode, with true
    context = browser.new_context() #a browser contest is an isolated incognito-alike session within a browser instance
    page = context.new_page()
    page.goto("https://adatamanagement.be/")
    page.get_by_placeholder("Enter your email address").click()
    page.get_by_placeholder("Enter your email address").fill("datamanagement.net")
    page.get_by_placeholder("Enter your password").click()
    page.get_by_placeholder("Enter your password").fill("datamanagement")
    #page.get_by_role("button", name="Log In").click()
    #page.locator("a").filter(has_text="Data Lake").first.click()

    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)'''






'''
import re
import asyncio
#from playwright.sync_api import Playwright, sync_playwright, expect
from playwright.async_api import async_playwright

async def main():
  async with async_playwright() as p:
    browser = await p.chromium.launch(headless=False)  # Set headless=True for background execution
    # Create two separate page contexts (tabs)
    context1 = await browser.new_context()
    context2 = await browser.new_context()

    # Open the first URL in the first context (tab)
    page1 = await context1.new_page()
    await page1.goto("https://dxxxxxxxxxxxxxxxxxxxxdxxxxxxxxxxxxxxxxxxxe/connect/login")

    # Open the second URL in the second context (tab)
    page2 = await context2.new_page()
    await page2.goto("https:/dxxxxxxxxxxxxxxxxxxxe/dataManagement/ingestionValidation")

    # You can now interact with each page independently using page1 and page2 objects

    # Example: Print page titles
    print(f"Page 1 title: {await page1.title()}")
    print(f"Page 2 title: {await page2.title()}")

    # Close the browser after interacting with the pages (if needed)
    # await browser.close()
if __name__ == "__main__":
  asyncio.run(main())'''


'''
from playwright.sync_api import sync_playwright 
#.sync_api , this submodule within Playwright provides functions for synchronous browser interaction. Synchronous means the code will execute line by line, waiting for each operation to complete before moving on.
#sync_playwright This is the function being imported. It's likely the entry point for interacting with browsers using Playwright's synchronous API.

with sync_playwright() as p:
  browser = p.chromium.launch(headless=False)  # Set headless=True for background execution

  # Create a new page context (browser window)
  context = browser.new_context()

  # Open the first URL in a new tab
  page1 = context.new_page()
  page1.goto("https://dxxxxxxxxxxxxxxxxxxx/connect/login")

  # Open the second URL in another new tab
  #page2 = context.new_page()
  #page2.goto("https://dxxxxxxxxxxxxxxxxxxx.be/dataManagement/ingestionValidation")

 # Check if only one tab is open (initial tab + newly opened ingestionValidation tab)
  # This ensures the login URL is opened in a new tab only after the first tab opens
  if len(context.pages) == 2:
    # Open the login URL in a new tab
    page2 = context.new_page()
    page2.goto("https://adxxxxxxxxxxxxxxxxxxx/dataManagement/ingestionValidation")
  else:
    print("Unexpected number of tabs open. Script requires opening the login URL in a new tab after the initial ingestionValidation tab opens.")


  # You can now interact with each page independently using page1 and page2 objects

  # Example: Print the title of each page
  #print(f"Page 1 title: {page1.title()}")
  #print(f"Page 2 title: {page2.title()}")

  # Close the browser window
  context.close()
  browser.close()
'''

