from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'prasanna',
    'start_date': datetime(year=2024, month=7, day=27),
    'catchup': False
}

dag = DAG(
    'hello_world',
    default_args= default_args,
    schedule= timedelta(days=1)
)

t1 = BashOperator(
    task_id = 'hello_world',
    bash_command= 'echo "Hello World"',
    dag = dag
)

t2 = BashOperator(
    task_id = 'hello_dml',
    bash_command= 'echo "Hello Prasanna"',
    dag = dag
)

t1 >> t2