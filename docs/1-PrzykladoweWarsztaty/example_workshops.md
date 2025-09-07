## **Definicje**
1. **Data Lake** - skalowalna przestrzeń która przechowauje dane surowe. Data lake bazuje na systemach plików i umieszczana jest na klastrach (HDFS, Cloud e.g. ADSL Gen 2)
2. **Data Warehouse** - przestrzeń do składowania danych ustrukturyzowanych (tabularycznych). Zwykle umieszczona na jednej maszynie, a co za tym idzie mało skalowalna.
3. **Lakehouse** - or data lakehouse - Oferuje najlepsze cechy Data Lake i Data Warehouse.
4. **Delta lake** - storage layer for lakehouse based on open standard Delta Lake (parquet data files  with file-based transatcion log for ACID transactions)
5. **Databricks** - platforma danych zbudowana na bazie Lakehouse z domyślnym formatem danych Delta [Delta official](https://delta.io/ "Delta format official docs")


![Lakehouse](assets/lakehouse.png)

## **Architektura Medalionu**
To wzorzec projektu służący do organizowania danych w Lakehouse. Składa się z trzech warstw:
Bronze => Silver => Gold

![Medalion Architecture](assets/medalion_architecture.png)

| Bronze                                                | Silver                                       | Gold                                                  |
|:------------------------------------------------------|:---------------------------------------------|:------------------------------------------------------|
| Dane surowe, pochodzące najczęściej z innych systemów | Wstępnie wyczyszczone i przeprocesowane dane | Najczęściej tabele faktów i wymiarów pod raportowanie |
| Zarządzanie przez Inżynierów Danych                   | Dane źródłowe do analityki                   |                                                       |

<div style='text-align: center; '> Table 1: Opis tabel w architekturze medalionu</div>














