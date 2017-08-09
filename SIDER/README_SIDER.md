SIDER subdatabase content extraction and tables generation program.

Date:08/09/2017

USAGE NOTE
-----
+ All .py files were coded using Python 2.7
+ Required module:pymysql,csv,urllib,re,bs4

File Description
-----
+ **create_SIDERdatabase.py**: create SIDER subdatabase and generate tables.
+ **fetch_SIDER_content.py**: read, extract and load data to MYSQL.
+ **grep_UMLS_concept_id.py**: read, extract and load UMLS_concept_id to the table in MYSQL.
+ **all_se_CCID.csv**: it's generated from one of the downloaded files,contains UMLS_concept_id and the corresponding STITCH_compound_ids,used for grepping ATC code for drug side effect.
+ **all_ind_CCID.csv**: the same with **all_se_CCID.csv** and used for grepping ATC code for drug indication.
+ **fetch_ATCC_se.py**: grep ATC code for drug side effect from website pages.
+ **fetch_ATCC_ind.py**: grep ATC code for drug indication from website pages.
+ **split_XXX.sql**: Contains SQL code for subtable creation. After execution in MySQL, they were saved as stored procedures.
 

RUNNING
------
To completely and correctly build SIDER subdatabase, following steps are needed:

+ Download the current version of SIDER data from [here](http://sideeffects.embl.de/download/)
+ Create SIDER subdatabase and tables using **create_SIDERdatabase.py**.
+ Read data and load data into MYSQL using **fetch_SIDER_content.py**. 
+ Read and load UMLS_concept_id into MYSQL using **grep_UMLS_concept_id.py**.
+ Run **fetch_ATCC_se.py** and **fetch_ATCC_ind.py** to grep ATC codes from website pages and load them into tables.
+ Create stored procedures via **split_XXX.sql** files on  MySQL clipboard.
+ Run the following commands on MYSQL clipboard:
```
	CALL split_se;
	CALL split_indications;
```
+ Delete table **drug_with_side_effect** and **drug_with_indications** by using commands on MYSQL clipboard:
```
	DELETE TABLE drug_with_indications;
	DELETE TABLE drug_with_side_effect;
```   
