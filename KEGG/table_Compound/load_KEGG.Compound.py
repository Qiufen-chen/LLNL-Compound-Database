# -*- coding: utf-8 -*-
import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
		             		 port=3306,
                             cursorclass=pymysql.cursors.DictCursor)
try:
    with connection.cursor() as cursor:
       #choose database
        sql = 'use KEGG'
        cursor.execute(sql)
        # create a table named Module.
        sql = """create table KEGG.Compound(Entry varchar(45) NOT NULL,
                                            Name varchar(5000),
                                            Formula varchar(500),
                                            Exact_mass varchar(500),
                                            Mol_weight varchar(500),
                                            Remark MEDIUMTEXT,
                                            Drug MEDIUMTEXT,
                                            Drug_Group MEDIUMTEXT,
                                            ATC_Code MEDIUMTEXT,
                                            Comment varchar(5000),
                                            Reaction MEDIUMTEXT,
                                            Module MEDIUMTEXT,
                                            Enzyme MEDIUMTEXT,
                                            Sequence LONGBLOB,
                                            Pathway MEDIUMTEXT,
                                            Brite LONGBLOB,
                                            Other_DBs MEDIUMTEXT,
                                            ChEBI MEDIUMTEXT,
                                            ChEMBL MEDIUMTEXT,
                                            Atom_Bond LONGBLOB,
                                            Reference LONGBLOB,
                                            PRIMARY KEY (Entry))"""
        cursor.execute(sql)
        #create subtable Reaction.
        sql =  ''' CREATE TABLE KEGG.Compound_Reaction ( Entry varchar(45) NOT NULL,
                                                                 Reaction varchar(20) NOT NULL,
                                                                 PRIMARY KEY (Entry,Reaction),
                                                                 FOREIGN KEY (Entry) REFERENCES KEGG.Compound(Entry)
                                                                ); '''
        cursor.execute(sql)
        
        #create subtable Module.
        sql =  ''' CREATE TABLE KEGG.Compound_Module ( Entry varchar(45) NOT NULL,
                                                                 Module varchar(20) NOT NULL,
                                                                 PRIMARY KEY (Entry,Module),
                                                                 FOREIGN KEY (Entry) REFERENCES KEGG.Compound(Entry)
                                                                ); '''
        cursor.execute(sql)
        
        #create subtable Pathway.
        sql =  ''' CREATE TABLE KEGG.Compound_Pathway ( Entry varchar(45) NOT NULL,
                                                                 Pathway varchar(20) NOT NULL,
                                                                 PRIMARY KEY (Entry,Pathway),
                                                                 FOREIGN KEY (Entry) REFERENCES KEGG.Compound(Entry)
                                                                ); '''
        cursor.execute(sql)
        
        #create subtable Enzyme.
        sql =  ''' CREATE TABLE KEGG.Compound_Enzyme ( Entry varchar(45) NOT NULL,
                                                                 Enzyme varchar(20) NOT NULL,
                                                                 PRIMARY KEY (Entry,Enzyme),
                                                                 FOREIGN KEY (Entry) REFERENCES KEGG.Compound(Entry)
                                                                ); '''
        cursor.execute(sql)
        #create subtable Drug.
        sql =  ''' CREATE TABLE KEGG.Compound_Drug ( Entry varchar(45) NOT NULL,
                                                                 Drug varchar(20) NOT NULL,
                                                                 PRIMARY KEY (Entry,Drug),
                                                                 FOREIGN KEY (Entry) REFERENCES KEGG.Compound(Entry)
                                                                ); '''
        cursor.execute(sql)
        #create subtable Drug_Group.
        sql =  ''' CREATE TABLE KEGG.Compound_Drug_Group ( Entry varchar(45) NOT NULL,
                                                                 Drug_Group varchar(20) NOT NULL,
                                                                 PRIMARY KEY (Entry,Drug_Group),
                                                                 FOREIGN KEY (Entry) REFERENCES KEGG.Compound(Entry)
                                                                ); '''
        cursor.execute(sql)
        #create subtable ATC_Code.
        sql =  ''' CREATE TABLE KEGG.Compound_ATC_Code ( Entry varchar(45) NOT NULL,
                                                                 ATC_Code varchar(20) NOT NULL,
                                                                 PRIMARY KEY (Entry,ATC_Code),
                                                                 FOREIGN KEY (Entry) REFERENCES KEGG.Compound(Entry)
                                                                ); '''
        cursor.execute(sql)
        #create subtable ChEBI.
        sql =  ''' CREATE TABLE KEGG.Compound_ChEBI ( Entry varchar(45) NOT NULL,
                                                                 ChEBI varchar(20) NOT NULL,
                                                                 PRIMARY KEY (Entry,ChEBI),
                                                                 FOREIGN KEY (Entry) REFERENCES KEGG.Compound(Entry)
                                                                ); '''
        cursor.execute(sql)
        #create subtable ChEMBL.
        sql =  ''' CREATE TABLE KEGG.Compound_ChEMBL ( Entry varchar(45) NOT NULL,
                                                                 ChEMBL varchar(20) NOT NULL,
                                                                 PRIMARY KEY (Entry,ChEMBL),
                                                                 FOREIGN KEY (Entry) REFERENCES KEGG.Compound(Entry)
                                                                ); '''
        cursor.execute(sql)
        
finally:
    connection.close()
