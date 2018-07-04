import matplotlib.pyplot as plt
import functions as f


# Input
def show(s, a, c, d):
    plt.plot(f.computeGraphs(a, c, d, s))
    plt.grid(True)
    plt.show()
