from datetime import datetime

from airflow import DAG
from airflow.decorators import task
from airflow.models.baseoperator import chain
from airflow.providers.amazon.aws.hooks.s3 import S3Hook
from airflow.providers.amazon.aws.hooks.redshift import RedshiftSQLHook
from airflow.contrib.hooks.aws_hook import AwsHook
from airflow.providers.amazon.aws.operators.redshift_sql import RedshiftSQLOperator
from airflow.providers.amazon.aws.transfers.s3_to_redshift import S3ToRedshiftOperator

S3_BUCKET = "bucket-case-keycash"
S3_KEY = "csv/"
REDSHIFT_SCHEMA = "keycash_schema"
REDSHIFT_TABLE = "landing_table"

#creating task to takes data from s3 bucket
@task(task_id='setup__takes_data_from_s3')
def takes_data_from_s3():
    s3_hook = S3Hook()
    s3_hook.get_bucket(S3_BUCKET)

#creating the DAG
with DAG(
    dag_id="s3_to_redshift",
    start_date=datetime(2022, 2, 21),
    schedule_interval='30 19 21 02 mon',
    catchup=False,
    tags=['test'],
) as dag:
    takes_data_from_s3 = takes_data_from_s3()
    
    setup__task_create_table = RedshiftSQLOperator(
        sql=f'CREATE TABLE IF NOT EXISTS {REDSHIFT_SCHEMA}.{REDSHIFT_TABLE}(id VARCHAR PRIMARY KEY,name VARCHAR ( 20 ) NULL,idade integer NULL,credito_solicitado integer NULL,data_solicitacao VARCHAR NULL)',
        task_id='setup__create_table'
    )
        
    
    #sends data from s3 to the selected schema and table on redshift
    task_transfer_s3_to_redshift = S3ToRedshiftOperator(
        s3_bucket=S3_BUCKET,
        s3_key=S3_KEY,
        schema="keycash_schema",
        table=REDSHIFT_TABLE,
        copy_options=['csv'],
        task_id='transfer_s3_to_redshift',
    )
    

    chain(
        [takes_data_from_s3, setup__task_create_table],
        task_transfer_s3_to_redshift
    )
