import matplotlib.pyplot as plt
import numpy as np

t,hbond = np.loadtxt("sasa.xvg", comments=["@", "#"], unpack=True)

fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot(111)


ax.plot(t,hbond, linestyle="-")
ax.set_xlabel("time $t$ (ns)")
ax.set_ylabel("Area (nm^2)")

plt.show()
