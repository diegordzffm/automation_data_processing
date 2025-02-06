https://acceptance.b-fine.be/airflow/api/v1/connections


#working get list of DAGs
curl -X GET "https://acceptance.b-fine.be/airflow/api/v1/dags" \
-H "Authorization: Basic $(echo -n 'diego.rodriguez@regnology.net:Frankfurt#60486' | base64)"


ping https://acceptance.b-fine.be

34.224.76.131

admin@regnology.net
Admin@admin123

5. get status of DAG Run

curl -X GET "https://acceptance.b-fine.be/airflow/api/v1/dags/ANACREDIT-ICR_BECRIS-ICR-NEW/dagRuns/manual__2024-09-04T10:30:37+00:00" \
-H "Authorization: Basic $(echo -n 'diego.rodriguez@regnology.net:Frankfurt#60487' | base64)"




get acceptance or airflow port


SSH Tunneling: Set up an SSH tunnel to the remote Airflow server:

ssh -L acceptance.b-fine.be diego.rodriguez@regnology.net@34.224.76.131

ssh -L 8080:localhost:8080 admin@regnology.net@34.224.76.131
