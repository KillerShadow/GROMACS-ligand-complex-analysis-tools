# GROMACS-ligand-complex-analysis-tools
Some very basic scripts to plot md simulation in gromacs

I was just so lazy to install xmgrace on debian so I wrote those scripts XD,

REMEMBER: check the names required by the script to open the xvg file!!!!

Here you have a couple of files:
  plot.py                -> plots RMSD for both the ligand and the protein
  gyration.py            -> plots radius of gyration for the protein
  hbond_count.py         -> plots the count of hnonds on time scale (make sure you choose the protein and ligand in gmx hbond)
  rmsf_ligand_protein.py -> plots root mean square flactuation for the chosen index and also the ligand
  sasa_calc.py           -> plots sasa for the protein.
