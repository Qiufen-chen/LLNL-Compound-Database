KEGG Genome table content extraction and sub-table generation program
Data: 08/14/2017

USAGE NOTE
-----
- All .py files were coded using Python 2.7
- Required module: pymysql, re

File Description
-----
- **genome**: main table, txt file, downloaded from [here](http://www.kegg.jp/kegg/download/)
- **genome_XXX.list**: subtables with id mapping information, txt file, downloaded from [here](http://www.kegg.jp/kegg/download/)
- **fetch_title.py**: search and return all tags in main table txt file.
- **load_KEGG.Genome.py**: create KEGG.Genome table and generate sub-tables.(connection may need change.)
- **fetch_genome_content.py**: read, extract, and load data from main txt file.(connection may need change.)
- **fetch_genome_lists.py**: read, extract, and load data from id mapping lists txt file.(connection may need change.)
- **split_XXX.sql**: contains SQL code for subtable creation, after execution in MySQL, they were saved as stored procedures. 

Running
-----
To completely and correctly build relational KEGG Genome database, following steps are needed:

- Run **fetch_title.py** and get all column names by running following command in terminal:
```
	python fetch_title.py
```
- Create main table and subtables using **load_KEGG.Genome.py** by running following command in terminal: 
```
	python load_KEGG.Genome.py
```
- Read data and load data into database using **fetch_genome_content.py** and **fetch_genome_lists.py** by running following command in terminal:
```
	python fetch_genome_content.py
	python fetch_genome_lists.py  
```
- Create procedure via **split_disease.sql** files on MySQL clipboard.
- Split via stored procedures using using following commands on MySQL clipboard:
```
	call split_Genome_disease();
```	
- Delete the column(Disease) which generate subtables in the main table Genome(by MYSQL GUI).