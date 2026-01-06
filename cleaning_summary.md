
# Data Cleaning Summary Report

## Project: Retail Inventory Optimizer - Day 1
**Date:** 2026-01-06

### Processing Overview
- **Raw Data Files Loaded:** train.csv, stores.csv, features.csv
- **Total Initial Rows (Merged):** 421,570
- **Successfully Cleaned Rows:** 421,570

### Business Rules Applied
1. **Markdowns handled:** All missing values in MarkDown1-5 columns were replaced with 0.0, representing no active promotion.
2. **Returns Flagged:** Identified 1,285 rows with negative sales values.
3. **Financial Engineering:** Created `Gross_Sales`, `Returns`, and `Net_Sales` columns to accurately track revenue.
4. **Date Formatting:** Converted 'Date' column to standard datetime objects for time-series analysis.
5. **Relational Integration:** Integrated Store and Feature attributes into a single master dataset.

### Output
- Cleaned dataset saved to: `data/processed\cleaned_walmart_data.csv`
