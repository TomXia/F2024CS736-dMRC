import matplotlib.pyplot as plt
from matplotlib import animation

itern = 0

while True:
    sizes = input()
    if sizes == '':
        break

    cache_sizes = [float(s) for s in sizes[:-1].split(",")]
    hit_rates = [float(s) for s in input()[:-1].split(",")]

    plt.plot(cache_sizes, hit_rates)
    plt.ylim((0.0,1.0))
    plt.title("stat of {} time".format(itern))
    plt.xlabel("cache_sizes/KB")
    plt.ylabel("hit_rates")
    plt.savefig("plot{}".format(itern))

    itern += 1
    plt.figure()