import pandas as pd
import matplotlib.pyplot as plt
import sys

baseline = sys.argv[1]
slope = sys.argv[2]
name = sys.argv[3]
df_baseline = pd.read_csv(baseline, skiprows=1,delimiter=',')
df_slope = pd.read_csv(slope, skiprows=1,delimiter=',')

x_column = 'Cache size'  # Replace with the name of the column for x-axis
y_column = 'Miss Rate'  # Replace with the name of the column for y-axis


plt.figure(figsize=(10, 6))
plt.plot(df_baseline[x_column]/(256), df_baseline[y_column], marker='o', label=f'Baseline MRC')
plt.plot(df_slope[x_column]/(256), df_slope[y_column], marker='x', label=f'Dynamic MRC')
plt.legend()
plt.ylim([0,1])

# Add labels, title, and legend
plt.xlabel('Cache Size (MB)')
plt.ylabel('Miss Rate')
if name in ["spanner", "bigtable"]:
    plt.title('MRC for '+ name + ' with a cache using ARC')
elif name == "app":
    plt.title('MRC for an anonymous app with a cache using ARC')
else:
    plt.title('MRC for a ' + name + ' workload with a cache using ARC')
plt.grid()
plt.tight_layout()
plt.savefig(name.split(".")[0]+".png")

plt.clf()
# Sim Time
df = pd.read_csv('time.csv')

# Step 2: Extract categories and data columns
categories = df['Workload']  # Assuming 'category' is the name of the first column
data1 = df['Baseline MRC']/df['Baseline MRC']  # Replace 'data1' with the name of the second column
data2 = df['Dynamic MRC']/df['Baseline MRC']  # Replace 'data2' with the name of the third column

# Step 3: Set up the x positions for the bars
x = range(len(categories))

# Step 4: Create a bar chart
width = 0.35  # Width of each bar

plt.bar(x, data1, width=width, label='Baseline MRC', align='center')
plt.bar([p + width for p in x], data2, width=width, label='Dynamic MRC', align='center')

# Step 5: Customize the plot
plt.xticks([p + width / 2 for p in x], categories)  # Position categories in the middle of grouped bars
plt.xlabel('Workload')
plt.ylabel('Construction Time')
plt.title('MRC Construction Time')
plt.legend()

# Step 6: Show the plot
plt.tight_layout()
plt.savefig("time.png")
