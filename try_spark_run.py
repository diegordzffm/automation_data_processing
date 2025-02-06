import subprocess
import json

# Airflow API endpoint
airflow_url = "https://datamanagementDiego/airflow/api/v1/dags/spark_submit_example/dagRuns"

# Define the parameters for your SparkSubmitOperator task
task_name = "your_task_name"
jar_version = "1.0.0"  # Example jar version
target_table = "your_target_table"
spark_master = "yarn"  # Example spark master
conf_path = "/path/to/config/"
app_params = ["param1", "param2"]  # Example Spark app arguments
table = {'conf_file': 'ingestion.conf'}


spark_master = "spark://spark:7077"
dag_name = "BECRIS-ICR-new"
client = "anacredit-icr"
runtime = None
bucket = "s3bucket"
jar_version = Variable.get('JAR_VERSION')
module_id = 6600






# Create the payload for the DAG trigger
payload = {
    "conf": {
        "task_id": task_name.replace(" ", "_"),
        "execution_timeout": "1200",  # 20 minutes in seconds
        "pool": "spark_pool",
        "application": f"spark/app/ingestion/ingestion-il-{jar_version}.jar",
        "name": target_table.upper(),
        "conn_id": "spark_default",
        "verbose": 1,
        "repositories": "https://oss.sonatype.org/content/repositories/snapshots",
        "conf": {
            "spark.master": spark_master,
            "spark.driver.extraJavaOptions": f"-Dconfig.file={conf_path + table['conf_file']}",
            "spark.jars.packages": "com.microsoft.azure:spark-mssql-connector:1.0.1",
            "spark.driver.extraClassPath": "/usr/local/spark/resources/jars/postgresql-42.6.0.jar"
        },
        "java_class": "com.bfine.Main",
        "application_args": app_params
    }
}

# Convert payload to JSON string
payload_json = json.dumps(payload)

# Curl command to trigger the DAG
curl_command = [
    "curl", "-X", "POST", 
    airflow_url,
    "-H", "Content-Type: application/json",
    "-d", payload_json
]

# Execute the curl command using subprocess
try:
    result = subprocess.run(curl_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print("Curl Command Output:", result.stdout)
    if result.returncode == 0:
        print("DAG successfully triggered!")
    else:
        print(f"Error in triggering DAG: {result.stderr}")
except Exception as e:
    print(f"Exception occurred: {e}")
