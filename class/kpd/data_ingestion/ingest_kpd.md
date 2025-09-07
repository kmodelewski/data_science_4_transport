# Ingest data from S3

```sql
%sql
CREATE OR REPLACE TABLE transportation_dept.bronze.kpd
AS
SELECT
  *,  input_file_name() AS source_file, _metadata
FROM read_files(
  'dbfs:/Volumes/transportation_dept/bronze/s3/kpd/csv/',
  format => 'csv',
  header => true,
  mode => 'PERMISSIVE',
  columnNameOfCorruptRecord => "_corrupt_record",
  schema=>'podmiot STRING, klasa STRING, typ STRING, poczatek_utrudnienia STRING,
  koniec_utrudnienia STRING, data_wygasniecia DATE, nr_drogi STRING, nazwa_ulicy STRING,
  pikietaz_poczatkowy DOUBLE, dlugosc_utrudnienia DOUBLE, kierunek STRING, aktywne STRING,
  dlugosc_gograficzna DOUBLE, szerokosc_geograficzna DOUBLE, opis_utrudnienia STRING,
  porada_dla_kierowcow STRING, s3_ingest_timestamp TIMESTAMP, _corrupt_record STRING'

)
```

MERGE INTO
https://www.startdataengineering.com/post/create-scd2-table-with-merge-into-with-spark-iceberg/ 