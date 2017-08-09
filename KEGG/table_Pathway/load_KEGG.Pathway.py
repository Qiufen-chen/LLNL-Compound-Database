# -*- coding: utf-8 -*-
import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
		             port=3306,
                             cursorclass=pymysql.cursors.DictCursor)
try:
    with connection.cursor() as cursor:
        # create a database named KEGG
        sql = "create database KEGG"
        cursor.execute(sql)
        # create a table named Pathway.
        sql = """create table KEGG.Pathway (Entry varchar(45) NOT NULL,
                                            Name varchar(500),
                                            Description MEDIUMTEXT,
                                            Organism varchar(1000),
                                            Class varchar(500),
                                            Compound MEDIUMTEXT,
                                            Module MEDIUMTEXT,
                                            Enzyme MEDIUMTEXT,
                                            Gene MEDIUMTEXT,
                                            Reaction MEDIUMTEXT,
                                            Drug MEDIUMTEXT,
                                            Orthology MEDIUMTEXT,
                                            Disease MEDIUMTEXT,
                                            Other_DBs varchar(500),
                                            Ko_pathway varchar(100),
                                            Reference longblob,
                                            PRIMARY KEY (Entry))"""
        
        cursor.execute(sql)
        #create subtable Module.
        sql =  ''' CREATE TABLE KEGG.Pathway_Module ( Entry varchar(45) NOT NULL,
                                                                 Module varchar(20) NOT NULL,
                                                                 PRIMARY KEY (Entry,Module),
                                                                 FOREIGN KEY (Entry) REFERENCES KEGG.Pathway(Entry)
                                                                ); '''
        cursor.execute(sql)
        #create subtable Compound.
        sql =  ''' CREATE TABLE KEGG.Pathway_Compound ( Entry varchar(45) NOT NULL,
                                                                 Compound varchar(20) NOT NULL,
                                                                 PRIMARY KEY (Entry,Compound),
                                                                 FOREIGN KEY (Entry) REFERENCES KEGG.Pathway(Entry)
                                                                ); '''
        cursor.execute(sql)
		#create subtable Enzyme.
        sql =  ''' CREATE TABLE KEGG.Pathway_Enzyme ( Entry varchar(45) NOT NULL,
                                                                 Enzyme varchar(20) NOT NULL,
                                                                 PRIMARY KEY (Entry,Enzyme),
                                                                 FOREIGN KEY (Entry) REFERENCES KEGG.Pathway(Entry)
                                                                ); '''
        cursor.execute(sql)
		#create subtable Gene.
        sql =  ''' CREATE TABLE KEGG.Pathway_Gene ( Entry varchar(45) NOT NULL,
                                                                 Gene varchar(20) NOT NULL,
                                                                 PRIMARY KEY (Entry,Gene),
                                                                 FOREIGN KEY (Entry) REFERENCES KEGG.Pathway(Entry)
                                                                ); '''
        cursor.execute(sql)
		#create subtable Reaction.
        sql =  ''' CREATE TABLE KEGG.Pathway_Reaction ( Entry varchar(45) NOT NULL,
                                                                 Reaction varchar(20) NOT NULL,
                                                                 PRIMARY KEY (Entry,Reaction),
                                                                 FOREIGN KEY (Entry) REFERENCES KEGG.Pathway(Entry)
                                                                ); '''
        cursor.execute(sql)
		#create subtable Drug.
        sql =  ''' CREATE TABLE KEGG.Pathway_Drug ( Entry varchar(45) NOT NULL,
                                                                 Drug varchar(20) NOT NULL,
                                                                 PRIMARY KEY (Entry,Drug),
                                                                 FOREIGN KEY (Entry) REFERENCES KEGG.Pathway(Entry)
                                                                ); '''
        cursor.execute(sql)
		#create subtable Orthology.
        sql =  ''' CREATE TABLE KEGG.Pathway_Orthology ( Entry varchar(45) NOT NULL,
                                                                 Orthology varchar(20) NOT NULL,
                                                                 PRIMARY KEY (Entry,Orthology),
                                                                 FOREIGN KEY (Entry) REFERENCES KEGG.Pathway(Entry)
                                                                ); '''
        cursor.execute(sql)
		#create subtable Disease.
        sql =  ''' CREATE TABLE KEGG.Pathway_Disease ( Entry varchar(45) NOT NULL,
                                                                 Disease varchar(20) NOT NULL,
                                                                 PRIMARY KEY (Entry,Disease),
                                                                 FOREIGN KEY (Entry) REFERENCES KEGG.Pathway(Entry)
                                                                ); '''
        cursor.execute(sql)
        connection.commit()
finally:
    connection.close()
