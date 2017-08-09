import pymysql.cursors, sys, re

connection = pymysql.connect(host='localhost',
                             user='root',
		             port=3306,
                             cursorclass=pymysql.cursors.DictCursor)
    

with open(sys.argv[1]) as fh:
    split_it = 0
    Tags = []
    All = []
    d = {}
    count = 0
    for line in fh:   
        if not line.startswith('///'):
            if not line.startswith(' '):
                if line.startswith('DRUG'):
                    All.append(Tags)
                    Tags = []
                    flag = line.split()[0]
                    content = re.findall('[A-Z]+[0-9]{5,5}', line)
                    Tags.append(flag)
                    for ele in content: Tags.append(ele)
                    split_it = 3
                elif (line.startswith('ENTRY') or \
                line.startswith('PATHWAY')):
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
                elif split_it == 3:
                    for ele in re.findall('[A-Z]+[0-9]{5,5}', line):
                        Tags.append(ele)
                elif split_it == 4:
                    Tags.append(line)
                elif split_it == 5:
                    Tags.append(line.lstrip())
        else:
            All.append(Tags)
            for sublist in All[1:]:
                if sublist[0] == 'BRITE' or sublist[0] == 'REFERENCE':
                    d[sublist[0]] = ''.join(sublist[1:])
                elif sublist[0] == 'DRUG':
                    sublist[1:] = list(set(sublist[1:]))
                    d[sublist[0]] = ';'.join(sublist[1:])
                else:
                    d[sublist[0]] = ';'.join(sublist[1:])
            d['DRUG_GROUP'] = ';'.join(re.findall('DG[0-9]{5,5}',str(d.get('DRUG'))))
            d['DRUG'] = ';'.join(re.findall('D[0-9]{5,5}',str(d.get('DRUG'))))
            All = []
            count += 1
            with connection.cursor() as cursor:
                sql = "SET sql_safe_updates = 0"
                cursor.execute(sql)
                sql = """INSERT INTO KEGG.Disease (Entry,Name,Description,Category,
                        Pathway,Env_Factor,Drug,Drug_Group,Marker,Gene,Pathogen,Carcinogen,
                        Other_DBs,Brite,Comment,Reference) 
                        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
                cursor.execute(sql,(d.get('ENTRY'),d.get('NAME'),d.get('DESCRIPTION'),
                        d.get('CATEGORY'),d.get('PATHWAY'),d.get('ENV_FACTOR'), 
                        d.get('DRUG'),d.get('DRUG_GROUP'),d.get('MARKER'),d.get('GENE'),
                        d.get('PATHOGEN'),d.get('CARCINOGEN'),d.get('DBLINKS'),
                        d.get('BRITE'),d.get('COMMENT'),d.get('REFERENCE')))
                connection.commit()
                print 'Loaded', count, 'entries'
            d = {}
connection.close()                               