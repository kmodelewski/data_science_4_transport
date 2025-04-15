## External table

Tabla with data in external location (on external storage like  Azure Storage Account -> abfss://)
Use external table only when you require direct access to the data outside of DBX clusters and warhouses.

DROP TABLE >talbe_name> does not delete underlying data. 

We have to create external location and then External table
### External Table 
```sql
CREATE TABLE <table_name>
    (id INTEGER, name STRING)
USING CSV 
OPTIONS (
    delimiter =";",
    header = "true"
         )
LOCATION "abfss://" --in case of Azure ADSL2

```
Necessary to have credentials to External Locations. We can "convert" csv t delta lake format.

#### Built-In functions

```sql
--SPARK SQL FUNCTIONS
current_timestamp() --records the timestamp
input_file_name() --records the source data file to each record 
```

### SPARK STRUCTURED STREAMING


### DELTA LIVE TABLES




