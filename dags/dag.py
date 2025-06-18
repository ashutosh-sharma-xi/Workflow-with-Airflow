from airflow.decorators import dag

from datetime import datetime
default_args = {}

# create a dag
etl_dag = dag('etl_dag' , default_args=default_args,    )