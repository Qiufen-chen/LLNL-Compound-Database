# -*- coding: utf-8 -*-
import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
		             		 port=3306,
                             cursorclass=pymysql.cursors.DictCursor)
try:
    with connection.cursor() as cursor:
        sql = 'use KEGG'
        cursor.execute(sql)
        # create a table named Module.
        sql = """create table KEGG.Module (Entry varchar(45) NOT NULL,
                                            Name varchar(500),
                                            Definition MEDIUMTEXT,
                                            Organism varchar(1000),
                                            Class varchar(500),
                                            Compound MEDIUMTEXT,
                                            Rmodule MEDIUMTEXT,
                                            Ref_Module MEDIUMTEXT,
                                            Pathway MEDIUMTEXT,
                                            Gene MEDIUMTEXT,
                                            Reaction MEDIUMTEXT,
                                            Orthology MEDIUMTEXT,
                                            Brite MEDIUMTEXT,
                                            Other_DBs varchar(5000),
                                            Comment varchar(5000),
                                            Reference longblob,
                                            PRIMARY KEY (Entry))"""
        cursor.execute(sql)
        #create subtable Compound.
        sql =  ''' CREATE TABLE KEGG.Module_Compound ( Entry varchar(45) NOT NULL,
                                                                 Compound varchar(20) NOT NULL,
                                                                 PRIMARY KEY (Entry,Compound),
                                                                 FOREIGN KEY (Entry) REFERENCES KEGG.Module(Entry)
                                                                ); '''
        cursor.execute(sql)
        #create subtable Rmodule.
        sql =  ''' CREATE TABLE KEGG.Module_Rmodule ( Entry varchar(45) NOT NULL,
                                                                 Rmodule varchar(20) NOT NULL,
                                                                 PRIMARY KEY (Entry,Rmodule),
                                                                 FOREIGN KEY (Entry) REFERENCES KEGG.Module(Entry)
                                                                ); '''
        cursor.execute(sql)
        #create subtable Ref_Module.
        sql =  ''' CREATE TABLE KEGG.Module_Ref_Module ( Entry varchar(45) NOT NULL,
                                                                 Ref_Module varchar(20) NOT NULL,
                                                                 PRIMARY KEY (Entry,Ref_Module),
                                                                 FOREIGN KEY (Entry) REFERENCES KEGG.Module(Entry)
                                                                ); '''
        cursor.execute(sql)
        #create subtable Pathway.
        sql =  ''' CREATE TABLE KEGG.Module_Pathway ( Entry varchar(45) NOT NULL,
                                                                 Pathway varchar(20) NOT NULL,
                                                                 PRIMARY KEY (Entry,Pathway),
                                                                 FOREIGN KEY (Entry) REFERENCES KEGG.Module(Entry)
                                                                ); '''
        cursor.execute(sql)
        #create subtable Gene.
        sql =  ''' CREATE TABLE KEGG.Module_Gene ( Entry varchar(45) NOT NULL,
                                                                 Gene varchar(20) NOT NULL,
                                                                 PRIMARY KEY (Entry,Gene),
                                                                 FOREIGN KEY (Entry) REFERENCES KEGG.Module(Entry)
                                                                ); '''
        cursor.execute(sql)
        #create subtable Orthology.
        sql =  ''' CREATE TABLE KEGG.Module_Orthology ( Entry varchar(45) NOT NULL,
                                                                 Orthology varchar(20) NOT NULL,
                                                                 PRIMARY KEY (Entry,Orthology),
                                                                 FOREIGN KEY (Entry) REFERENCES KEGG.Module(Entry)
                                                                ); '''
        cursor.execute(sql)   
        #create subtable Reaction.
        sql =  ''' CREATE TABLE KEGG.Module_Reaction ( Entry varchar(45) NOT NULL,
                                                                 Reaction varchar(20) NOT NULL,
                                                                 PRIMARY KEY (Entry,Reaction),
                                                                 FOREIGN KEY (Entry) REFERENCES KEGG.Module(Entry)
                                                                ); '''
        cursor.execute(sql)     
        #create subtable Brite.
        sql =  ''' CREATE TABLE KEGG.Module_Brite( Entry varchar(45) NOT NULL,
                                                                 Brite varchar(20) NOT NULL,
                                                                 PRIMARY KEY (Entry,Brite),
                                                                 FOREIGN KEY (Entry) REFERENCES KEGG.Module(Entry)
                                                                ); '''
        cursor.execute(sql)       
        connection.commit()
finally:
    connection.close()
