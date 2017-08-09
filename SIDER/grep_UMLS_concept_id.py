import pymysql.cursors
# Connect to the database
connection = pymysql.connect(host='clip.llnl.gov',
                             user='dong8',
		             		 port=5507,
                             cursorclass=pymysql.cursors.DictCursor)

with open("meddra.tsv") as fh:
    count = 0
    unique = set()
    for line in fh:
        idcolumn = line.split()[0]
        unique.add(idcolumn)
        count += 1
        #if count > 20:break
    idlist = (';'.join(unique)).split(";")

    order = 0
    for concept_id in idlist:
        order += 1

        with connection.cursor() as cursor:
            sql = "use SIDER"
            cursor.execute(sql)
            sql = "insert into UMLS_concept_id(UMLS_concept_id) values (%s)"
            cursor.execute(sql,concept_id)
            connection.commit()
            print order,"loaded"
connection.close()






