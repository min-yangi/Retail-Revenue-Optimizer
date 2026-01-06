# Retail Inventory Optimizer

## Project Objective
The **Retail Inventory Optimizer** is designed to leverage historical sales data from Walmart to identify patterns, optimize inventory levels, and maximize revenue. As a Senior Business Analyst, the goal of this project is to provide actionable insights into seasonal trends, promotional impacts, and store performance to drive data-driven decision-making.

## Tech Stack
- **Languages:** Python 3.x
- **Libraries:** Pandas (Data Manipulation), NumPy
- **Environment:** Visual Studio Code / Jupyter Notebooks
- **Data Source:** Walmart Sales Dataset (Kaggle)

## Project Roadmap

### Day 1: Data Audit and Professional Structuring
On the first day of the project, the focus was on establishing a professional project architecture and implementing robust data cleaning logic to ensure the integrity of subsequent analyses.

#### 1. Project Architecture
Established a standardized directory structure to maintain a clean workspace:
- `/data/raw`: Immutable raw data files.
- `/data/processed`: Cleaned and transformed datasets ready for modeling.
- `/notebooks`: Exploratory Data Analysis (EDA) and experimental prototyping.
- `/scripts`: Production-ready Python scripts for automation.

#### 2. Business Logic & Cleaning Rules
Applied the following Senior Business Analyst rules to prepare the dataset:
- **Relational Integration:** Merged the primary sales data (`train.csv`) with store metadata (`stores.csv`) and external environmental factors (`features.csv`) to create a comprehensive unified dataset.
- **Promotional Analysis (Markdowns):** Identified that missing values in markdown columns represented days without active promotions. These were filled with `0.0` to prevent analytical bias.
- **Returns Management:** Identified 1,285 transactions with negative `Weekly_Sales`. Instead of deleting this data, it was flagged as `Returns`, and the following metrics were engineered:
  - `Gross_Sales`: Positive transaction values.
  - `Returns`: Absolute value of negative transaction values.
  - `Net_Sales`: `Gross_Sales - Returns` (aligned with standard accounting principles).
- **Temporal Standardization:** Converted all date strings into `datetime` objects to facilitate time-series forecasting.

#### 3. Data Audit Results
- **Total Records Processed:** 421,570
- **Integrity Check:** 100% of rows preserved after the relational join.
- **Cleaned Data Output:** `data/processed/cleaned_walmart_data.csv`

### Day 2: Excel Discovery & Business Insights
The second day focused on extracting high-level business intelligence and exporting actionable data for executive review.

#### 1. Temporal & Holiday Performance
Generated a comparative analysis of revenue performance across holiday vs. regular weeks.
- **Metric:** Total Revenue by Month segmented by Holiday Status.
- **Insight:** Provided a clear view of seasonal peaks and the direct impact of holiday events on gross turnover.

#### 2. Quality Control & Returns Analysis
Conducted a deep dive into department-level returns to identify operational friction.
- **Key Performance Indicator (KPI):** Return Rate (Total Returns / Weekly Sales).
- **Finding:** Identified Department 78 as having the highest return rate at approximately **20.54%**, signaling a need for a quality audit or inventory review for that category.

#### 3. Executive Output
Exported these findings into a professional Excel workbook: `Day2_Business_Insights.xlsx`.
- **Tab 1:** `Monthly_Holiday_Sales` (Timeline optimization).
- **Tab 2:** `Top_10_Dept_Returns` (Risk management & QA).

---
*This project is updated daily to reflect the progress of the analysis.*
