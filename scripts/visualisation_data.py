import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the data you generated
df = pd.read_csv("transactions_synthetic.csv")

# 2. Hardcore Analysis: Grouping data to find the biggest polluters
category_impact = df.groupby('merchant')['co2e_kg'].sum().sort_values(ascending=False)

# 3. Visualization: Creating the Dashboard
plt.figure(figsize=(10, 6))
sns.barplot(x=category_impact.values, y=category_impact.index, palette="Greens_r")

plt.title('Total Carbon Footprint by Merchant (kg CO2e)', fontsize=15)
plt.xlabel('Total CO2e (kg)', fontsize=12)
plt.ylabel('Merchant', fontsize=12)

# 4. Save the visualization
plt.tight_layout()
plt.savefig("carbon_dashboard.png")
print("Hardcore Visualization Generated: carbon_dashboard.png")
plt.show()
