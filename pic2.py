import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load the dataset
df = pd.read_excel(r"C:\Users\y.gu\Desktop\dataset\planespotters_fleet.xlsx")

# Filter for 'Active' and Airline aircraft
active_al_aircraft_df = df[(df['Status'] == 'Active')& (df['Current Operator Category' ] == 'Airline')]

# Identify aircraft where 'Current Operator' and 'First Operator' are the same
dif_operator_df = active_al_aircraft_df[df['Current Operator'] != df['First Operator']]

# Count of such aircraft by region
dif_operator_counts = dif_operator_df.groupby('Current Operator Region').size()
total_counts = active_al_aircraft_df.groupby('Current Operator Region').size()


not_same_operator = (dif_operator_counts / total_counts) * 100
not_same_operator_sorted = not_same_operator.sort_values()
not_same_operator_sorted

# Count the average operation period of 1st customer by region
first_customer_per_df = dif_operator_df.groupby(by='Current Operator Region')['Gap'].mean()
first_customer_per_sorted=first_customer_per_df.sort_values()
first_customer_per_sorted

# Visualization
fig, ax1 = plt.subplots(figsize=(12, 8))

# Bar plot for the share of aircraft with the same current and first operator
color = 'teal'
bar_width = 0.35
index = np.arange(len(not_same_operator_sorted))  # Create an index for the bars
index
bars1 = ax1.bar(index,not_same_operator_sorted.values,width=0.35, color=color)
ax1.set_xlabel('Region')
ax1.set_ylabel('Share (%)', color=color)
#ax1.tick_params(axis='y', labelcolor=color)
ax1.set_xticklabels(index,rotation=45)

# Adding text labels for share percentages on top of the bars
for bar in bars1:
    height = bar.get_height()
    ax1.annotate(f'{height:.2f}%',
                 xy=(bar.get_x() + bar.get_width() / 2, height),
                 xytext=(0, 3),  # 3 points vertical offset
                 textcoords="offset points",
                 ha='center', va='bottom', color='black')

# Setup for the average operation period of the first customer
ax2 = ax1.twinx()

# Bar plot for the average operation period of the first customer
bars2 = ax2.bar(index + bar_width/2, first_customer_per_sorted.values, width=0.35, label='Avg Operation Period (Years)', color='darkorange')

ax2.set_ylabel('Avg Operation Period (Years)', color='darkorange')
ax2.tick_params(axis='y', labelcolor='darkorange')

# Optionally, add labels above bars for clarity
for bars in [bars1, bars2]:
    for bar in bars:
        height = bar.get_height()
        label_x_pos = bar.get_x() + bar.get_width() / 2
        ax1.annotate(f'{height:.2f}',
                     xy=(label_x_pos, height),
                     xytext=(0, 3),  # 3 points vertical offset
                     textcoords="offset points",
                     ha='center', va='bottom')

plt.grid(True)
plt.tight_layout()
plt.show()