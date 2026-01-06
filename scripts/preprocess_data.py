import pandas as pd
import os

def preprocess_data():
    print("Starting data preprocessing...")
    
    # Paths
    raw_path = "data/raw"
    processed_path = "data/processed"
    
    # Load datasets
    train = pd.read_csv(os.path.join(raw_path, "train.csv"))
    stores = pd.read_csv(os.path.join(raw_path, "stores.csv"))
    features = pd.read_csv(os.path.join(raw_path, "features.csv"))
    
    # 1. Relational Join
    # Merge train with stores
    data = pd.merge(train, stores, on="Store", how="left")
    # Merge with features
    data = pd.merge(data, features, on=["Store", "Date", "IsHoliday"], how="left")
    
    initial_row_count = len(data)
    
    # 2. Format Dates
    data['Date'] = pd.to_datetime(data['Date'])
    
    # 3. Handle Markdowns: Fill NaN with 0
    markdown_cols = ['MarkDown1', 'MarkDown2', 'MarkDown3', 'MarkDown4', 'MarkDown5']
    for col in markdown_cols:
        if col in data.columns:
            data[col] = data[col].fillna(0)
            
    # 4. Process Returns
    # Flag negative values as Returns
    data['Is_Return'] = data['Weekly_Sales'] < 0
    data['Gross_Sales'] = data['Weekly_Sales'].apply(lambda x: x if x > 0 else 0)
    data['Returns'] = data['Weekly_Sales'].apply(lambda x: abs(x) if x < 0 else 0)
    data['Net_Sales'] = data['Gross_Sales'] - data['Returns']
    
    # Save cleaned data
    output_file = os.path.join(processed_path, "cleaned_walmart_data.csv")
    data.to_csv(output_file, index=False)
    
    # Generate Summary Report
    summary = f"""
# Data Cleaning Summary Report

## Project: Retail Inventory Optimizer - Day 1
**Date:** {pd.Timestamp.now().strftime('%Y-%m-%d')}

### Processing Overview
- **Raw Data Files Loaded:** train.csv, stores.csv, features.csv
- **Total Initial Rows (Merged):** {initial_row_count:,}
- **Successfully Cleaned Rows:** {len(data):,}

### Business Rules Applied
1. **Markdowns handled:** All missing values in MarkDown1-5 columns were replaced with 0.0, representing no active promotion.
2. **Returns Flagged:** Identified {data['Is_Return'].sum():,} rows with negative sales values.
3. **Financial Engineering:** Created `Gross_Sales`, `Returns`, and `Net_Sales` columns to accurately track revenue.
4. **Date Formatting:** Converted 'Date' column to standard datetime objects for time-series analysis.
5. **Relational Integration:** Integrated Store and Feature attributes into a single master dataset.

### Output
- Cleaned dataset saved to: `{output_file}`
"""
    
    with open("cleaning_summary.md", "w") as f:
        f.write(summary)
        
    print(f"Preprocessing complete. Summary saved to cleaning_summary.md")
    print(f"Cleaned data saved to {output_file}")

if __name__ == "__main__":
    preprocess_data()
