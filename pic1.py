# Importing necessary libraries
import pandas as pd
import matplotlib.pyplot as plt

# Reading the dataset into a pandas DataFrame

df = pd.read_excel(r"C:\Users\y.gu\Desktop\dataset\planespotters_fleet.xlsx")

# Filtering the DataFrame
curr_airline_df = df[(df['Current Operator Category'] == 'Airline') & (df['Status'] == 'Active')]


# group by region,segment
segment_counts= curr_airline_df.groupby(by=['Current Operator Region', 'Aircraft Segment']).size()
segment_counts
average_ages = curr_airline_df.groupby(by='Current Operator Region')['Age'].mean()
unstacked_counts = segment_counts.unstack(fill_value=0)
average_ages


# Plotting the region counts
fig,ax1 = plt.subplots(figsize=(15, 10))
unstacked_counts.plot(kind='bar', stacked=True, ax=ax1, color=['skyblue', 'orange', 'green', 'red', 'purple'])
ax1.set_xlabel('The Continents')
ax1.set_ylabel('Fleet Number', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')
ax1.set_xticklabels(unstacked_counts.index, rotation=45, fontsize=12)
ax1.legend(loc='center right')

# the chart for average age
ax2 = ax1.twinx()
x_ticks = range(len(average_ages.index))

y = average_ages.values

ax2.scatter(x_ticks, y, color='black', marker='o', s=100)  # s=The size of each point

for i, age in zip(x_ticks, y):
    ax2.text(i, age+0.2, f'{age:.2f}', color='black', ha='center', va='bottom')      #set annotation for the age of fleet

ax2.set_ylabel('Average Age', color='black')
ax2.tick_params(axis='y', labelcolor='black')
ax2.set_ylabel('Average Age(Years)', color='black')
ax2.tick_params(axis='y', labelcolor='black')
ax2.set_xticks(x_ticks)


plt.title('The Number and The Average age of Active Airline Fleet')
plt.tight_layout()
# 
totals = unstacked_counts.sum(axis=1)

for i, total in enumerate(totals):
    ax1.text(i, total, str(int(total)), ha='center', va='bottom',fontsize=15) # Set annotaion of the number of total fleeet

plt.show()