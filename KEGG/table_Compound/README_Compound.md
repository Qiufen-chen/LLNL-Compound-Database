KEGG compound table content extraction and sub-table generation program.
Date: 07/20/2017

USAGE NOTE
-----
- All .py files were coded using Python 2.7
- Required module: pymysql, sys, re

File Description
-----
- **compound**: downloaded from [here](http://www.kegg.jp/kegg/download/)
- **fetch_title.py**: search and return all tags in main table txt file.
- **load_KEGG.Compound.py**: create KEGG.Compound table and generate sub-tables.(connection may need change.)
- **fetch_compound_content.py**: read, extract, and load data from main txt file.(connection may need change.)
- **split_XXX.sql**: contains SQL code for subtable creation, after execution in MySQL, they were saved as stored procedures. 
- call_compound.sql: For the execution of all stored procedures created by split_XXX.sql 

Running
-----
To completely and correctly build relational KEGG Compound database, following steps are needed:

- Run **fetch_title.py** and get all column names of main table.
```python
	python fetch_title.py
```
- Create main table and subtables using **load_KEGG_compound.py** by running following command in terminal: 
```python
	python load_KEGG.compound.py
```
- Read data and load data into database using **fetch_compound_content.py** by running following command in terminal:
```python
	python fetch_compound_content.py compound
```
- Create procedures via 9 **split_XXX.sql** files on MySQL clipboard.
- Split via stored procedures using following commands on MySQL clipboard:
```
	call split_Compound_atc_code();
	call split_Compound_drug_droup();
	call split_Compound_drug();
	call split_Compound_enzyme();
	call split_Compound_module();
	call split_Compound_pathway();
	call split_Compound_reaction();
	call split_Compound_chebi();
	call split_Compound_chembl();
```
- Delete the columns which generate subtables in the main table Compound(by MYSQL GUI).
