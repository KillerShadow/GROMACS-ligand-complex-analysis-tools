import matplotlib.pyplot as plt
import numpy as np

t,hbond,pairs = np.loadtxt("hbondnum.xvg", comments=["@", "#"], unpack=True)

fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot(111)


ax.plot(t,hbond, color="black", linestyle="-")
ax.set_xlabel("time $t$ (ps)")
ax.set_ylabel("number of H bonds")

plt.show()
