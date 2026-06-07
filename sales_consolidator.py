import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import glob
import os

file_paths = glob.glob("data/*.xlsx")

if not file_paths:
    raise FileNotFoundError("No Excel files found in data folder")

data_frames = []
for file in file_paths:
    try:
        df = pd.read_excel(file)
        df['Branch'] = os.path.basename(file).replace('.xlsx', '')
        data_frames.append(df)
    except Exception as e:
        print(f"Error reading {file}: {e}")

combined_df = pd.concat(data_frames, ignore_index=True)

combined_df.drop_duplicates(inplace=True)

combined_df['Total_Revenue'] = combined_df['Quantity'] * combined_df['Price_Per_Item']

plt.figure(figsize=(8, 5))
sns.set_theme(style="whitegrid")
sns.barplot(data=combined_df, x='Product_Name', y='Total_Revenue', hue='Branch', palette='muted')

plt.title('Total Revenue per Product by Branch', fontsize=14, fontweight='bold')
plt.xlabel('Product Name', fontsize=12)
plt.ylabel('Total Revenue ($)', fontsize=12)

plt.savefig('sales_chart.png', dpi=300, bbox_inches='tight')
plt.show()

combined_df.to_excel('Final_Combined_Sales_Report.xlsx', index=False)
print("Automation completed successfully. File is ready for download!")
