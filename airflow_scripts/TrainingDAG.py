from datetime import timedelta, datetime
import airflow
from airflow import DAG
from airflow.providers.ssh.operators.ssh import SSHOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'start_date': datetime.now() - timedelta(minutes=20),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}
dag = DAG(
    dag_id='TrainingDAG',
    default_args=default_args,
    schedule_interval='0,10,20,30,40,50 * * * *',
    dagrun_timeout=timedelta(seconds=120),
)

# commands
uploadDataToMinIO = "python3 writeDataToMiniIO.py"
KILabTraining = "python3 /opt/KI_Lab_training.py"
#createModelCard = "docker exec -it myflow_server python3 createModelCard.py"
#deployModel = "docker exec -it myflow_server python3 deployModel.py"
# dockerHelloWorld = "docker run hello-world"


# Step 1 - Upload Data from Database to MinIO
t1 = SSHOperator(
    ssh_conn_id='influxdb', task_id='uploadDbData', command=uploadDataToMinIO, dag=dag
)

# Step 2 - run AutoML Script
t2 = SSHOperator(
    ssh_conn_id='automl', task_id='runAutoML', command=KILabTraining, dag=dag
)

# Step 3 - create ModelCard for Model
#t3 = SSHOperator(
#    ssh_conn_id='cogitat', task_id='createModelCard', command=createModelCard, dag=dag
#)

# Step 4 - Deploy Model to production
#t4 = SSHOperator(
#    ssh_conn_id='cogitat', task_id='deployModel', command=deployModel, dag=dag
#)


t1 >> t2 #>> t3 >> t4
