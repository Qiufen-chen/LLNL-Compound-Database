KEGG Enzyme table content extraction and sub-table generation program
Data: 07/20/2017

USAGE NOTE
-----
- All .py files were coded using Python 2.7
- Required module: pymysql, sys, re

File Description
-----
- **enzyme**: main table, txt file, downloaded from [here](http://www.kegg.jp/kegg/download/)
- **fetch_title.py**: search and return all tags in main table txt file.
- **load_KEGG.Enzyme**: create KEGG.Enzyme table and generate sub-tables.(connection may need change.)
- **fetch_enzyme_content.py**: read, extract, and load data from main txt file.(connection may need change.)
- **split_XXX.sql**: contains SQL code for subtable creation, after execution in MySQL, they were saved as stored procedures. 

Running
-----
To completely and correctly build relational KEGG Enzyme database, following steps are needed:

- Run **fetch_title.py** and get all column names by running following command in terminal:
```
	python fetch_title.py
```
- Create main table and subtables using **load_KEGG.Enzyme.py** by running following command in terminal: 
```
	python load_KEGG.Enzyme.py
```
- Read data and load data into database using **fetch_enzyme_content.py** by running following command in terminal:
```
	python fetch_enzyme_content.py enzyme
```
- Create procedures via 5 **split_XXX.sql** files on MySQL clipboard.
- Split via stored procedures using using following commands on MySQL clipboard:
```
	call split_Enzyme_all_reac();
	call split_Enzyme_orthology();
	call split_Enzyme_pathway();
	call split_Enzyme_product();
	call split_Enzyme_substrate();
```	
- Delete the columns which generate subtables in the main table Enzyme(by MYSQL GUI).