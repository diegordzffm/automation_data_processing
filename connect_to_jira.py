import requests


url = "https://jira.regnology.net"
username = "diego.rodriguez@regnology.net"
password = "Fitness70569"

response = requests.get(url, auth=(username, password))
print(response.json())


'''jira token: NzUwMTI4MTg4OTYzOiZFffdb7Zvdc/0RCgjUs06zPuyv'''