from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator
with DAG(
    dag_id="dag_formation_INCROYABLEQUIFAITHELLO",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
    tags=["guide"],
) as dag:
    hello = BashOperator(
        task_id="hello",
        bash_command="echo 'Airflow est prêt sur cette EC2'; hostname; date"
    )
    liste = BashOperator(
        task_id="liste",
        bash_command="ls -la"
    )
    show_hostname = BashOperator(
        task_id="show_hostname",
        bash_command="hostname"
    )
    hello >> liste >> show_hostname
