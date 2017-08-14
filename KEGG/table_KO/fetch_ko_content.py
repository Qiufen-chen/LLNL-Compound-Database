import pymysql.cursors

connection = pymysql.connect(host='localhost',
                             user='root',
		             port=3306,
                             cursorclass=pymysql.cursors.DictCursor)


with open('/Users/yingdong/Downloads/ko') as fh:
    split_it = 0
    Tags = []
    All = []
    d = {}
    count = 0
    for line in fh:
        if not line.startswith('///'):
            if not line.startswith(' '):
                if (line.startswith('ENTRY') or \
                line.startswith('PATHWAY') or \
                line.startswith('DISEASE') or \
                line.startswith('MODULE')):
                    All.append(Tags)
                    Tags = []
                    flag = line.split()[0]
                    content = line.lstrip(str(flag)).split()
                    Tags.append(flag)
                    Tags.append(content[0])
                    split_it = 1
                elif line.startswith('BRITE'):
                    All.append(Tags)
                    Tags = []
                    flag = line.split()[0]
                    content = line.replace(flag, ' '*len(flag))
                    Tags.append(flag)
                    Tags.append(content)
                    split_it = 4
                elif line.startswith('REFERENCE'):
                    All.append(Tags)
                    if Tags[0] != 'REFERENCE':
                        Tags = []
                        flag = line.split()[0]
                        content = line.lstrip().strip(str(flag)).lstrip()
                        Tags.append(flag)
                        Tags.append(content)
                        split_it = 5
                    else:
                        content = line.lstrip().strip('REFERENCE').lstrip()
                        Tags.append('\n'+content)
                        split_it = 5
                else:
                    All.append(Tags)
                    Tags = []
                    flag = line.split()[0]
                    content = line.lstrip(str(flag)).strip().strip(';')
                    Tags.append(flag)
                    Tags.append(content)
                    split_it = 0
            else:
                if split_it == 0:
                    Tags.append(line.strip())
                elif split_it == 1:
                    Tags.append(line.strip().split()[0])
                elif split_it == 4:
                    Tags.append(line)
                elif split_it == 5:
                    Tags.append(line.lstrip())
        else:
            All.append(Tags)
            for sublist in All[1:]:
                if sublist[0] == 'BRITE' or sublist[0] == 'REFERENCE':
                    d[sublist[0]] = ''.join(sublist[1:])
                elif (sublist[0] == 'PATHWAY' or \
                sublist[0] == 'DISEASE' or \
                sublist[0] == 'MODULE'):
                    sublist[1:] = list(set(sublist[1:]))
                    d[sublist[0]] = ';'.join(sublist[1:])
                elif sublist[0] == 'GENES':
                    d[sublist[0]] = '|'.join(sublist[1:])
                else:
                    d[sublist[0]] = ';'.join(sublist[1:])
            All = []
            count += 1
            with connection.cursor() as cursor:
                sql = "SET sql_safe_updates = 0"
                cursor.execute(sql)
                sql = """INSERT INTO KEGG.Ko (Entry,Name,Definition,Pathway,
                        Disease,Module,Brite,Other_DBs,Genes,Reference)
                        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
                cursor.execute(sql,(d.get('ENTRY'),d.get('NAME'),d.get('DEFINITION'),
                        d.get('PATHWAY'),d.get('DISEASE'),d.get('MODULE'),
                        d.get('BRITE'),d.get('DBLINKS'),d.get('GENES'),d.get('REFERENCE')))
                connection.commit()
                print 'Loaded', count, 'entries'
            d = {}
connection.close()
