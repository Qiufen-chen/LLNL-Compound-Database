KEGG Reaction table content extraction and sub-table generation programReaction
Data: 07/20/2017

USAGE NOTE
-----
- All .py files were coded using Python 2.7
- Required reaction: pymysql, sys, re

File Description
-----
- **reaction**: main table, txt file, downloaded from [here](http://www.kegg.jp/kegg/download/)
- **fetch_title.py**: search and return all tags in main table txt file.
- **load_KEGG_Reaction**: create KEGG.Reaction table and generate sub-tables.(connection may need change.)
- **fetch_reaction_content.py**: read, extract, and load data from main txt file.(connection may need change.)
- **split_XXX.sql**: contains SQL code for sutable creation, after execution in MySQL, they were saved as stored procedures. 

Running
-----
To completely and correctly build relational KEGG Reaction database, following steps are needed:

- Run **fetch_title.py** and get all column names by running following command in terminal: 
```
	python fetch_title.py
```
- Create main table and subtables using **load_KEGG.Reaction.py** by running following command in terminal: 
```
	python load_KEGG.Reaction.py
```
- Read data and load data into database using **fetch_reaction_content.py** by running following command in terminal:
```
	python fetch_reaction_content.py reaction
```
- Create procedures via 5 **split_XXX.sql** files in MySQL. 
- Split via stored procedures using using following commands on MySQL clipboard:
```
	call split_Reaction_enzyme();
	call split_Reaction_module();
	call split_Reaction_orthology();
	call split_Reaction_pathway();
	call split_Reaction_rclass();
```
- Delete the columns which generate subtables in the main table Reaction(by MYSQL GUI).