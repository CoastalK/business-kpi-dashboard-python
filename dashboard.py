import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

print("Loading data...")
df = pd.read_csv('sample_sales_data.csv')
df['date'] = pd.to_datetime(df['date'])

# Calculate weekly revenue
df['week'] = df['date'].dt.isocalendar().week
weekly_revenue = df.groupby('week')['revenue'].sum()

print(f"Total revenue: ${df['revenue'].sum():,.2f}")
print(f"Average weekly revenue: ${weekly_revenue.mean():,.2f}")

# Create visualization
plt.figure(figsize=(10, 6))
plt.plot(weekly_revenue.index, weekly_revenue.values, marker='o')
plt.title('Weekly Revenue Trend')
plt.xlabel('Week Number')
plt.ylabel('Revenue ($)')
plt.grid(True, alpha=0.3)
plt.savefig('weekly_revenue.png', dpi=300, bbox_inches='tight')
print("Chart saved as weekly_revenue.png")