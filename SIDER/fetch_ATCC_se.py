import csv,urllib,re,pymysql.cursors
from bs4 import *
# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
		             		 port=3306,
                             cursorclass=pymysql.cursors.DictCursor)
count = 0
# Grep ATC code from SIDER website.
with open('all_se_CCID.csv','rU') as csvfile:
    atcCode = set()
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        c_id = row[0]
        se_idList = set(row[1].split(';'))
        for se_id in se_idList:
            suffix = ''
            search = se_id[4:]
            for char in search:
                if char != '0':
                    suffix = search[search.index(char):]
                    break
            url = 'http://sideeffects.embl.de/drugs/'+suffix
            html = urllib.urlopen(url).read()
            soup = BeautifulSoup(html)
            tags = soup('a')
            for tag in tags:
                if 'atc' in tag.get('href', ''):
                    if re.search('[A-Z][0-9][0-9][A-Z][A-Z][0-9][0-9]', tag.contents[0]) is not None:
                        atcCode.add(tag.contents[0])
        column1 = c_id
        column2 = ';'.join(list(atcCode))
        count += 1
        atcCode = set()

        # Load data from website to the database.
        with connection.cursor() as cursor:
            sql = "USE SIDER"
            cursor.execute(sql)
            sql = "SET SQL_SAFE_UPDATES = 0"
            cursor.execute(sql)
            sql = """INSERT INTO SIDER.drug_with_side_effect (
                                     UMLS_concept_id_for_label,
                                     ATC_Code)
                                     VALUES (%s,%s)
                            """
            cursor.execute(sql, (column1, column2))
            connection.commit()

        print count, column1, column2
connection.close()