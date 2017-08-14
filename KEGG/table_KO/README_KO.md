KEGG KO table content extraction and sub-table generation program
Data: 08/14/2017

USAGE NOTE
-----
- All .py files were coded using Python 2.7
- Required module: pymysql, re

File Description
-----
- **ko**: main table, txt file, downloaded from [here](http://www.kegg.jp/kegg/download/)
- **ko_XXX.list**: subtables with id mapping information, txt file, downloaded from [here](http://www.kegg.jp/kegg/download/)
- **fetch_title.py**: search and return all tags in main table txt file.
- **load_KEGG.KO.py**: create KEGG.KO table and generate sub-tables.(connection may need change.)
- **fetch_ko_content.py**: read, extract, and load data from main txt file.(connection may need change.)
- **fetch_ko_lists.py**: read, extract, and load data from id mapping lists txt file.(connection may need change.)
- **split_XXX.sql**: contains SQL code for subtable creation, after execution in MySQL, they were saved as stored procedures. 

Running
-----
To completely and correctly build relational KEGG KO database, following steps are needed:

- Run **fetch_title.py** and get all column names by running following command in terminal:
```
	python fetch_title.py
```
- Create main table and subtables using **load_KEGG.KO.py** by running following command in terminal: 
```
	python load_KEGG.KO.py
```
- Read data and load data into database using **fetch_ko_content.py** and **fetch_ko_lists.py** by running following command in terminal:
```
	python fetch_ko_content.py
	python fetch_ko_lists.py  
```
- Create procedure via **split_XXX.sql** files on MySQL clipboard.
- Split via stored procedures using using following commands on MySQL clipboard:
```
	call split_KO_pathway();
	call split_KO_module();
	call split_KO_disease();
```	
- Delete the column(Pathway,Module,Disease) which generate subtables in the main table KO(by MYSQL GUI).