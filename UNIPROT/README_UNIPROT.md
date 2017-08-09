UNIPROT subdatabase content extraction and tables generation program.

Date:08/09/2017

USAGE NOTE
-----
+ All .py file was coded using Python 2.7
+ Required module:pymysql

File Description
-----
+ **create_UNIPROTdatabase.py**: create UNIPROT subdatabase and generate tables.
+ **fetch_UNIPROT_content.py**: read, extract and load data from id mapping file to mysql.

RUNNING
------
To completely and correctly build UNIPROT subdatabase, following steps are needed:

+ Download the current version of ID Mapping data file which are updated in conjunction with the UniProt Knowledgebase(UniProtKB) from [here](ftp://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/idmapping/)
+ Create UNIPROT subdatabase and tables using **create_UNIPROTdatabase.py**.
+ Read data and load data into mysql using **fetch_UNIPROT_content.py**.
+ Run the following commands on MYSQL clipboard:
```
	INSERT INTO UNIPROT.ID_MAPPING
	SELECT A.UNIPROT_ID, A.PDB_ID, B.CHEMBL_ID FROM UNIPROT_TO_PDB A
	LEFT OUTER JOIN
	UNIPROT_TO_CHEMBL B ON A.UNIPROT_ID = B.UNIPROT_ID;
```
+ Delete table **Uniprot_to_Chembl** and **Uniprot_to_PDB** by using commands on MYSQL clipboard:
```
	delete table Uniprot_to_PDB;
	delete table Uniprot_to_Chembl;
``` 
