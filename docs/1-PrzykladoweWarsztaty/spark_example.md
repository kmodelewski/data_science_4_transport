## Apache spark engine


Heavy workloads and growing business needs requires another aproach to computing. One mainframe computers are expensive
and diffcult to upgrade. Below example of Apache spark architecture.

![Laekhouse](assets/spark_arch.png)

Partitioning (Huge table - partition - files). Subdividing data by column. Do not use partition for high 
data cardinality use. load_date, country. Problem malych plikow. Avoid column with high skewness or null values.


|id | lane_no | vehicle_count | sys_load_date |
|:--|:--|:--|:--------------|
|1|1|12| 2025-03-24    |

``` py title="partitionBy"
df.write.format("delta").partitionBy("sys_load_date").saveAsTable("traffic_monitoring")
```