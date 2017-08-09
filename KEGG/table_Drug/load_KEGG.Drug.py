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
        sql = """create table KEGG.Drug(Entry varchar(45) NOT NULL,
                                            Name varchar(500),
                                            Product LONGBLOB,
                                            Formula varchar(500),
                                            Exact_mass varchar(500),
                                            Mol_weight varchar(500),
                                            Class LONGBLOB,
                                            Component MEDIUMTEXT,
                                            Sequence LONGBLOB,
                                            Source MEDIUMTEXT,
                                            Remark varchar(500),
                                            Compound MEDIUMTEXT,
                                            Drug_Group MEDIUMTEXT,
                                            Therapeutic_Category MEDIUMTEXT,
                                            ATC_Code MEDIUMTEXT,
                                            Activity MEDIUMTEXT,
                                            Comment varchar(1000),
                                            Brite LONGBLOB,
                                            Target MEDIUMTEXT,
                                            Metabolism MEDIUMTEXT,
                                            Interaction varchar(500),
                                            All_Map MEDIUMTEXT, 
                                            Other_DBs MEDIUMTEXT,
                                            Atom_Bond LONGBLOB,
                                            PRIMARY KEY (Entry))"""
        cursor.execute(sql)
        #create subtable Compound.
        sql =  ''' CREATE TABLE KEGG.Drug_Compound( Entry varchar(45) NOT NULL,
                                                                 Compound varchar(20) NOT NULL,
                                                                 PRIMARY KEY (Entry,Compound),
                                                                 FOREIGN KEY (Entry) REFERENCES KEGG.Drug(Entry)
                                                                ); '''
        cursor.execute(sql)
        #create subtable Compound.
        sql =  ''' CREATE TABLE KEGG.Drug_Drug_Group( Entry varchar(45) NOT NULL,
                                                                 Drug_Group varchar(20) NOT NULL,
                                                                 PRIMARY KEY (Entry,Drug_Group),
                                                                 FOREIGN KEY (Entry) REFERENCES KEGG.Drug(Entry)
                                                                ); '''
        cursor.execute(sql)
        #create subtable Therapeutic_Category.
        sql =  ''' CREATE TABLE KEGG.Drug_Therapeutic_Category( Entry varchar(45) NOT NULL,
                                                                 Therapeutic_Category varchar(20) NOT NULL,
                                                                 PRIMARY KEY (Entry,Therapeutic_Category),
                                                                 FOREIGN KEY (Entry) REFERENCES KEGG.Drug(Entry)
                                                                ); '''
        cursor.execute(sql)
        #create subtable ATC_Code.
        sql =  ''' CREATE TABLE KEGG.Drug_ATC_Code( Entry varchar(45) NOT NULL,
                                                                 ATC_Code varchar(20) NOT NULL,
                                                                 PRIMARY KEY (Entry,ATC_Code),
                                                                 FOREIGN KEY (Entry) REFERENCES KEGG.Drug(Entry)
                                                                ); '''
     
        cursor.execute(sql)
        #create subtable All_Map.
        sql =  ''' CREATE TABLE KEGG.Drug_All_Map( Entry varchar(45) NOT NULL,
                                                                 All_Map varchar(20) NOT NULL,
                                                                 PRIMARY KEY (Entry,All_Map),
                                                                 FOREIGN KEY (Entry) REFERENCES KEGG.Drug(Entry)
                                                                ); '''
        cursor.execute(sql)
        connection.commit()
finally:
    connection.close()
