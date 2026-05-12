````md
# 📊 Sales Data Analysis with Python & Pandas

Automated sales analysis project developed using Python and Pandas.

This project simulates a real-world data analysis workflow, including:

- Data extraction from Excel
- Data cleaning and preprocessing
- Handling invalid and missing values
- Exploratory Data Analysis (EDA)
- Sales ranking generation
- Automated Excel report export

---

# 🚀 Technologies Used

- Python
- Pandas
- Matplotlib
- OpenPyXL
- Excel

---

# 📂 Project Structure

```bash
sales-analysis-python/
│
├── sales_analysis.py
├── sales_data.xlsx
├── relatorio_vendas.xlsx
└── README.md
````

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
grafico_vendas.png
```

Containing:

* Total Sales by Sales Rep
* Average Sales by Category
* Sales Ranking
* Charts containing comparison between sales representatives

---

# 🧠 Skills Demonstrated

* Data Cleaning
* Data Transformation
* Exploratory Data Analysis
* Data Validation
* Report Automation
* Python for Data Analytics

---

# ▶️ How to Run

## Install dependencies

```bash
pip install pandas openpyxl
```

## Run the project

```bash
py sales_analysis.py
```

---

# 📌 Future Improvements

* Data visualization with Matplotlib
* Interactive dashboards
* SQL integration
* API consumption
* Automated insights generation

---

# 👨‍💻 Author

Daniel Nascimento

[LinkedIn](https://www.linkedin.com/in/daniel-nascimento-2729941a8/)

```
```
