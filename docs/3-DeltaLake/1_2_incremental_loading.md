## Increamental Loading
Create table and load to it data incrementally

Limitations:
- loaded data should have the same schema
- data deduplication should be handled downstream because copy into load new files
- cannot re-ingest readed files
- idempotant operation - re-run do not load readed files (preventig data deduplication on file level)



### COPY INTO
```sql
COPY INTO <table>
 FROM 'path'
 FILEFORMAT = parquet
 COPY_OPTIONS ('mergeSchema' = 'true') --key value pairs

```
There is a _rescued_data column to indicate data that do not match schema

### COPYING CSV
```sql
COPY INTO <table_name>
 (SELECT * ,
    cast(cast(column/1e5 AS TIMESTAMP) AS DATE) new_date_column,
    current_timestamp() operation_timestamp,
    input_file_name() source_file --dbfs:/mnt/...
FROM ''
FILEFORMAT = PARQUET
COPY_OPTIONS ('mergeSchema' = 'true')
)
```

### AUTOLOADER
```sql


```

### SPARK STRUCTURED STREAMING


### DELTA LIVE TABLES




