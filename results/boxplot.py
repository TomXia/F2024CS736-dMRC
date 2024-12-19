import matplotlib.pyplot as plt
import numpy as np

xticklabels = ["Random", "Sequential", "Bigtable", "Spanner", "App"]
rand_err = [0.0002929999999999877, 0.00034000000000000696, 0.0005319999999999769, 0.00011099999999997223, 0.0008700000000000374, 0.0004769999999999497, 0.0012294999999999945, 0.00040799999999996395, 0.005951999999999957, 0.009583999999999926, 0.012762999999999969, 0.013638000000000039, 0.013008999999999937, 0.011233000000000049, 0.007494999999999918, 0.001591000000000009, 0.0016780000000000683, 0.0016410000000000036, 0.002859500000000015, 0.001407000000000047, 0.0014220000000000343, 0.0014060000000000183, 0.0013900000000000023, 0.0013739999999999863, 0.0013739999999999863, 0.0013739999999999863, 0.0013739999999999863, 0.0013739999999999863, 0.0013739999999999863, 0.0013739999999999863, 0.0013739999999999863, 0.0013739999999999863]
seq_err=[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.1875, 0.375, 0.5625, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
big_err=[0.0, 0.0, 0.0, 0.0, 0.004161250000000005, 0.002287499999999998, 0.011075249999999981, 0.0, 0.0, 0.0, 0.0005215000000000636, 0.0, 0.002738750000000012, 0.0009784999999999933, 0.0017982499999998902, 0.0, 0.0013606250000001152, 0.004793249999999971, 0.008340875000000025, 0.007002500000000023, 0.005875124999999981, 0.011818749999999989, 0.010947375000000092, 0.006834000000000118, 0.008092624999999964, 0.007477249999999991, 0.006789875000000056, 0.006862499999999994, 0.005913125000000075, 0.005673750000000033, 0.0026993749999999483, 0.0]
span_err = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
app_err =[0.0, 0.0, 0.007789999999999964, 0.0, 0.0, 0.0, 0.0006090000000000817, 0.0, 0.004445374999999974, 0.0023017499999999913, 0.00015812500000000895, 0.0019855000000000844, 0.002464874999999922, 0.004287249999999965, 0.0021436249999999824, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
data = [rand_err, seq_err, big_err, span_err, app_err]

fig, ax = plt.subplots()
ax.boxplot(data, showfliers=False, meanline=True, showmeans=True)
ax.set_xticklabels(xticklabels)
ax.set_xlabel("Workloads")
ax.set_ylabel("Absolute Error")
ax.set_title("Dynamic MRC Construction Error")
ax.set_yticks(np.arange(0, 0.05, 0.005))
plt.savefig("error.svg")