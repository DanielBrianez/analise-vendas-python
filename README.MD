````md
# 📊 Sales Data Analysis Pipeline with Python, SQL and Pandas

End-to-end sales data analysis project developed with Python, Pandas and Matplotlib, featuring data cleaning, exploratory data analysis (EDA), automated chart generation and sales insights extraction.

This project simulates a real-world data analysis pipeline, including:

- Data extraction from Excel
- Data cleaning and preprocessing
- Exploratory Data Analysis (EDA)
- Automated chart generation
- SQLite database integration
- SQL-based analysis
- Automated report generation

---

# 🚀 Technologies Used

- Python
- Pandas
- Matplotlib
- OpenPyXL
- Excel
- SQLite

---

# 📂 Project Structure

```bash
sales-analysis-python/
│
├── graficos/
│   ├── grafico_vendas.png
│   ├── grafico_categoria.png
│   ├── grafico_canais.png
│   └── sql_total_vendas_por_vendedor.png
│
├── sales_analysis.py
├── sales_sql_analysis.py
├── sales_data.xlsx
├── sales.db
├── relatorio_vendas.xlsx
├── README.md
├── LICENSE
```

---

# 📊 Features

## ✔ Data Import
Reads sales data directly from an Excel file using Pandas.

## ✔ Data Cleaning
- Converts inconsistent values to numeric
- Handles invalid data using `errors="coerce"`
- Replaces missing values (`NaN`) with the column average

## ✔ Exploratory Data Analysis (EDA)
Performs:
- Sales aggregation
- Grouping and filtering
- Ranking analysis
- Category analysis

## ✔ Automated Reporting
Exports processed data into structured Excel reports.

## ✔ Data Visualization
Generates automated sales charts using Matplotlib.

## ✔ Image Export
Automatically saves generated charts as PNG images.

## ✔ SQL Integration
Stores and analyzes data using SQLite and SQL queries.
---

# 📈 Analyses Performed

### Total Sales by Sales Representative

Ranks sales reps by total revenue.

### Average Sales by Product Category

Calculates average sales value for each category.

### Sales Filtering

Filters:

* Sales above specific values
* Specific sales reps and categories

### Sales Ranking

Creates a ranking by:

* Sales Representative
* Product Category

---

# 📤 Generated Files

The project automatically generates:

```bash
relatorio_vendas.xlsx
graficos/grafico_vendas.png
graficos/grafico_categoria.png
graficos/grafico_canais.png
graficos/sql_total_vendas_por_vendedor.png
sales.db
```

Containing:

- Sales analysis reports
- Sales rankings
- Automated visualizations
- SQL analysis outputs
- SQLite database file

---

# 🧠 Skills Demonstrated

* Data Cleaning
* Data Transformation
* Exploratory Data Analysis
* Data Validation
* Report Automation
* Python for Data Analytics
* Data Visualization
* Pipeline Organization
* SQL and SQLite Integration
* Data Pipelines

---

# ▶️ How to Run

## Install dependencies

```bash
pip install pandas matplotlib openpyxl
```

## Run the project

```bash
py sales_analysis.py
```

---

# 📌 Future Improvements

* Advanced visualizations with Matplotlib
* Interactive dashboards
* Advanced SQL queries
* API integration with automated pipelines
* Automated report generation

---

# 👨‍💻 Author

Daniel Nascimento

[LinkedIn](https://www.linkedin.com/in/daniel-nascimento-2729941a8/)

```
```
