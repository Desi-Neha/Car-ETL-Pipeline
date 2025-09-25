# 🚗 Car Sales ETL Pipeline

An **end-to-end ETL (Extract, Transform, Load) pipeline** project built in Python.  
This pipeline demonstrates real-world data engineering skills by extracting raw car sales data, transforming it with cleaning and enrichment steps, and loading it into both a **SQLite database** and CSV format.  
It also generates **visualizations** to provide insights into car prices, fuel types, and mileage patterns.

---

## ✨ Features
- 🔄 **Extraction**
  - Automatically reads multiple CSV input files from `/data`
  - Fetches live USD → INR exchange rates (with fallback option)

- 🧹 **Transformation**
  - Cleans raw car sales data (handles missing values, duplicates)
  - Standardizes column formats (date, numeric, categorical)
  - Enriches dataset with price conversion to INR

- 💾 **Loading**
  - Loads the cleaned dataset into **SQLite database** (`cars_etl.db`)
  - Exports a transformed CSV (`cars_transformed.csv`)

- 📊 **Visualization**
  - Price distribution plots
  - Fuel type analysis
  - Mileage vs. price scatter plots
  - Stored automatically in `/plots`

- 🛡 **Incremental Processing**
  - Keeps track of already processed files to avoid duplication

---

## 🛠 Tech Stack
- Python 3  
- Pandas – Data manipulation  
- Requests – API calls (exchange rate)  
- SQLite3 – Lightweight database  
- Matplotlib & Seaborn – Data visualization  
- GitHub – Version control & collaboration  

---

## 📂 Repository Structure
