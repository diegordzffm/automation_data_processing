import requests
import subprocess

airflow_server_url = "https://datamanagementDiego/airflow"
dag_id = "ANACREDIT_RL-INGESTION-NEW-CREDIT-INSTITUTIONS"
username = "datamanagementDiego.net"
password = "Fccxccxxx6"
#CURL Command: This command triggers the DAG using Airflow's REST API. It uses basic authentication, so you need to provide your username and password
curl_command = [
    "curl", "-X", "POST",
    f"{airflow_server_url}/api/v1/dags/{dag_id}/dagRuns",
    "-u", f"{username}:{password}",
    "-H", "Content-Type: application/json",
    "-d", '{"conf": {"email": "datamanagementDiego.net", "entity": "Bxxxxa", "lot": 1, "reporting_date": "2024-12-11","source_system": "Manual"}}'  # Optional: Use {"conf":{}} to pass additional configurations to your DAG
]
#https://datamanagementDiego/airflow/api/v1/dags/ANACREDIT-ICR_BECRIS-ICR-NEW/dagRuns
#Run the Command: The subprocess.run function executes the CURL command. It captures the output and any potential errors, which are then printed.
try:
    result = subprocess.run(curl_command, capture_output=True, text=True)
    print("Status Code:", result.returncode)
    print("Response:", result.stdout)
    if result.stderr:
        print("Error:", result.stderr)
except Exception as e:
    print("An error occurred:", str(e))


#curl -X GET "https://datamanagementDiego/airflow/api/v1/dags" \
#-H "Authorization: Basic $(echo -n 'datamanagementDiego.net:Frsssdaassasd' | base64)"'''

#to get the taskinstances
#https://datamanagementDiego/airflow/api/v1/dags/ANACREDIT-ICR_BECRIS-ICR-NEW/dagRuns/manual__2024-09-10T07:09:04.965432+00:00/taskInstances

#to get the lots

# curl -X GET "https://datamanagementDiego/airflow/api/v1/dags/ANACREDIT-ICR_BECRIS-ICR-NEW/dagRuns/manual__2024-09-10T07:09:04.965432+00:00/taskInstances" -H "Authorization: Basic $(echo -n 'datamanagementDiego.net:datamanagementDiego' | base64)"

#curl -X GET "https://datamanagementDiego/airflow/api/v1/dags/ANACREDIT-ICR_BECRIS-ICR-NEW" -H "Authorization: Basic $(echo -n 'datamanagementDiego.net:datamanagementDiego' | base64)"

 #curl -X GET "https://datamanagementDiego/airflow/api/v1/dags/ANACREDIT-ICR_BECRIS-ICR-NEW/dagRuns/manual__2024-09-10T07:09:04.965432+00:00/taskInstances/update_lot" -H "Authorization: Basic $(echo -n 'datamanagementDiego.net:datamanagementDiego' | base64)"  

'''
import requests
from requests.auth import HTTPBasicAuth

# Define the Airflow server URL and endpoint to trigger a DAG run
airflow_url = "https://datamanagementDiego/airflow/api/v1/dags/ANACREDIT-ICR_BECRIS-ICR-NEW/dagRuns"

# Replace with your Airflow username and password
username = "datamanagementDiego.net"
password = "datamanagementDiego"

# Basic authentication setup
auth = HTTPBasicAuth(username, password)

# Headers to specify content type
headers = {
    "Content-Type": "application/json"
}

# Optional: Payload to customize the DAG run (for example, setting the execution_date)
payload = {
    "conf": {
        # Add any parameters you want to pass to the DAG run
        "email": "datamanagementDiego.net",
        "entity": "B-Fine",
        "lot": 1,
        "reporting_date": "2024-08-23",
        "source_system": "Manual"
    }
}

# Trigger the DAG by sending a POST request
response = requests.post(airflow_url, auth=auth, headers=headers, json=payload)

# Check if the request was successful
if response.status_code == 200:
    print("DAG triggered successfully!")
    print("Response:", response.json())  # Print the JSON response if available
else:
    print(f"Failed to trigger DAG. Status code: {response.status_code}")
    print("Response:", response.text)
'''