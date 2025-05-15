# 📊 Job Security Dashboard: Retirement Patterns

This project is a data science exploration into **retirement patterns** among public employees in Brazil. The goal is to analyze trends and develop an interactive dashboard to visualize insights around job stability, aging workforce, and long-term employment.

---

## 🚀 Project Goals

- 🔍 Ingest, clean, and explore public retirement data from the Central Bank of Brazil
- 📈 Perform statistical analyses to reveal patterns in retirements by city, age group, or career length
- 🧮 Build a dashboard (in Jupyter and later as an API) to display findings interactively
- 🛠️ Enable scheduled updates and automation for ongoing data freshness

---

## 📦 Data Source

- [Central Bank of Brazil - Dados Cadastrais de Aposentados](https://dadosabertos.bcb.gov.br/dataset/dados-cadastrais-de-aposentados)
- Format: CSV
- Content: Retirement registration data of Central Bank employees

---

## 🧱 Project Structure

```
job-security-dashboard-brazil/
│
├── data/                      # Raw and processed datasets
├── notebooks/                 # Jupyter notebooks for exploration
├── src/                       # Python scripts for data ingestion, cleaning
├── api/                       # API to serve analysis (coming soon)
├── dashboard/                 # Dashboard app (Jupyter + Streamlit or Dash)
├── README.md                  # You’re here!
├── requirements.txt           # Python dependencies
└── .gitignore
```

## 🧰 Tools & Libraries
- Python 3.10.6
- pandas
- numpy
- Jupyter Notebook
