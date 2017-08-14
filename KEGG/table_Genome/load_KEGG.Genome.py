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
        # choose database
        sql = 'use KEGG'
        cursor.execute(sql)
        # create a table named Genome.
        sql = """create table KEGG.Genome (Entry varchar(45) NOT NULL,
                                            Name varchar(5000),
                                            Definition varchar(1000),
                                            Annotation varchar(5000),
                                            Taxonomy varchar(5000),
                                            Lineage varchar(5000),
                                            Data_Source varchar(5000),
                                            Original_DB varchar(5000),
                                            Keywords varchar(5000),
                                            Disease varchar(5000),
                                            Comment varchar(5000),
                                            Plasmid1 varchar(5000),
                                            Plasmid2 longblob,
                                            Chromosome1 varchar(5000),
                                            Chromosome2 longblob,
                                            Statistics longblob,
                                            Created varchar(1000),
                                            Reference longblob,
                                            Other_DBs varchar(5000),
                                            PRIMARY KEY (Entry))"""
        cursor.execute(sql)
        # create a table called Genome_Tax.
        sql = """ CREATE TABLE `KEGG`.`Genome_Tax` (
                  `Genome` VARCHAR(45) NOT NULL,
                  `Taxonomy` VARCHAR(45) NOT NULL,
                  PRIMARY KEY (`Genome`, `Taxonomy`));
        """
        cursor.execute(sql)
        # create a table called Genome_Refseq.
        sql = """CREATE TABLE `KEGG`.`Genome_Refseq` (
                  `Genome` VARCHAR(45) NOT NULL,
                  `Refseq` VARCHAR(45) NOT NULL,
                  PRIMARY KEY (`Genome`, `Refseq`));
        """
        cursor.execute(sql)
        # create a table called Genome_Pubmed.
        sql = """CREATE TABLE `KEGG`.`Genome_Pubmed` (
                  `Genome` VARCHAR(45) NOT NULL,
                  `Pubmed` VARCHAR(45) NOT NULL,
                  PRIMARY KEY (`Genome`, `Pubmed`));
        """
        cursor.execute(sql)
        # create a table called Genome_Pathway.
        sql = """CREATE TABLE `KEGG`.`Genome_Pathway` (
                          `Genome` VARCHAR(45) NOT NULL,
                          `Pathway` VARCHAR(45) NOT NULL,
                          PRIMARY KEY (`Genome`, `Pathway`));
                """
        cursor.execute(sql)
        # create a table called Genome_Module.
        sql = """CREATE TABLE `KEGG`.`Genome_Module` (
                                  `Genome` VARCHAR(45) NOT NULL,
                                  `Module` VARCHAR(45) NOT NULL,
                                  PRIMARY KEY (`Genome`, `Module`));
                        """
        cursor.execute(sql)
        # create a table called Genome_Genbank.
        sql = """CREATE TABLE `KEGG`.`Genome_Genbank` (
                                          `Genome` VARCHAR(45) NOT NULL,
                                          `Genbank` VARCHAR(45) NOT NULL,
                                          PRIMARY KEY (`Genome`, `Genbank`));
                                """
        cursor.execute(sql)
        # create a table called Genome_Disease.
        sql = """CREATE TABLE `KEGG`.`Genome_Disease` (
                                                 `Genome` VARCHAR(45) NOT NULL,
                                                 `Disease` VARCHAR(45) NOT NULL,
                                                 PRIMARY KEY (`Genome`, `Disease`));
                                       """
        cursor.execute(sql)
        # create a table called Genome_Compound.
        sql = """CREATE TABLE `KEGG`.`Genome_Compound` (
                                                     `Genome` VARCHAR(45) NOT NULL,
                                                     `Compound` VARCHAR(45) NOT NULL,
                                                     PRIMARY KEY (`Genome`, `Compound`));
                                           """
        cursor.execute(sql)
        # create a table called Genome_Brite.
        sql = """CREATE TABLE `KEGG`.`Genome_Brite` (
                                                     `Genome` VARCHAR(45) NOT NULL,
                                                     `Brite` VARCHAR(45) NOT NULL,
                                                     PRIMARY KEY (`Genome`, `Brite`));
                                                   """
        cursor.execute(sql)
        # create a table called Genome_Assembly.
        sql = """CREATE TABLE `KEGG`.`Genome_Assembly` (
                                                     `Genome` VARCHAR(45) NOT NULL,
                                                     `Assembly` VARCHAR(45) NOT NULL,
                                                     PRIMARY KEY (`Genome`, `Assembly`));
                                                   """
        cursor.execute(sql)


        connection.commit()
finally:
    connection.close()
