import requests
import json
from fpdf import FPDF

# JIRA API Credentials
JIRA_URL = "https://jira.regnology.net/"
JIRA_EMAIL = "diego.rodriguez@regnology.net"
JIRA_API_TOKEN = "NzUwMTI4MTg4OTYzOiZFffdb7Zvdc/0RCgjUs06zPuyv"
PROJECT_KEY = "RRH"
REPOSITORY_NAME = "BECRIS_ICR"  # The name of the Test Repository

# JIRA API Endpoints
TEST_REPOSITORY_ENDPOINT = f"{JIRA_URL}/rest/api/2/search"

# Basic Authentication for JIRA API
auth = (JIRA_EMAIL, JIRA_API_TOKEN)

# Query to find all Xray Tests in the Test Repository
jql_query = f'project = "{PROJECT_KEY}" AND issuetype = "Test" AND "Test Repository" ~ "{REPOSITORY_NAME}"'

# Search for Tests in the Test Repository
response = requests.get(
    TEST_REPOSITORY_ENDPOINT,
    params={'jql': jql_query},
    auth=auth,
    headers={'Content-Type': 'application/json'}
)

# Check if the request was successful
if response.status_code == 200:
    test_issues = response.json().get('issues', [])
    print(f"Found {len(test_issues)} test issues in repository '{REPOSITORY_NAME}'.")

    # Iterate over each test issue and retrieve the "Test Details"
    for test_issue in test_issues:
        test_key = test_issue['key']
        test_summary = test_issue['fields']['summary']
        test_description = test_issue['fields']['description']

else:
    print(f"Failed to retrieve tests from repository '{REPOSITORY_NAME}'. Status Code: {response.status_code}")
    print(response.text)

'''


# Check if the request was successful


        # Create a PDF for each test description
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        # Add content to PDF
        pdf.cell(200, 10, txt=f"Test Key: {test_key}", ln=True)
        pdf.cell(200, 10, txt=f"Test Summary: {test_summary}", ln=True)
        pdf.ln(10)
        pdf.multi_cell(0, 10, txt=f"Test Details:\n\n{test_description}")

        # Save PDF file
        pdf_filename = f"{test_key}.pdf"
        pdf.output(pdf_filename)
        print(f"Saved: {pdf_filename}")

"https://jira.regnology.net/rest/api/2/project/16204","id":"16204","key":"RRH","name":"Regnology Reporting Hub"

'''


