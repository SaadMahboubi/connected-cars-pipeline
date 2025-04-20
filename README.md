# Connected Cars Data Pipeline 🚗

Pipeline complet sur GCP pour ingérer, transformer et analyser des données de voitures connectées.

## Stack
- GCP : GCS, BigQuery, Cloud Composer
- Python
- Airflow
- Terraform (infra-as-code)
- SQL

## Étapes
1. Génération de données JSON simulées
2. Upload sur GCS
3. Ingestion dans BigQuery
4. Transformation SQL
5. Orchestration avec Airflow

## Structure du projet
- `scripts/` : Scripts de génération et upload
- `data/` : Données JSON simulées
- `dags/` : DAG Airflow
- `sql/` : Transformations SQL
- `terraform/` : Infrastructure GCP
- `config.py` : Variables globales
