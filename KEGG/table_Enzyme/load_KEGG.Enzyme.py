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
        sql = """create table KEGG.Enzyme (Entry varchar(100) NOT NULL,
                                            Name varchar(5000),
                                            Class varchar(1000),
                                            Sysname varchar(5000),
                                            Reaction MEDIUMTEXT,
                                            All_Reac varchar(5000),
                                            Substrate MEDIUMTEXT,
                                            Product MEDIUMTEXT,
                                            Comment varchar(5000),
                                            History MEDIUMTEXT,
                                            Pathway MEDIUMTEXT,
                                            Orthology MEDIUMTEXT,
                                            Genes longblob,
                                            Other_DBs varchar(5000),
                                            Reference longblob,
                                            PRIMARY KEY (Entry))"""
        cursor.execute(sql)
        #create subtable All_Reac.
        sql =  ''' CREATE TABLE KEGG.Enzyme_All_Reac ( Entry varchar(45) NOT NULL,
                                                                 All_Reac varchar(20) NOT NULL,
                                                                 PRIMARY KEY (Entry,All_Reac),
                                                                 FOREIGN KEY (Entry) REFERENCES KEGG.Enzyme(Entry)
                                                                ); '''
        cursor.execute(sql)
        #create subtable Orthology.
        sql =  ''' CREATE TABLE KEGG.Enzyme_Orthology ( Entry varchar(45) NOT NULL,
                                                                 Orthology varchar(20) NOT NULL,
                                                                 PRIMARY KEY (Entry,Orthology),
                                                                 FOREIGN KEY (Entry) REFERENCES KEGG.Enzyme(Entry)
                                                                ); '''
        cursor.execute(sql)
        #create subtable Pathway.
        sql =  ''' CREATE TABLE KEGG.Enzyme_Pathway ( Entry varchar(45) NOT NULL,
                                                                 Pathway varchar(20) NOT NULL,
                                                                 PRIMARY KEY (Entry,Pathway),
                                                                 FOREIGN KEY (Entry) REFERENCES KEGG.Enzyme(Entry)
                                                                ); '''
        cursor.execute(sql)
        #create subtable Product.
        sql =  ''' CREATE TABLE KEGG.Enzyme_Product ( Entry varchar(45) NOT NULL,
                                                                 Product varchar(20) NOT NULL,
                                                                 PRIMARY KEY (Entry,Product),
                                                                 FOREIGN KEY (Entry) REFERENCES KEGG.Enzyme(Entry)
                                                                ); '''
        cursor.execute(sql)
        #create subtable Substrate.
        sql =  ''' CREATE TABLE KEGG.Enzyme_Substrate ( Entry varchar(45) NOT NULL,
                                                                 Substrate varchar(20) NOT NULL,
                                                                 PRIMARY KEY (Entry,Substrate),
                                                                 FOREIGN KEY (Entry) REFERENCES KEGG.Enzyme(Entry)
                                                                ); '''
        cursor.execute(sql)
        connection.commit()
finally:
    connection.close()
