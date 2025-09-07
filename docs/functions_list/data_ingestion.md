# Function list

1. read_files()

* składnia: read_files(path [, option_key => option_value ] [...])
* opis: wczytuje pliki z lokalizacji chmurowych. Rozszerzenia plików:
JSON, CSV, XML, TEXT, BINARYFILE, PARQUET, AVRO, and ORC. 
  * mode => 'FAILFAST' - przerywa proces wczytywania wyrzucając błąd
  * mode => 'PERMISSIVE' - wstawia null
  * mode => 'DROPMALFORMED' - ignoruje złe wiersze
  * komentarz: _metadata jest struct i zawiera file_path, file_name...
* dokumentacja: https://docs.databricks.com/aws/en/sql/language-manual/functions/read_files

  2.  .selectExpr("*", "_metadata as source_metadata") \