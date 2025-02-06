#from jira import JIRA
#from jira.exceptions import JIRAError
import requests
from requests.auth import HTTPBasicAuth
import urllib3
import subprocess
import json

JIRA_URL = "https://jira.dxxxxxxxxxxxxxxxxxxx.net/rest/api/2/search"
JIRA_EMAIL = "ddxxxxxxxxxxxxxxxxxxx"
JIRA_USERNAME = "dxxxxxxxxxxxxxxxxxxx"
JIRA_PASSWORD = "dxxxxxxxxxxxxxxxxxxx#dxxxxxxxxxxxxxxxxxxx"
JIRA_API_TOKEN = "dxxxxxxxxxxxxxxxxxxx/dxxxxxxxxxxxxxxxxxxxx"

try:
    jira = JIRA(JIRA_URL, auth = HTTPBasicAuth(jira_username, JIRA_API_TOKEN))
    # If the above connection is successful, print a success message
    print("Successfully connected to Jira!")
    
except JIRAError as e:
    print(f"Failed to connect to Jira: {e}")
'''import requests
from requests.auth import HTTPBasicAuth

def get_jira_issue_title(issue_key):
    """Gets the title of a JIRA issue using the JIRA API.

    Args:
        issue_key (str): The key of the JIRA issue.

    Returns:
        str: The title of the JIRA issue.
    """

    # Replace with your JIRA base URL, email, and API token
    jira_base_url = "https://dxxxxxxxxxxxxxxxxxxx.dxxxxxxxxxxxxxxxxxxx.net/rest/api/2"
    email = "dxxxxxxxxxxxxxxxxxxx"
    api_token = "dxxxxxxxxxxxxxxxxxxx/dxxxxxxxxxxxxxxxxxxx"
    PROJECT_KEY = "dxxxxxxxxxxxxxxxxxxx"

    # Construct the authentication header
    auth = HTTPBasicAuth(email, api_token)

    # Construct the API endpoint URL
    url = f"{jira_base_url}issue/{issue_key}"

    # Make the API request
    response = requests.get(url, headers=auth)

    # Check if the request was successful
    if response.status_code == 200:
        # Extract the issue title from the response JSON
        issue_data = response.json()
        return issue_data['fields']['summary']
    else:
        raise Exception(f"Failed to get issue title: {response.status_code} - {response.text}")

# Example usage
issue_key = "RRH-6734"
title = get_jira_issue_title(issue_key)
print(title)'''

'''curl -X POST {{baseUrlOfYourInstance}}/rest/pat/latest/tokens -H "Content-Type: application/json" -d '{"name": "tokenName","expirationDuration": 90}' --user "username:password"


curl -u username:password -X GET -H "Content-Type: application/json" http://localhost:8080/rest/api/2/issue/createmeta

curl -u D7ESq htth
'''
