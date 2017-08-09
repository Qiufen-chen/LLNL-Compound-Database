import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='clip.llnl.gov',
                             user='dong8',
		             port=5507,
                             cursorclass=pymysql.cursors.DictCursor)
try:
    with connection.cursor() as cursor:
        # create a database named PDB.
        sql = "create database PDB"
        cursor.execute(sql)
        # create a table named PDB_file.
        sql = "create table PDB.PDB_file( PDB_ID varchar(10), Target_type varchar(50), Method varchar(50), PDB_file longblob ,PRIMARY KEY (PDB_ID));"
        cursor.execute(sql)
        
        connection.commit()
finally:
    connection.close()
        
        


