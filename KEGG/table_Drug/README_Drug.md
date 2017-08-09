KEGG Drug table content extraction and sub-table generation program
Data: 07/20/2017

USAGE NOTE
-----
- All .py files were coded using Python 2.7
- Required module: pymysql, sys, re

File Description
-----
- **drug**: main table, txt file, downloaded from [here](http://www.kegg.jp/kegg/download/)
- **fetch_title.py**: search and return all tags in main table txt file.
- **load_KEGG.Drug**: create KEGG.Drug table and generate sub-tables.(connection may need change.)
- **fetch_drug_content.py**: read, extract, and load data from main txt file.(connection may need change.)
- **split_XXX.sql**: contains SQL code for subtable creation, after execution in MySQL, they were saved as stored procedures. 

Running
-----
To completely and correctly build relational KEGG Drug database, following steps are needed:

- Run **fetch_title.py** and get all column names by running following command in terminal:
```
	python fetch_title.py
```
- Create main table and subtables using **load_KEGG.Drug.py** by running following command in terminal: 
```
	python load_KEGG.Drug.py
```
- Read data and load data into database using **fetch_drug_content.py** by running following command in terminal:
```
	python fetch_drug_content.py drug
```
- Create procedures via 5 **split_XXX.sql** files on MySQL clipboard. 
- Split via stored procedures using using following commands on MySQL clipboard:
```
	call split_Drug_drug_group();
	call split_Drug_compound();
	call split_Drug_therapeutic_category();
	call split_Drug_atc_code();
	call split_Drug_all_map();
```
- Delete the columns which generate subtables in the main table Drug(by MYSQL GUI).