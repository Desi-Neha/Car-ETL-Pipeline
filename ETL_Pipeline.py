import pandas as pd
import requests
import sqlite3
import glob
import os
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------- CONFIG ----------------
PROCESSED_LOG = "processed_files.log"
PLOTS_DIR = "plots"
os.makedirs(PLOTS_DIR, exist_ok=True)  # make sure plots folder exists

# ---------------- EXTRACT ----------------
def extract(data_path, api_url):
    # Find all CSV files in folder
    all_files = glob.glob(f"{data_path}/*.csv")

    if not all_files:
        print("⚠️ No CSV files found.")
        return None, None, []

    # Load processed files log
    if os.path.exists(PROCESSED_LOG):
        with open(PROCESSED_LOG, "r") as f:
            processed = set(f.read().splitlines())
    else:
        processed = set()

    # Only process new files
    new_files = [f for f in all_files if f not in processed]

    if not new_files:
        print("⚠️ No new CSV files found. Skipping extract.")
        return None, None, []

    # Read all new CSVs
    dfs = [pd.read_csv(f) for f in new_files]
    cars = pd.concat(dfs, ignore_index=True)

    # Fetch exchange rate (with fallback)
    try:
        response = requests.get(api_url).json()
        usd_inr = response["rates"]["INR"]
    except Exception:
        print("⚠️ API failed, using fallback exchange rate = 83")
        usd_inr = 83

    print(f"✅ Extracted {len(cars)} rows from {len(new_files)} new CSV(s)")
    print(f"💱 1 USD = {usd_inr:.2f} INR")
    return cars, usd_inr, new_files

# ---------------- TRANSFORM ----------------
def transform(cars, usd_inr):
    df = cars.copy()
    df.columns = ["Manufacturer","Model","Engine_size","Fuel_type",
                  "Year_of_manufacture","Mileage","Price"]

    # Clean + Feature engineering
    df = df.dropna().drop_duplicates()
    current_year = datetime.now().year
    df["Car_Age"] = current_year - df["Year_of_manufacture"]
    df["Price_INR"] = df["Price"] * usd_inr

    def mileage_flag(x):
        if x < 50000: return "Low"
        elif x < 100000: return "Medium"
        else: return "High"
    df["Mileage_Category"] = df["Mileage"].apply(mileage_flag)
    df["Price_per_km"] = df["Price"] / df["Mileage"]

    print("✅ Transformed dataset")
    return df

# ---------------- LOAD ----------------
def load(df, new_files, db_name="cars_etl.db", table_name="cars_analysis"):
    conn = sqlite3.connect(db_name)
    df.to_sql(table_name, conn, if_exists="append", index=False)  # append new rows
    conn.close()

    # Append to transformed CSV
    df.to_csv("cars_transformed.csv", mode="a", header=not os.path.exists("cars_transformed.csv"), index=False)

    # Update log of processed files
    with open(PROCESSED_LOG, "a") as f:
        for file in new_files:
            f.write(file + "
")

    print(f"✅ Loaded {len(df)} rows into {db_name} and cars_transformed.csv")

# ---------------- VISUALIZE ----------------
def visualize(df):
    # 1. Distribution of Prices (INR)
    plt.figure(figsize=(8,5))
    sns.histplot(df["Price_INR"], bins=30, kde=True, color="skyblue")
    plt.title("Distribution of Car Prices (INR)")
    plt.xlabel("Price (INR)")
    plt.ylabel("Count")
    plt.savefig(os.path.join(PLOTS_DIR, "price_distribution.png"))
    plt.close()

    # 2. Count of Cars by Fuel Type
    plt.figure(figsize=(6,5))
    sns.countplot(x="Fuel_type", data=df, palette="Set2")
    plt.title("Number of Cars by Fuel Type")
    plt.xlabel("Fuel Type")
    plt.ylabel("Count")
    plt.savefig(os.path.join(PLOTS_DIR, "fuel_type_distribution.png"))
    plt.close()

    # 3. Price vs Mileage Category
    plt.figure(figsize=(6,5))
    sns.boxplot(x="Mileage_Category", y="Price_INR", data=df, palette="Set3")
    plt.title("Car Price vs Mileage Category")
    plt.xlabel("Mileage Category")
    plt.ylabel("Price (INR)")
    plt.savefig(os.path.join(PLOTS_DIR, "price_by_mileage.png"))
    plt.close()

    # 4. Car Age vs Price
    plt.figure(figsize=(7,5))
    sns.scatterplot(x="Car_Age", y="Price_INR", hue="Fuel_type", data=df)
    plt.title("Car Age vs Price (INR)")
    plt.xlabel("Car Age (years)")
    plt.ylabel("Price (INR)")
    plt.savefig(os.path.join(PLOTS_DIR, "age_vs_price.png"))
    plt.close()

    print(f"📊 Visualizations saved in '{PLOTS_DIR}/'")

# ---------------- RUN PIPELINE ----------------
def run_pipeline():
    data_path = "./data"   # folder where your CSVs are stored
    api_url = "https://api.frankfurter.app/latest?from=USD&to=INR"

    cars, usd_inr, new_files = extract(data_path, api_url)
    if cars is None:
        return None

    df = transform(cars, usd_inr)
    load(df, new_files)
    visualize(df)
    return df

# ---------------- DEMO ----------------
if __name__ == "__main__":
    final_df = run_pipeline()
    if final_df is not None:
        print(final_df.head())
