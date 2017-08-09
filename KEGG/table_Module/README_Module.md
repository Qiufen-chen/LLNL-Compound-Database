KEGG Module table content extraction and sub-table generation program
Data: 07/20/2017

USAGE NOTE
-----
- All .py files were coded using Python 2.7
- Required module: pymysql, sys, re

File Description
-----
- **module**: main table, txt file, downloaded from [here](http://www.kegg.jp/kegg/download/)
- **fetch_title.py**: search and return all tags in main table txt file.
- **load_KEGG_Module.py**: create KEGG.Module table and generate sub-tables.(connection may need change.)
- **fetch_module_content.py**: read, extract, and load data from main txt file.(connection may need change.)
- **split_XXX.sql**: Contains SQL code for subtable creation, after execution in MySQL, they were saved as stored procedures. 

Running
-----
To completely and correctly build relational KEGG Module database, following steps are needed:

- Run **fetch_title.py** and get all column names by running following command in terminal:
```
	python fetch_title.py
```
- Create main table and subtables using **load_KEGG.module.py** by running following command in terminal: 
```
	python load_KEGG.module.py
```
- Read data and load data into database using **fetch_module_content.py** by running following command in terminal:
```
	python fetch_module_content.py module
```
- Create procedures via 8 **split_XXX.sql** files on MySQL clipboard.
- Split via stored procedures using using following commands on MySQL clipboard:
```
	call split_Module_brite();
	call split_Module_compound();
	call split_Module_gene();
	call split_Module_orthology();
	call split_Module_pathway();
	call split_Module_reaction();
	call split_Module_refmodule();
	call split_Module_rmodule();
```
- Delete the columns which generate subtables in the main table Module(by MYSQL GUI).