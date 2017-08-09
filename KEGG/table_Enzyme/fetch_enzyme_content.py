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
                if line.startswith('ENTRY'):
                    All.append(Tags)
                    Tags = []
                    flag = line.split()[0]
                    content = line.split()[2]
                    Tags.append(flag)
                    Tags.append(content)
                elif line.startswith('ALL_REAC'):
                    All.append(Tags)
                    Tags = []
                    flag = line.split()[0]
                    content = line.lstrip(str(flag))
                    if '>' in content:
                        all_reac = content.split()[:content.split().index('>')]
                    elif '(other)' in content:
                        all_reac = content.strip().strip('(other) ').split()
                    else:
                        all_reac = content.strip().strip(';').split()
                    Tags.append(flag)
                    for ele in all_reac:
                        Tags.append(ele)
                    split_it = 3  
                elif (line.startswith('ORTHOLOGY') or \
                line.startswith('PATHWAY')):
                    All.append(Tags)
                    Tags = []
                    flag = line.split()[0]
                    content = line.lstrip(str(flag)).split()
                    Tags.append(flag)
                    Tags.append(content[0])
                    split_it = 1
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
                    Tags.append(line.strip().strip(';'))
                elif split_it == 1:
                    Tags.append(line.strip().split()[0])
                elif split_it == 5:
                        Tags.append(line.lstrip())
                elif split_it == 3:
                    content = line.lstrip()
                    if '>' in content:
                        all_reac = content.split()[:content.split().index('>')]
                    elif '(other)' in content:
                        all_reac = content.strip().strip(str('(other) ')).split()
                    else:
                        all_reac = content.strip().strip(';').split()
                        for ele in all_reac:
                            Tags.append(ele)
            
        else:
            All.append(Tags)
            for sublist in All[1:]:
                if sublist[0] == 'PATHWAY' or \
                sublist[0] =='ORTHOLOGY' or \
                sublist[0] =='ALL_REAC':
                    sublist[1:] = list(set(sublist[1:]))
                    d[sublist[0]] = ';'.join(sublist[1:])
                elif sublist[0] == 'REFERENCE' or \
                sublist[0] == 'GENES':
                    d[sublist[0]] = ''.join(sublist[1:])
                else:
                    d[sublist[0]] = ';'.join(sublist[1:])
            substrate = re.findall('CPD:([A-Z]+[0-9]+)',str(d.get('SUBSTRATE')))
            product = re.findall('CPD:([A-Z]+[0-9]+)',str(d.get('PRODUCT')))
            d['SUBSTRATE'] = ';'.join(list(set(substrate)))
            d['PRODUCT'] = ';'.join(list(set(product)))
            All = []
            count += 1
            with connection.cursor() as cursor:
                sql = "SET sql_safe_updates = 0"
                cursor.execute(sql)
                sql = """INSERT INTO KEGG.Enzyme (Entry,Name,Sysname,Class,Reaction,
                        All_Reac,Pathway,Orthology,Substrate,Product,History,
                        Other_DBs,Genes,Comment,Reference) 
                        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
                cursor.execute(sql,(d.get('ENTRY'),d.get('NAME'),d.get('SYSNAME'),
                        d.get('CLASS'),d.get('REACTION'),d.get('ALL_REAC'),
                        d.get('PATHWAY'),d.get('ORTHOLOGY'),d.get('SUBSTRATE'),
                        d.get('PRODUCT'),d.get('HISTORY'),d.get('DBLINKS'),
                        d.get('GENES'),d.get('COMMENT'),d.get('REFERENCE')))
                connection.commit()
                print 'Loaded', count, 'entries'
connection.close()                               