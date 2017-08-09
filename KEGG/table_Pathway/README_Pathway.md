KEGG pathway table content extraction and sub-table generation program
Data: 07/20/2017

USAGE NOTE
-----
- All .py files were coded using Python 2.7
- Required module: pymysql, sys, re

File Description
-----
- **pathway**: main table, txt file, downloaded from [here](http://www.kegg.jp/kegg/download/)
- **fetch_title.py**: search and return all tags in main table txt file.
- **load_KEGG.Pathway.py**: create KEGG.Pathway table and generate sub-tables.(connection may need change.)
- **fetch_pathway_content.py**: read, extract, and load data from main txt file.(connection may need change.)
- **split_XXX.sql**: Contains SQL code for subtable creation, after execution in MySQL, they were saved as stored procedures. 

Running
-----
To completely and correctly build relational KEGG Pathway database, following steps are needed:

- Run **fetch_title.py** and get all column names of main table by running following command in terminal:
```
	python fetch_title.py
```
- Create main table and subtables using **load_KEGG_pathway.py** by running following command in terminal: 
```
	python load_KEGG.pathway.py
```
- Read data and load data into database using **fetch_pathway_content.py** by running following command in terminal:
```
	python fetch_pathway_content.py pathway
```
- Create procedures via 8 **split_XXX.sql** files on MySQL clipboard. 
- Split via stored procedures using using following commands on MySQL clipboard:
```
	call split_Pathway_compound();
	call split_Pathway_module();
	call split_Pathway_disease();
	call split_Pathway_drug();
	call split_Pathway_enzyme();
	call split_Pathway_gene();
	call split_Pathway_orthology();
	call split_Pathway_reaction();
```
- Delete the columns which generate subtables in the main table Pathway(by MYSQL GUI).