from Bio.PDB import *

pdblist = PDBList()

pdblist.download_entire_pdb()

pdblist.update_pdb()
