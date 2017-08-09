KEGG Reaction table content extraction and sub-table generation programReaction
Data: 07/20/2017

USAGE NOTE
-----
- All .py file was coded using Python 2.7
- Required reaction: pymysql, sys, re

File Description
-----
reaction: main table, txt file.
fetch_title.py: Search and return all tags in main table txt file.
load_KEGG_Reaction: Create KEGG.Reaction table and generate sub-tables.(‘connection’ may need change.)
fetch_reaction_content.py: Read, extract, and load data from main txt file.(‘connection’ may need change.)
split_XXX.sql: Contains SQL code for sutable creation. After execution in MySQL, they were saved as stored procedures. 
call_reaction.sql: For the execution of all stored procedures created by split_XXX.sql 

Running
-----
To completely and correctly build relational KEGG Reaction database, following steps are needed:
- Run fetch_title.py and get all column names.
	python fetch_title.py
- Create main table and subtables using ‘load_KEGG.Reaction.py’ by running following command in terminal: 
	python load_KEGG.Reaction.py
- Read data and load data into database using ‘fetch_reaction_content.py’ by running following command in terminal:
	python fetch_reaction_content.py reaction
- Create procedures via 5 “split_XXX.sql” files in MySQL. 
- Split via stored procedures using “call_reaction.sql”
- Delete the columns which generate subtables in the main table Reaction(by GUI).