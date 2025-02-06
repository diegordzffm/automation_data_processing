https://acceptance.b-fine.be/dataManagement


import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None: #function named run that takes a single argument named playwright.This is the argument name, representing an instance of the Playwright class from the Playwright library. It provides access to various browser automation functionalities.
    #> None: This part defines the return type of the run function. It indicates that the function doesn't return any value (None).
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://acceptance.b-fine.be/dataManagement")
    page.goto("https://acceptance.b-fine.be/dataManagement/ingestionValidation")
    page.goto("https://acceptance.b-fine.be/")
    page.goto("https://acceptance.b-fine.be/connect/login")
    page.get_by_placeholder("Enter your email address").click()
    page.get_by_placeholder("Enter your email address").click()
    page.get_by_placeholder("Enter your email address").fill("admin@regnology.net")
    page.get_by_placeholder("Enter your password").click()
    page.get_by_placeholder("Enter your password").click(modifiers=["ControlOrMeta"])
    page.get_by_placeholder("Enter your password").fill("Admin@admin123")
    page.get_by_role("button", name="Log In").click()
    page.locator("a").filter(has_text="Data Lake").first.click()
    page.get_by_role("button", name="Add file").click()
    page.get_by_placeholder("Select an entity...").click()
    page.get_by_role("menu").locator("div").filter(has_text=re.compile(r"^B-Fine$")).first.click()
    page.get_by_role("textbox", name="Search source system...").click()
    page.get_by_role("menu").locator("div").filter(has_text=re.compile(r"^Manual$")).first.click()
    page.get_by_placeholder("MM/DD/YYYY").click()
    page.get_by_label("Choose date, selected date is").click()
    page.get_by_role("gridcell", name="23").click()
    page.get_by_role("button", name="Click to select files").click()
    page.get_by_role("button", name="Upload all files").click()
    page.get_by_role("row", name="Name Owner Entity Source").get_by_role("checkbox").check()
    page.locator(".css-1vup00y-control > .css-1wy0on6 > .css-1xc3v61-indicatorContainer > .css-8mmkcg").click()
    page.get_by_text("ANACREDIT_RL-INGESTION-NEW").click()
    page.get_by_role("button", name="Trigger the ingestion").click()
    page.locator("a").filter(has_text="Data Lake").first.click()
    page.get_by_text("ANACREDIT_RL-INGESTION-NEW").first.click()
    with page.expect_popup() as page1_info:
        page.get_by_role("link", name="ANACREDIT_RL-INGESTION-NEW").click()
    page1 = page1_info.value
    page1.goto("https://acceptance.b-fine.be/airflow/graph?dag_id=ANACREDIT_RL-INGESTION-NEW&run_id=manual__2024-05-23T12%3A20%3A53.080217%2B00%3A00&execution_date=2024-05-23T12%3A20%3A53.080Z")
    page1.get_by_role("link", name="Tree").click()
    page1.close()
    page.get_by_label("Delete").click()
    page.get_by_role("link", name="Reports").click()
    page.get_by_role("button", name="Add a new report").click()
    page.get_by_placeholder("Select an entity...").click()
    page.get_by_role("menu").locator("div").filter(has_text=re.compile(r"^B-Fine$")).first.click()
    page.get_by_placeholder("MM/DD/YYYY").first.click()
    page.locator("div:nth-child(7) > .c332w-4012 > .css-b62m3t-container > .css-1vup00y-control > .css-i9ymxl > .css-8r5rw9").click()
    page.locator("#createReport div").filter(has_text="New reportRegulatory").first.click()
    page.get_by_role("button", name="Create from workflow").click()
    page.get_by_role("row", name="Select Regnology Reporting Hub ECB B-Fine AnaCredit Belgium, Becris Full S S S 1 M 2 Calendar day 1").get_by_role("button").click()
    page.locator(".c332w-3914 > div > .iconSvg > div > .icon > path").first.click()
    page.get_by_role("menu").get_by_text("Diego Rodriguez").click()
    page.get_by_role("img").nth(2).click()
    page.get_by_role("menu").get_by_text("Diego Rodriguez").click()
    page.get_by_role("img").nth(3).click()
    page.get_by_role("textbox", name="Search user...").click()
    page.get_by_role("textbox", name="Search user...").fill("SER")
    page.get_by_role("img").nth(2).click()
    page.locator("body > div:nth-child(14) > div").first.click()
    page.get_by_role("button", name="Create the report and open it").click()
    page.get_by_label("Close").click()
    page.locator("a").filter(has_text="Anacredit").click()
    page.locator("#console").get_by_text("Data").click()
    page.get_by_text("312ANA BECRIS 2024-05-23 14:").click()
    page.once("dialog", lambda dialog: dialog.dismiss())
    page.get_by_role("button", name="Confirm Lot Selection").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
