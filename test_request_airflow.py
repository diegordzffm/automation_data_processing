import requests
from playwright.sync_api import sync_playwright

# Step 1: Perform login with credentials
login_url = "https://acceptance.b-fine.be/connect/login"
credentials = {
    "username": "diego.rodriguez@regnology.net",
  	"password": "Frankfurt#60486"
}

# Send a POST request to login
with requests.Session() as session:
    response = session.post(login_url, data=credentials)
    
    if response.status_code == 200:
        print("Login successful!")
        
        # Get cookies or session info if needed
        cookies = session.cookies.get_dict()
    else:
        print(f"Login failed with status code: {response.status_code}")
        exit()

# Step 2: Open the dashboard with Playwright using the same session
dashboard_url = "https://acceptance.b-fine.be/app/dashboard"

def open_dashboard():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()

        # Add cookies to the Playwright browser context
        for cookie in cookies:
            context.add_cookies([{
                'name': cookie,
                'value': cookies[cookie],
                'domain': '.acceptance.b-fine.be',
                'path': '/',
                'httpOnly': True,
                'secure': True
            }])

        # Open a new page and navigate to the dashboard
        page = context.new_page()
        page.goto(dashboard_url)

        # Keep the browser open
        page.wait_for_timeout(10000)

        browser.close()

open_dashboard()





#works ok
'''import requests
from requests.auth import HTTPBasicAuth

# Server URL
url = "https://acceptance.b-fine.be/connect/login"

# Credentials
username = "diego.rodriguez@regnology.net"
password = "Frankfurt#60486"

# Send a GET request with basic authentication
response = requests.get(url, auth=HTTPBasicAuth(username, password))

# Check if access was successful
if response.status_code == 200:
    print("Access was successful!")
else:
    print(f"Failed to access the server. Status code: {response.status_code}")
https://acceptance.b-fine.be/app/dashboard'''