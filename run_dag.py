username = "diego.rodriguez@regnology.net"
password = "Frankfurt#60486"


import requests
from datetime import datetime

# Airflow server URL
airflow_url = "https://acceptance.b-fine.be/airflow/tree?dag_id=ANACREDIT-ICR_BECRIS-ICR-NEW"

# Current date
current_date = datetime.now().strftime('%Y-%m-%d')

# Payload with parameters
payload = {
    "conf": {
    "db": "rl",
    "entity": "B-Fine",
    "lot": "1",
    "lot_table": "AnaLot",
    "reporting_date": "current:date",
    "source_sys": "Manual"
  }
}



# Headers
headers = {
    "Content-Type": "application/json",
    "Accept: application/json",
    "Authorization": "Bearer YOUR_API_TOKEN"  # Replace with your Airflow API token
}

# Trigger the DAG
response = requests.post(airflow_url, json=payload, headers=headers)

# Check the response
if response.status_code == 200:
    print("DAG triggered successfully!")
    print("Response:", response.json())
else:
    print("Failed to trigger DAG")
    print("Status Code:", response.status_code)
    print("Response:", response.text)
