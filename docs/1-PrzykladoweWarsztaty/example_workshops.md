## **Definicje**
1. **Data Lake** - skalowalna przestrzeń która przechowauje dane surowe. Data lake bazuje na systemach plików i umieszczana jest na klastrach (HDFS, Cloud e.g. ADSL Gen 2)
2. **Data Warehouse** - przestrzeń do składowania danych ustrukturyzowanych (tabularycznych). Zwykle umieszczona na jednej maszynie, a co za tym idzie mało skalowalna.
3. **Lakehouse** - or data lakehouse - Oferuje najlepsze cechy Data Lake i Data Warehouse.
4. **Delta lake** - storage layer for lakehouse based on open standard Delta Lake (parquet data files  with file-based transatcion log for ACID transactions)
5. **Databricks** - Unified platform built on Lakehouse Architecture with default format: Delta [Delta official](https://delta.io/ "Delta format official docs")


![Lakehouse](assets/lakehouse.png)

## **Architektura Medalionu**
To wzorzec projektu służący do organizowania danych w Lakehouse. Składa się z trzech warstw:
Bronze => Silver => Gold

![Medalion Architecture](assets/medalion_architecture.png)

| Bronze                                                                    | Silver                                 | Gold                                                                                        |
|:--------------------------------------------------------------------------|:---------------------------------------|:--------------------------------------------------------------------------------------------|
| Raw data, where data comes from external systems.                         | Cleansed and preprocessed data         | "Project - specific" (Product). Usually for reporting purposes (fact and dimensions tables) |
| Managed by Data Engineers and Administrators with no access to other uses | Source data for self-service analytics |                                                                                             |

<div style='text-align: center; '> Table 1: Opis tabel w architekturze medalionu</div>














