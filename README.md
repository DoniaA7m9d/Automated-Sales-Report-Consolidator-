# Automated Sales Report Consolidator & Data Visualizer

## Project Overview
Retail clients often send weekly sales data from multiple branches in separate Excel files. Manually merging and cleaning these files takes 5+ hours/week and has high error risk.

This Python script automates the entire process: merging, cleaning, calculating revenue, and generating visual reports.

## Key Features
- **Automated Merging**: Combines multiple weekly Excel sheets into one dataset
- **Data Cleaning**: Removes duplicate entries and handles missing data
- **Automated Calculations**: Computes total revenue per transaction
- **Data Visualization**: Generates professional bar charts comparing branch performance using Seaborn & Matplotlib
- **Output**: Saves a clean, executive-ready Excel report and high-resolution charts

## Tech Stack
- Python
- Pandas, NumPy
- Matplotlib, Seaborn

## Results
- 100% automated data consolidation
- Saved ~5 hours of manual work per week
- Eliminated human error in calculations

## How to Run
1. Place all branch Excel files in the `/data` folder
2. Install dependencies: `pip install pandas numpy matplotlib seaborn openpyxl`
3. Run the script: `python sales_consolidator.py`
4. Check `Final_Combined_Sales_Report.xlsx` and `sales_chart.png` in the output

