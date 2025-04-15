## Medalion Architecture
Design pattern to organize data in Lakehouse using three layers:
Bronze => Silver => Gold

![Medalion Architecture](assets/medalionArchitecture.png)

| Bronze                                                                    | Silver                                 | Gold                                                                                        |
|:--------------------------------------------------------------------------|:---------------------------------------|:--------------------------------------------------------------------------------------------|
| Raw data, where data comes from external systems.                         | Cleansed and preprocessed data         | "Project - specific" (Product). Usually for reporting purposes (fact and dimensions tables) |
| Managed by Data Engineers and Administrators with no access to other uses | Source data for self-service analytics |                                                                                             |

<div style='text-align: center; '> Table 1: Description of Medalion layers</div>



Data Lake (storage, external storage + warehouse (plus sql endpoint))

