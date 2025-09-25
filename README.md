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
```text
car-sales-etl/
│
├─ data/                  # Raw CSV input files
│   └─ *.csv
│
├─ plots/                 # Generated visualizations
│   ├─ price_distribution.png
│   ├─ fuel_type_analysis.png
│   ├─ mileage_vs_price.png
│   └─ age_vs_price.png
│
├─ etl_pipeline.py        # Main ETL pipeline code
├─ cars_etl.db            # SQLite database (generated after ETL run)
├─ cars_transformed.csv   # Transformed CSV output
└─ README.md              # Project documentation
```
---

## 🚀 Usage / How to Run

**Clone the repository**
```text
git clone https://github.com/your-username/car-sales-etl.git
cd car-sales-etl
```

**Run the ETL pipeline**
```text
python etl_pipeline.py
```

**This will:**

-Extract all CSVs from the data/ folder

-Transform and clean the data

-Load it into cars_etl.db (SQLite) and cars_transformed.csv

-Generate visualizations in the plots/ folder

**Check outputs**

Transformed CSV: cars_transformed.csv

SQLite database: cars_etl.db

Plots: plots/ folder

## 📊 Visualizations

The pipeline automatically generates the following plots:

 1. Price Distribution – Understand the range of car prices.

 2. Fuel Type Analysis – Count and proportion of cars by fuel type.

 3. Mileage vs. Price – Scatter plot showing the relationship between mileage and price.

 4. Age vs. Price – Scatter plot showing how the car’s age affects its price.

Stored in the plots/ folder.

---

## 📌 Author  
👩‍💻 Created by **Desi Neha P**  
_Data Scientist and Analyst | Passionate about healthcare & business intelligence_  
📍 Bengaluru, Karnataka, India  
🔗 [LinkedIn](https://www.linkedin.com/in/desi-neha-prakash-652605326/) | [GitHub](https://github.com/Desi-Neha/patient-waitlist-dashboard)  
