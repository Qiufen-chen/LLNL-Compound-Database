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
        # create a table named KO.
        sql = """create table KEGG.KO (Entry varchar(45) NOT NULL,
                                            Name varchar(1000),
                                            Definition varchar(1000),
                                            Pathway varchar(1000),
                                            Disease varchar(500),
                                            Module varchar(500),
                                            Brite longblob,
                                            Other_DBs varchar(500),
                                            Genes MEDIUMTEXT,
                                            Reference longblob,
                                            PRIMARY KEY (Entry))"""
        cursor.execute(sql)

        # create subtable KO_Pathway.
        sql = """CREATE TABLE `KEGG`.`KO_Pathway` (
                  `KO_ENTRY` VARCHAR(45) NOT NULL,
                  `Pathway` VARCHAR(45) NOT NULL,
                  PRIMARY KEY (`KO_ENTRY`, `Pathway`));
        """
        cursor.execute(sql)
        # create subtable KO_Disease.
        sql = """CREATE TABLE `KEGG`.`KO_Disease` (
                  `KO_ENTRY` VARCHAR(45) NOT NULL,
                  `Disease` VARCHAR(45) NOT NULL,
                  PRIMARY KEY (`KO_ENTRY`, `Disease`));
                """
        cursor.execute(sql)
        # create subtable KO_Module.
        sql = """CREATE TABLE `KEGG`.`KO_Module` (
                  `KO_ENTRY` VARCHAR(45) NOT NULL,
                  `Module` VARCHAR(45) NOT NULL,
                  PRIMARY KEY (`KO_ENTRY`, `Module`));
                """
        cursor.execute(sql)
        # create subtable KO_Enzyme.
        sql = """CREATE TABLE `KEGG`.`KO_Enzyme` (
                  `KO_ENTRY` VARCHAR(45) NOT NULL,
                  `Enzyme` VARCHAR(45) NOT NULL,
                  PRIMARY KEY (`KO_ENTRY`, `Enzyme`));
                """
        cursor.execute(sql)
        # create subtable KO_Drug.
        sql = """CREATE TABLE `KEGG`.`KO_Drug` (
                  `KO_ENTRY` VARCHAR(45) NOT NULL,
                  `Drug` VARCHAR(45) NOT NULL,
                  PRIMARY KEY (`KO_ENTRY`, `Drug`));
                """
        cursor.execute(sql)
        # create subtable KO_Dgroup.
        sql = """CREATE TABLE `KEGG`.`KO_Dgroup` (
                  `KO_ENTRY` VARCHAR(45) NOT NULL,
                  `Dgroup` VARCHAR(45) NOT NULL,
                  PRIMARY KEY (`KO_ENTRY`, `Dgroup`));
                """
        cursor.execute(sql)
        # create subtable KO_Cog.
        sql = """CREATE TABLE `KEGG`.`KO_Cog` (
                  `KO_ENTRY` VARCHAR(45) NOT NULL,
                  `Cog` VARCHAR(45) NOT NULL,
                  PRIMARY KEY (`KO_ENTRY`, `Cog`));
                """
        cursor.execute(sql)
        # create subtable KO_Cazy.
        sql = """CREATE TABLE `KEGG`.`KO_Cazy` (
                  `KO_ENTRY` VARCHAR(45) NOT NULL,
                  `Cazy` VARCHAR(45) NOT NULL,
                  PRIMARY KEY (`KO_ENTRY`, `Cazy`));
                """
        cursor.execute(sql)
        # create subtable KO_Brite.
        sql = """CREATE TABLE `KEGG`.`KO_Brite` (
                  `KO_ENTRY` VARCHAR(45) NOT NULL,
                  `Brite` VARCHAR(45) NOT NULL,
                  PRIMARY KEY (`KO_ENTRY`, `Brite`));
                """
        cursor.execute(sql)
        # create subtable KO_GO.
        sql = """CREATE TABLE `KEGG`.`KO_GO` (
                  `KO_ENTRY` VARCHAR(45) NOT NULL,
                  `GO` VARCHAR(45) NOT NULL,
                  PRIMARY KEY (`KO_ENTRY`, `GO`));
                """
        cursor.execute(sql)
        # create subtable KO_Gene.
        sql = """CREATE TABLE `KEGG`.`KO_Gene` (
                  `KO_ENTRY` VARCHAR(45) NOT NULL,
                  `Gene` VARCHAR(45) NOT NULL,
                  PRIMARY KEY (`KO_ENTRY`, `Gene`));
                """
        cursor.execute(sql)
        # create subtable KO_TC.
        sql = """CREATE TABLE `KEGG`.`KO_TC` (
                  `KO_ENTRY` VARCHAR(45) NOT NULL,
                  `TC` VARCHAR(45) NOT NULL,
                  PRIMARY KEY (`KO_ENTRY`, `TC`));
                """
        cursor.execute(sql)
        # create subtable KO_Reaction.
        sql = """CREATE TABLE `KEGG`.`KO_Reaction` (
                  `KO_ENTRY` VARCHAR(45) NOT NULL,
                  `Reaction` VARCHAR(45) NOT NULL,
                  PRIMARY KEY (`KO_ENTRY`, `Reaction`));
                """
        cursor.execute(sql)
        # create subtable KO_Rclass.
        sql = """CREATE TABLE `KEGG`.`KO_Rclass` (
                  `KO_ENTRY` VARCHAR(45) NOT NULL,
                  `Rclass` VARCHAR(45) NOT NULL,
                  PRIMARY KEY (`KO_ENTRY`, `Rclass`));
                """
        cursor.execute(sql)
        # create subtable KO_Pubmed.
        sql = """CREATE TABLE `KEGG`.`KO_Pubmed` (
                  `KO_ENTRY` VARCHAR(45) NOT NULL,
                  `Pubmed` VARCHAR(45) NOT NULL,
                  PRIMARY KEY (`KO_ENTRY`, `Pubmed`));
                """
        cursor.execute(sql)
        connection.commit()
finally:
    connection.close()
