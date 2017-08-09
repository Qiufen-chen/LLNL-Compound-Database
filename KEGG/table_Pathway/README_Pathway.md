KEGG pathway table content extraction and sub-table generation program
Data: 07/20/2017

USAGE NOTE
-----
- All .py file was coded using Python 2.7
- Required module: pymysql, sys, re

File Description
-----
pathway: main table, txt file.
fetch_title.py: Search and return all tags in main table txt file.
load_KEGG.Pathway: Create KEGG.Pathway table and generate sub-tables.(‘connection’ may need change.)
fetch_pathway_content.py: Read, extract, and load data from main txt file.(‘connection’ may need change.)
split_XXX.sql: Contains SQL code for subtable creation. After execution in MySQL, they were saved as stored procedures. 
call_pathway.sql: For the execution of all stored procedures created by split_XXX.sql 

Running
-----
To completely and correctly build relational KEGG Pathway database, following steps are needed:
- Run fetch_title.py and get all column names of main table.
	python fetch_title.py
- Create main table and subtables using ‘load_KEGG_pathway.py’ by running following command in terminal: 
	python load_KEGG.pathway.py
- Read data and load data into database using ‘fetch_pathway_content.py’ by running following command in terminal:
	python fetch_pathway_content.py pathway
- Create procedures via 8 “split_XXX.sql” files in MySQL. 
- Split via stored procedures using “call_pathway.sql”
- Delete the columns which generate subtables in the main table Pathway(by GUI).