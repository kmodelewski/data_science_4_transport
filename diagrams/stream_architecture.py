from diagrams import Cluster, Diagram
from diagrams.azure.analytics import Databricks
from diagrams.custom import Custom
from diagrams.azure.analytics import EventHubs, DataExplorerClusters
from diagrams.onprem.monitoring import Grafana
from diagrams.azure.storage import TableStorage

with Diagram("Streaming Analytics Architecture", show=True):



    with Cluster('Streaming source'):
        stream = [Custom("Kafka", "./assets/kafka.png"),
        EventHubs('Azure Event Hub'),
        DataExplorerClusters('Azure Data Explorer')]

    with Cluster("Analytics and reporting layer"):
        dbx= Databricks("Databricks")
    #
    with Cluster("Reporting Layer"):
        reporting = [Grafana('grafana'),Custom("Power Bi", "./assets/pbi.png")]

    with Cluster('Sharing layer'):
        table = TableStorage('Delta Table')

    # Chain connections between lists and nodes
    stream >> dbx >> reporting
    dbx >> table

    

