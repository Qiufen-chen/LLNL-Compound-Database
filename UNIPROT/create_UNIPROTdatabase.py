import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='clip.llnl.gov',
                             user='dong8',
                             port=5507,
                             cursorclass=pymysql.cursors.DictCursor)
try:
    with connection.cursor() as cursor:
        sql = "create database UNIPROT"
        cursor.execute(sql)
        sql = "use UNIPROT"
        cursor.execute(sql)
        sql = "create table UNIPROT.Uniprot_to_PDB(Uniprot_ID varchar(25),PDB_ID varchar(10),primary key(Uniprot_ID,PDB_ID));"
        cursor.execute(sql)

        sql = "create table UNIPROT.Uniprot_to_Chembl(Uniprot_ID varchar(25),Chembl_ID varchar(20),primary key(Uniprot_ID,Chembl_ID));"
        cursor.execute(sql)

        sql = """CREATE TABLE `ID_Mapping` (
                 `Uniprot_ID` varchar(25) NOT NULL,
                  `PDB_ID` varchar(10) NOT NULL,
                  `Chembl_ID` varchar(20) NOT NULL,
                  PRIMARY KEY (`Uniprot_ID`,`PDB_ID`,`Chembl_ID`),
                  KEY `fk_ID_Mapping_1_idx` (`PDB_ID`),
                  CONSTRAINT `fk_ID_Mapping_1` FOREIGN KEY (`PDB_ID`) REFERENCES `PDB`.`PDB_file` (`PDB_ID`) ON DELETE NO ACTION ON UPDATE NO ACTION
                ) ENGINE=InnoDB DEFAULT CHARSET=latin1;
        """
        cursor.execute(sql)

        connection.commit()
finally:
    connection.close()




