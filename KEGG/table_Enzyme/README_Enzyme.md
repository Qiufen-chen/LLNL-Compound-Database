KEGG Enzyme table content extraction and sub-table generation program
Data: 07/20/2017

USAGE NOTE
-----
- All .py file was coded using Python 2.7
- Required module: pymysql, sys, re

File Description
-----
enzyme: main table, txt file.
fetch_title.py: Search and return all tags in main table txt file.
load_KEGG.Enzyme: Create KEGG.Enzyme table and generate sub-tables.(‘connection’ may need change.)
fetch_enzyme_content.py: Read, extract, and load data from main txt file.(‘connection’ may need change.)
split_XXX.sql: Contains SQL code for subtable creation. After execution in MySQL, they were saved as stored procedures. 
call_enzyme.sql: For the execution of all stored procedures created by split_XXX.sql 

Running
-----
To completely and correctly build relational KEGG Enzyme database, following steps are needed:
- Run fetch_title.py and get all column names.
	python fetch_title.py
- Create main table and subtables using ‘load_KEGG.Enzyme.py’ by running following command in terminal: 
	python load_KEGG.Enzyme.py
- Read data and load data into database using ‘fetch_enzyme_content.py’ by running following command in terminal:
	python fetch_enzyme_content.py enzyme
- Create procedures via 5 “split_XXX.sql” files in MySQL. 
- Split via stored procedures using “call_enzyme.sql”
- Delete the columns which generate subtables in the main table Enzyme(by GUI).