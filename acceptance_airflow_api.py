https://xxxxxxxxxxx/airflow/api/v1/connections


#working get list of DAGs
curl -X GET "https://xxxxxxxxxx/airflow/api/v1/dags" \
-H "Authorization: Basic $(echo -n 'dxxxxxxxx:xxxxxxxxx' | base64)"


ping https://xxxxxxxxxxe





5. get status of DAG Run

curl -X GET "https://axxxxxxxx/dagRuns/manual__2024-09-04T10:30:37+00:00" \
-H "Authorization: Basic $(echo -n 'dxxxxxxxxxxxxxxxxxxx' | base64)"




get acceptance or airflow port


SSH Tunneling: Set up an SSH tunnel to the remote Airflow server:

ssh -L dxxxxxxxxxxxxxxxxxxx

ssh -L 8080:localhost:8080 dxxxxxxxxxxxxxxxxxxx@34.224.76.131
