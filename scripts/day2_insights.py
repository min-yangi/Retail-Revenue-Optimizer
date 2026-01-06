import pandas as pd
import os

def generate_insights():
    print("Starting Day 2: Excel Discovery...")
    
    # Paths
    processed_path = "data/processed"
    input_file = os.path.join(processed_path, "cleaned_walmart_data.csv")
    output_excel = "Day2_Business_Insights.xlsx"
    
    if not os.path.exists(input_file):
        print(f"Error: {input_file} not found.")
        return

    # Load the cleaned data
    df = pd.read_csv(input_file)
    df['Date'] = pd.to_datetime(df['Date'])
    
    # 1. Summary Table: Total Sales by Month and Holiday status
    # Extract Month and Year for grouping
    df['Year_Month'] = df['Date'].dt.to_period('M')
    
    monthly_holiday_sales = df.groupby(['Year_Month', 'IsHoliday'])['Weekly_Sales'].sum().reset_index()
    # Pivot for a cleaner summary table if desired, or keep as is. 
    # Let's pivot for better Excel readability
    summary_table = monthly_holiday_sales.pivot(index='Year_Month', columns='IsHoliday', values='Weekly_Sales').fillna(0)
    summary_table.columns = ['Regular_Week_Sales', 'Holiday_Week_Sales']
    summary_table['Total_Sales'] = summary_table['Regular_Week_Sales'] + summary_table['Holiday_Week_Sales']
    summary_table = summary_table.reset_index()
    summary_table['Year_Month'] = summary_table['Year_Month'].astype(str)

    # 2. Rank list: Top 10 Departments by 'Return Rate'
    # Return Rate = Returns / Weekly_Sales. 
    # Note: We should aggregate first to avoid division by zero or skewed results from single low-sales weeks.
    dept_stats = df.groupby('Dept').agg({
        'Returns': 'sum',
        'Weekly_Sales': 'sum'
    }).reset_index()
    
    # Avoid division by zero by filtering out depts with 0 or negative total weekly sales
    dept_stats = dept_stats[dept_stats['Weekly_Sales'] > 0]
    dept_stats['Return_Rate'] = dept_stats['Returns'] / dept_stats['Weekly_Sales']
    
    top_10_returns = dept_stats.sort_values(by='Return_Rate', ascending=False).head(10)

    # 3. Export to Excel
    with pd.ExcelWriter(output_excel, engine='openpyxl') as writer:
        summary_table.to_excel(writer, sheet_name='Monthly_Holiday_Sales', index=False)
        top_10_returns.to_excel(writer, sheet_name='Top_10_Dept_Returns', index=False)
    
    print(f"Day 2 Insights exported to {output_excel}")
    
    # Store findings for README update
    return {
        "top_return_dept": top_10_returns.iloc[0]['Dept'],
        "top_return_rate": top_10_returns.iloc[0]['Return_Rate'],
        "total_period_sales": summary_table['Total_Sales'].sum()
    }

if __name__ == "__main__":
    findings = generate_insights()
    print("Findings for documentation:", findings)
