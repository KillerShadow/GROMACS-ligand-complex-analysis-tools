import numpy as np
import matplotlib.pyplot as plt


p_handle = open('protein_rmsd.xvg')
l_handle = open('ligand_rmsd.xvg')

ligand = [line.split() for line in l_handle if line[0] == ' ']
lig_x = np.array([float(x[0]) for x in ligand])
lig_y = np.array([float(x[1]) for x in ligand])

protein = [line.split() for line in p_handle if line[0] == ' ']
protein_x = np.array([float(x[0]) for x in protein])
protein_y = np.array([float(x[1]) for x in protein])

plt.ylim(0,lig_y.max())
plt.xlim(0,lig_x.max())

plt.plot(lig_x,lig_y,lw=1.2,label='LIGAND')
plt.plot(protein_x,protein_y,lw=1.2,label='PROTEIN')

plt.title("RMSD: Ligand, Protein Complex")
plt.xlabel("time (ns)")
plt.ylabel("RMSD (nm)")
plt.legend()
plt.savefig("RMSD.jpg",dpi=400)

plt.show()
