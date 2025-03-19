import numpy as np
import matplotlib.pyplot as plt


p_handle = open('protein_rmsf.xvg')
l_handle = open('ligand_rmsf.xvg')

protein = [line.split() for line in p_handle if line[0] == ' ']
pro_x = np.array([int(x[0])for x in protein])
pro_y = np.array([float(x[1]) for x in protein])


ligand = [line.split() for line in l_handle if line[0] == ' ']
lig_x = np.array([int(x[0]) for x in ligand])
lig_y = np.array([float(x[1]) for x in ligand])


#/////
plt.subplot(311)
plt.title("RMSF Protein")
plt.xlim(pro_x.min(),pro_x.max())
plt.plot(pro_x,pro_y,lw=1.2)
plt.xticks([pro_x[i * 20] for i in range(int(len(pro_x)/20))],rotation="vertical")
plt.ylabel("nm")
plt.xlabel("Backbone Atom Nums")

#/////
plt.subplot(313)
plt.title("RMSF Ligand")
plt.xlim(0,lig_x.max() - lig_x.min())
plt.ylim(0,0.5)
plt.plot(lig_x - lig_x.min(), lig_y,lw=1.2)
plt.xticks(lig_x - lig_x.min())
plt.ylabel("nm")
plt.xlabel("Heavy Atom Nums")



plt.show()
