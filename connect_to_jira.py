import requests


url = "datamanagementDiego"
username = "datamanagementDiego.net"
password = "xxxxxx"

response = requests.get(url, auth=(username, password))
print(response.json())


'''jira token: NxxxxxxxxzPuyv'''