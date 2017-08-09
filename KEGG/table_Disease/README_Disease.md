KEGG disease table content extraction and sub-table generation program
Data: 07/20/2017

USAGE NOTE
-----
- All .py files were coded using Python 2.7
- Required module: pymysql, sys, re

File Description
-----
**disease**: main table, txt file, downloaded from [here](http://www.kegg.jp/kegg/download/)
**fetch_title.py**: search and return all tags in main table txt file.
**load_KEGG.Disease**: Create KEGG.Disease table and generate sub-tables.(connection may need change.)
**fetch_disease_content.py**: read, extract, and load data from main txt file.(‘connection’ may need change.)
**split_XXX.sql**: contains SQL code for subtable creation, after execution in MySQL, they were saved as stored procedures. 

Running
-----
To completely and correctly build relational KEGG Disease database, following steps are needed:

- Run **fetch_title.py** and get all column names by running following command in terminal:
```
	python fetch_title.py
```
- Create main table and subtables using **load_KEGG.Disease.py** by running following command in terminal: 
```
	python load_KEGG.Disease.py
```
- Read data and load data into database using **fetch_disease_content.py** by running following command in terminal:
```
	python fetch_disease_content.py disease
```
- Create procedures via 2 **split_XXX.sql** files on MySQL clipboard. 
- Split via stored procedures using using following commands on MySQL clipboard:
```
	call split_Disease_drug();
	call split_Disease_drug_group;
```
- Delete the columns which generate subtables in the main table Disease(by GUI).