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
        sql = """create table KEGG.Disease (Entry varchar(45) NOT NULL,
                                            Name varchar(1000),
                                            Description MEDIUMTEXT,
                                            Drug varchar(1000),
                                            Drug_Group varchar(1000),
                                            Category varchar(500),
                                            Env_Factor MEDIUMTEXT,
                                            Carcinogen MEDIUMTEXT,
                                            Marker MEDIUMTEXT,
                                            Pathway varchar(500),
                                            Gene MEDIUMTEXT,
                                            Pathogen MEDIUMTEXT,
                                            Brite longblob,
                                            Other_DBs varchar(1000),
                                            Comment varchar(500),
                                            Reference longblob,
                                            PRIMARY KEY (Entry))"""
        cursor.execute(sql)
        #create subtable Drug.
        sql =  ''' CREATE TABLE KEGG.Disease_Drug( Entry varchar(45) NOT NULL,
                                                                 Drug varchar(20) NOT NULL,
                                                                 PRIMARY KEY (Entry,Drug),
                                                                 FOREIGN KEY (Entry) REFERENCES KEGG.Disease(Entry)
                                                                ); '''
        cursor.execute(sql)
        #create subtable Drug_Group.
        sql =  ''' CREATE TABLE KEGG.Disease_Drug_Group( Entry varchar(45) NOT NULL,
                                                                 Drug_Group varchar(20) NOT NULL,
                                                                 PRIMARY KEY (Entry,Drug_Group),
                                                                 FOREIGN KEY (Entry) REFERENCES KEGG.Disease(Entry)
                                                                ); '''
        cursor.execute(sql)
        connection.commit()
finally:
    connection.close()
