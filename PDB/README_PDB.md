PDB subdatabase content extraction and tables generation program.

Date:08/09/2017

USAGE NOTE
-----
+ All .py file was coded using Python 2.7
+ Required module:pymysql,biopython

File Description
-----
+ **pdb_entry_type.txt**: txt file, contains information of PDB ID, Target Type and Method.
+ **downloadPDB_biopdb.py**: download the whole PDB bank from the lastest release.
+ **create_PDBdatabase.py**: create PDB subdatabase and generate tables.
+ **load_pdb_content.py**: read, extract adn load data from pdb_entry_type.txt to mysql.

RUNNING
------
To completely and correctly build PDB subdatabase, following steps are needed:

+ Run **downloadPDB_biopdb.py** to download the whole PDB bank on the local repository.
+ Create PDB subdatabase and tables using **create_PDBdatabase.py**.
+ Read data and load data into mysql using **load_pdb_content.py**. 
