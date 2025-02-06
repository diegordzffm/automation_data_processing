'''import re
#import re statement in Python brings in the powerful re module, which stands for "regular expressions." This module provides a comprehensive toolkit for working with patterns in text data
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://playwright.dev/")

    # Expect a title "to contain" a substring.s
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
    page.goto("https://datamanagementDiego/")
    page.get_by_placeholder("Enter your email address").click()
    page.get_by_placeholder("Enter your email address").fill("datamanagementDiego.net")
    page.get_by_placeholder("Enter your password").click()
    page.get_by_placeholder("Enter your password").fill("Admin@admin123")
    #page.get_by_role("button", name="Log In").click()
    #page.locator("a").filter(has_text="Data Lake").first.click()

    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)'''




#.sync_api , this submodule within Playwright provides functions for synchronous browser interaction. Synchronous means the code will execute line by line, waiting for each operation to complete before moving on.
import asyncio
from playwright.async_api import async_playwright 
#sync_playwright This is the function being imported. It's likely the entry point for interacting with browsers using Playwright's synchronous API.
async def becris():
  with async_playwright() as p:
    browser = await p.chromium.launch(headless=False)  # Set headless=True for background execution




  
  # Create a new page context (browser window)
  context = browser.new_context()
  # Open the first URL in a new tab
  page = await context.new_page()
  page.goto("https://datamanagementDiego/connect/login")
  page.get_by_placeholder("Enter your email address").click()
  page.get_by_placeholder("Enter your email address").fill("datamanagementDiego.net")
  page.get_by_placeholder("Enter your password").click()
  page.get_by_placeholder("Enter your password").click(modifiers=["ControlOrMeta"])
  page.get_by_placeholder("Enter your password").fill("admin@datamanagementDiego")
  page.get_by_role("button", name="Log In").click()
  # Open the second URL in another new tab
  page2 = context.new_page()
  page2.goto("https://datamanagementDiego/dataManagement/ingestionValidation")
 
 # Check if only one tab is open (initial tab + newly opened ingestionValidation tab)
  # This ensures the login URL is opened in a new tab only after the first tab opens
  '''if len(context.pages) == 2:
    # Open the login URL in a new tab
    page2 = context.new_page()
    page2.goto("https://datamanagementDiego/dataManagement/ingestionValidation")
  else:
    print("Unexpected number of tabs open. Script requires opening the login URL in a new tab after the initial ingestionValidation tab opens.")
'''

  # You can now interact with each page independently using page1 and page2 objects

  # Example: Print the title of each page
  #print(f"Page 1 title: {page1.title()}")
  #print(f"Page 2 title: {page2.title()}")

  # Close the browser window
  context.close()
  browser.close()

