import numpy as np
import matplotlib.pyplot as plt


p_handle = open('protein_gyration.xvg')


protein = [line.split() for line in p_handle if line[0] == ' ']
pro_x = np.array([float(x[0])/1000 for x in protein])
pro_y = np.array([float(x[1]) for x in protein])



plt.ylim(2,pro_y.max())
plt.xlim(0,pro_x.max())

plt.plot(pro_x,pro_y,lw=1.2)

plt.title("Radius of Gyration")
plt.xlabel("Time(ns)")
plt.ylabel("nm")#"Å")

plt.show()

