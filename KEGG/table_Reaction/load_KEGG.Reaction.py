# -*- coding: utf-8 -*-
import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
		             port=3306,
                             cursorclass=pymysql.cursors.DictCursor)
try:
    with connection.cursor() as cursor:
        # Drop a existed schema
        # sql = "drop database if exists KEGG"
        # cursor.execute(sql)
        # create a database named KEGG
        # sql = "create database KEGG"
        # cursor.execute(sql)
        #choose database
        sql = 'use KEGG'
        cursor.execute(sql)
        # create a table named Module.
        sql = """create table KEGG.Reaction (Entry varchar(45) NOT NULL,
                                            Name varchar(1000),
                                            Rclass varchar(500),
                                            Definition varchar(1000),
                                            Module MEDIUMTEXT,
                                            Orthology MEDIUMTEXT,
                                            Enzyme MEDIUMTEXT,
                                            Pathway MEDIUMTEXT,
                                            Equation varchar(5000),
                                            Reaction MEDIUMTEXT,
                                            Comment MEDIUMTEXT,
                                            Reference longblob,
                                            PRIMARY KEY (Entry))"""
        cursor.execute(sql)
         #create subtable Rclass.
        sql =  ''' CREATE TABLE KEGG.Reaction_Rclass( Entry varchar(45) NOT NULL,
                                                                Rclass varchar(20) NOT NULL,
                                                                 PRIMARY KEY (Entry,Rclass),
                                                                 FOREIGN KEY (Entry) REFERENCES KEGG.Reaction(Entry)
                                                                ); '''
        cursor.execute(sql)
        #create subtable Orthology.
        sql =  ''' CREATE TABLE KEGG.Reaction_Orthology( Entry varchar(45) NOT NULL,
                                                                Orthology varchar(20) NOT NULL,
                                                                 PRIMARY KEY (Entry,Orthology),
                                                                 FOREIGN KEY (Entry) REFERENCES KEGG.Reaction(Entry)
                                                                ); '''
        cursor.execute(sql)
        #create subtable Module.
        sql =  ''' CREATE TABLE KEGG.Reaction_Module( Entry varchar(45) NOT NULL,
                                                                Module varchar(20) NOT NULL,
                                                                 PRIMARY KEY (Entry,Module),
                                                                 FOREIGN KEY (Entry) REFERENCES KEGG.Reaction(Entry)
                                                                ); '''
        cursor.execute(sql)
        #create subtable Enzyme.
        sql =  ''' CREATE TABLE KEGG.Reaction_Enzyme( Entry varchar(45) NOT NULL,
                                                                Enzyme varchar(20) NOT NULL,
                                                                 PRIMARY KEY (Entry,Enzyme),
                                                                 FOREIGN KEY (Entry) REFERENCES KEGG.Reaction(Entry)
                                                                ); '''
        cursor.execute(sql)
        #create subtable Pathway.
        sql =  ''' CREATE TABLE KEGG.Reaction_Pathway( Entry varchar(45) NOT NULL,
                                                                Pathway varchar(20) NOT NULL,
                                                                 PRIMARY KEY (Entry,Pathway),
                                                                 FOREIGN KEY (Entry) REFERENCES KEGG.Reaction(Entry)
                                                                ); '''
        cursor.execute(sql)
        
        connection.commit()
finally:
    connection.close()
