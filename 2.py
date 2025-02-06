import subprocess
import json

# Define the URL and credentials
url = "https://datamanagementDiego/rest/api/2/search"
username = "datamanagementDiego.net"  # Replace with your JIRA username or email
api_token = "OTdatamanagementDiegos6N8y66i7ESq"  # Replace with your JIRA API token

# Construct the curl command
curl_command = [
    "curl",
    "-u", f"{username}:{api_token}",
    "-H", "Accept: application/json",
    url
]

try:
    # Execute the curl command
    result = subprocess.run(curl_command, capture_output=True, text=True, check=True)
    
    # Check if the request was successful
    if result.returncode == 0:
        print("Request successful!")
        # Output the response (you can process it as needed)
        print(result.stdout)
    else:
        print(f"Request failed with return code {result.returncode}")
        print(result.stderr)
except subprocess.CalledProcessError as e:
    print(f"An error occurred while executing curl: {e}")



 