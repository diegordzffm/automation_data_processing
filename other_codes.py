'''import re

text = "My email is example@domain.com and phone number is 123-456-7890."

# Search for email address
email_pattern = r"[\w\.]+@[\w\.]+"  # Pattern for email format
email_match = re.search(email_pattern, text)

if email_match:
  email = email_match.group()
  print("Email:", email)

# Replace phone number with a placeholder
phone_pattern = r"\d{3}-\d{3}-\d{4}"  # Pattern for phone number format
new_text = re.sub(phone_pattern, "[redacted]", text)
print(new_text)'''

'''
from playwright.sync_api import sync_playwright 

with sync_playwright() as p:
  browser = p.chromium.launch(headless=False)  # Set headless=True for background execution

  context = browser.new_context()
  page1 = context.new_page()
  page1.goto("https://datamanagementDiego/connect/login")

  if len(context.pages) == 1:
    # Open the login URL in a new tab
    page2 = context.new_page()
    page2.goto("https://datamanagementDiego/dataManagement/ingestionValidation")
    page2.get_by_placeholder("Enter your email address").fill("datamanagementDiego")
    page2.get_by_placeholder("Enter your password").click()
    page2.get_by_placeholder("Enter your password").fill("datamanagementDiego")
    page2.get_by_role("button", name="Log In").click()
    page2.locator("a").filter(has_text="Data Lake").first.click()
    page2.get_by_role("button", name="Add file").click()
    page2.get_by_placeholder("Select an entity...").click()
  else:
    print("Unexpected number of tabs open. Script requires opening the login URL in a new tab after the initial ingestionValidation tab opens.")'''


'''from playwright.sync_api import sync_playwright

def open_urls_with_condition(url1, url2):
  with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # Set headless to False for visual confirmation
    context = browser.new_context()
    page1 = context.new_page()
    # Open the first URL with wait for navigation
    try:
      page1.goto(url1)
      print(f"Opened page 1: {url1}")
      page1.goto("https://datamanagementDiego/connect/login")
      page1.get_by_placeholder("Enter your email address").click()
      page1.get_by_placeholder("Enter your email address").click()
      page1.get_by_placeholder("Enter your email address").fill("datamanagementDiego")
      page1.get_by_placeholder("Enter your password").click()
      page1.get_by_placeholder("Enter your password").click(modifiers=["ControlOrMeta"])
      page1.get_by_placeholder("Enter your password").fill("datamanagementDiego")
      page1.get_by_role("button", name="Log In").click()
    except Exception as e:
      print(f"Error opening page 1: {e}")
      browser.close()
      return

    # Wait for specific element on first page to indicate successful loading (replace with your actual element)
    page1.wait_for_selector(".login-success-message", timeout=1000)  # Adjust timeout if needed

    # Open the second URL in a new tab after successful first page load
    page2 = context.new_page()
    page2.goto(url2)
    print(f"Opened page 2: {url2}")

    # You can now perform actions on both pages (page1 and page2)

    browser.close()

# Replace with your actual URLs
url1 = "https://datamanagementDiego/connect/login"
url2 = "https://datamanagementDiego/dataManagement/ingestionValidation"
open_urls_with_condition(url1, url2)
'''

#in-built locator

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
  browser = p.chromium.launch(headless=False)  # Set headless to False for visual debugging

  page1 = browser.new_page()
  page1.goto("https://datamanagementDiego/connect/login")
  page1.goto("https://datamanagementDiego/")
    page.goto("https://datamanagementDiego/connect/login")
    page.get_by_placeholder("Enter your email address").click()
    page.get_by_placeholder("Enter your email address").click()
    page.get_by_placeholder("Enter your email address").fill("datamanagementDiego")
    page.get_by_placeholder("Enter your password").click()
    page.get_by_placeholder("Enter your password").click(modifiers=["ControlOrMeta"])
    page.get_by_placeholder("Enter your password").fill("datamanagementDiego")
    page.get_by_role("button", name="Log In").click()

  # Wait for login page to load (modify selector as needed)
  page1.wait_for_selector(".login-form", timeout=10000)  # Adjust timeout if necessary

  # Check if login page loaded successfully (optional)
  if page1.title() == "B-Fine Acceptance - Login":
    print("Login page loaded successfully")
    # Open the second URL in a new tab within the same page (context) 
  else:
    page2 = browser.new_page(context=page1.context)
    page2.goto("https://datamanagementDiego/dataManagement/ingestionValidation")
    print("Opened https://datamanagementDiego/dataManagement/ingestionValidation in a new tab")
    print("Login page failed to load or title mismatch")

  # Add a pause to see the opened tabs (optional)
  page1.wait_for_timeout(5000)  # Wait for 5 seconds

  browser.close()
