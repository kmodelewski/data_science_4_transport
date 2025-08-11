from diagrams import Cluster, Diagram
from diagrams.azure.analytics import Databricks
from diagrams.azure.storage import StorageAccounts
from diagrams.aws.storage import Storage as AWSStorage
from diagrams.gcp.storage import Storage as GCPStorage
from diagrams.generic.storage import Storage as GenericStorage
from diagrams.custom import Custom
from diagrams.azure.storage import TableStorage
from diagrams.onprem.workflow import Nifi

from diagrams.onprem.workflow import Airflow
from diagrams.onprem.monitoring import Grafana
from diagrams.onprem.analytics import Hadoop
from diagrams.onprem.analytics import Spark

with Diagram("Batch Analytics Architecture", show=True):

    with Cluster("Orchestration Layer"):
        airflow = Airflow("Airflow")


    with Cluster("Cloud Ingestion Layer"):
        cloud_storage = [StorageAccounts('Azure'),AWSStorage('AWS'), GCPStorage('GCP')]

    with Cluster("OnPrem Ingestion Layer"):
         hadoop = [Hadoop("HDFS"), GenericStorage('Local files')]


    with Cluster("Analytics and reporting layer"):
        dbx= Databricks("Databricks")
        spark = Spark("Apache Spark")
    #
    with Cluster("Reporting Layer"):
        reporting = [Grafana('grafana'),Custom("Power Bi", "./assets/pbi.png")]

    with Cluster('Sharing layer'):
        table = TableStorage('Delta Table')

    # Chain connections between lists and nodes
    cloud_storage >> dbx
    dbx >> reporting
    dbx >> table
    hadoop >> airflow >> cloud_storage


