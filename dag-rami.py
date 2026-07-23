from datetime import datetime
from airflow import DAG
from airflow.utils.trigger_rule import TriggerRule
from airflow.operators.bash import BashOperator
with DAG(
    dag_id="dag_formation_INCROYABLEQUIFAITHELLO",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
    tags=["guide"],
) as dag:
    task1 = BashOperator(
        task_id="task1",
        bash_command="echo 'Airflow est prêt sur cette EC2'; hostname; date"
    )
    task2 = BashOperator(
        task_id="task2",
        bash_command="wesh"
    )
    task3 = BashOperator(
        task_id="task3",
        bash_command="hostname",
        trigger_rule=TriggerRule.ONE_SUCCESS
    )
    task4 = BashOperator(
        task_id="exitone",
        bash_command="exit 1",
        trigger_rule=TriggerRule.ALL_FAILED
    )
    ([task1, task2] >> [task3, task4])
