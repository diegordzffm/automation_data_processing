import requests
from requests.auth import HTTPBasicAuth
import json
import csv
import base64
from jira import JIRA
import urllib3

def JiraBoard():
  JIRA_URL = "https://jira.regnology.net/rest/api/2/issue/RRH-7614"
  JIRA_EMAIL = "diego.rodriguez@regnology.net"
  #username = "DiegoFFM"
  #api_token = "OTI3MzM4MjU5MzcyOq7jc8xGcgQXJsLYs6N8y66i7ESq"
  #JIRA_PASSWORD = "kim#60486"
  username = diego.rodriguez
  JIRA_API_TOKEN = "NzUwMTI4MTg4OTYzOiZFffdb7Zvdc/0RCgjUs06zPuyv"
#PROJECT_KEY = "RRH"
#REPOSITORY_NAME = "BECRIS_ICR"  # The name of the Test Repository
  session = requests.Session()
  session.auth = HTTPBasicAuth(username, JIRA_API_TOKEN)
  headers = {
    "Accept": "application/json"
  }
  response = session.get(JIRA_URL, headers=headers)
  if response.status_code == 200:
    print("Request successful!")
    #print(response.json())  # Assuming the response is JSON
  else:
    print(f"Request failed with status code {response.status_code}")
    print(response.text)


# Step 1: Convert list to string
  #auth_jira = HTTPBasicAuth(JIRA_EMAIL, JIRA_API_TOKEN)

# Step 2: Use the URL with requests
  #auth_jira = JIRA(JIRA_URL, basic_auth=(JIRA_EMAIL, JIRA_API_TOKEN))
  #response = requests.get(JIRA_URL, basic_auth(JIRA_EMAIL, JIRA_API_TOKEN))

# Print the status code or the content of the response
  #print(response.status_code)
  #print(response.content)

JiraBoard()
'''# JIRA API Endpoints
#TEST_REPOSITORY_ENDPOINT = f"{JIRA_URL}/rest/api/2/search"

# Basic Authentication for JIRA API
auth = HTTPBasicAuth(JIRA_EMAIL, JIRA_API_TOKEN)
#make API request 
response = requests.get(JIRA_URL, auth)
# Check if the request was successful
if response.status_code == 200:
    issue_data = response.json()
    # Print the issue title (summary)
    print("Title (Summary):", issue_data["fields"]["summary"])
else:
    print(f"Failed to retrieve issue. Status code: {response.status_code}")
    print(response.text)'''






# Query to find all Xray Tests in the Test Repository
#jql_query = f'project = "{PROJECT_KEY}" AND issuetype = "Test" AND "Test Repository" ~ "{REPOSITORY_NAME}"'

# Search for Tests in the Test Repository
'''response = requests.get(
    TEST_REPOSITORY_ENDPOINT,
    params={'jql': jql_query},
    auth=auth,
    headers={'Content-Type': 'application/json'}
)
'''
