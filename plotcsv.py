import pandas as pd
import matplotlib.pyplot as plt
import sys

for name in sys.argv[1:]:
    df = pd.read_csv(name)

    print(df.head())
    x_column = 'Cache size'  # Replace with the name of the column for x-axis
    y_column = 'Miss Rate'  # Replace with the name of the column for y-axis

    plt.figure(figsize=(10, 6))
    plt.plot(df[x_column], df[y_column], marker='o', label=f'{y_column} vs {x_column}')

    # Add labels, title, and legend
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.title('MRC '+ name)
    plt.grid()
    plt.savefig(name.split(".")[0]+".svg")
