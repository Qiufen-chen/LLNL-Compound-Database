import pymysql.cursors

connection = pymysql.connect(host='clip.llnl.gov',
                             user='dong8',
                             port=5507,
                             cursorclass=pymysql.cursors.DictCursor)
cursor = connection.cursor()
sql = "use UNIPROT"
cursor.execute(sql)

with open("/Users/yingdong/Downloads/idmapping.dat") as fh:
    count = 0
    counter_a = 0
    counter_b = 0
    for line in fh:
        count += 1
        if line.split()[1] == "PDB":
            uniprot_id = line.split()[0]
            pdb_id = line.split()[2]
            counter_a += 1
            sql = """ insert into UNIPROT.Uniprot_to_PDB2 (Uniprot_ID,PDB_ID)
                      values (%s,%s)
                  """
            cursor.execute(sql, (uniprot_id, pdb_id))
            print counter_a, 'uniprot id', uniprot_id, 'PDB_id', pdb_id
        elif line.split()[1] == "ChEMBL":
            uniprot_id = line.split()[0]
            chembl_id = line.split()[2]
            counter_b += 1
            sql = """ insert into UNIPROT.Uniprot_to_Chembl2 (Uniprot_ID,Chembl_ID)
                      values (%s,%s)
                  """
            cursor.execute(sql, (uniprot_id, chembl_id))
            print counter_b, 'uniprot id', uniprot_id, 'Chembl_id', chembl_id
            connection.commit()
connection.close()