#get PDB ID from file.
import pymysql.cursors

with open('pdb_entry_type.txt') as handle:
  count=0
  ids=[]
  for line in handle:
    ids.append(str(line[0:4]))
    columns=line.split()
    
    # Connect to the database
connection = pymysql.connect(host='clip.llnl.gov',
		     port=5507,
                     user='dong8',
                     db='PDB',
                     cursorclass=pymysql.cursors.DictCursor)
                    

with connection.cursor() as cursor:
    # Safety setting
    sql = "SET sql_safe_updates = 0"
    cursor.execute(sql)
    # Set a bigger allowed packet value
    sql = "SET GLOBAL max_allowed_packet= 104857600"
    cursor.execute(sql)
    # Delete the existing data
    sql = "delete from PDB.PDB_file"
    cursor.execute(sql)
    # Create a new record
    
    for record in ids:
        sql = "INSERT ignore INTO PDB.PDB_file (PDB_ID) VALUES (%s)"
        cursor.execute(sql, (record))
	folder = record[1:3]
        #Insert other columns:PDB_file,Target_type,Method
        #sql = "UPDATE PDB.PDB_file SET PDB_file=load_file('/home/dong8/PDBdatabase/pdb_data/"+folder+"/pdb"+record+".ent'),Target_type=%s, Method=%s WHERE PDB_ID=%s"
	sql = "UPDATE PDB.PDB_file SET Target_type=%s, Method=%s, PDB_File_Path ='/home/dong8/PDBdatabase/pdb_data/"+folder+"/pdb"+record+".ent' WHERE PDB_ID=%s "
        cursor.execute(sql, (columns[1],columns[2],record))

        count+=1
	#if count > 99:break
	print count,"loaded"


    connection.commit()

   

connection.close()
        
