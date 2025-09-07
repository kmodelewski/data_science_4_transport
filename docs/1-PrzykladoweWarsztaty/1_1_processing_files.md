
## File sources

### SPARK SQL
#### 1. Parquet files
```sql
--INFO: this not relates to SQL ENDPOINT (querying warehouse)

--parquet from abfss
SELECT * FROM parquet.`abfss://container@storageaccount.dfs.core.windows.net/xxxx`
--parquet from abfss (internal storage - Databricks File System like HDFS)
SELECT * FROM parquet.`dbfs:/user/hive/warehouse/my_table/file_test.snappy.parquet`
```
#### 1. CSV files
```sql
--INFO: this not relates to SQL ENDPOINT (querying warehouse)

--parquet from abfss
SELECT * FROM read_files(`abfss://container@storageaccount.dfs.core.windows.net/xxxx`,
    format => 'csv',
    sep => ';',
    header => true,
    mode => 'FAILFAST'
    
    
--parquet from abfss (internal storage - Databricks File System like HDFS)
SELECT * FROM parquet.`dbfs:/user/hive/warehouse/my_table/file_test.snappy.parquet`
```

