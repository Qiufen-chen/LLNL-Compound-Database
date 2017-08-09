# -*- coding: utf-8 -*-
import pymysql.cursors, re, sys

connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             port=3306,
                             db='KEGG',
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
                if line.startswith('NAME') or \
                line.startswith('DESCRIPTION') or \
                line.startswith('CLASS') or \
                line.startswith('DBLINKS')  or \
                line.startswith('ORGANISM'):
                #line.startswith('GENE'):
                    All.append(Tags)
                    Tags = []
                    flag = line.split()[0]
                    content = line.lstrip(str(flag)).strip().rstrip(';')
                    Tags.append(flag)
                    Tags.append(content)
                    split_it = 0
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
                    content = line.strip(str(flag)).strip().split()
                    Tags.append(flag)
                    if ',' in content[0]:
                        for ele in content[0].split(','): Tags.append(ele)
                    else:
                        Tags.append(content[0])
                    split_it = 1
                      
            else:
                if split_it == 0:
                    Tags.append(line.strip().strip(';'))
                elif split_it == 1:
                    tag = line.strip().split()[0]
                    if ',' in tag:
                        for ele in tag.split(','): Tags.append(ele)
                    else:    
                        Tags.append(line.strip().split()[0])
                elif split_it == 5:
                    Tags.append(line.lstrip()) 
                              
        else:
            All.append(Tags)
            for sublist in All[1:]:
                try:
                    if sublist[0] == 'REFERENCE':
                        d[sublist[0]] = ''.join(sublist[1:])
                    elif sublist[0] == 'NAME' or \
                    sublist[0] == 'DESCRIPTION' or \
                    sublist[0] == 'CLASS' or \
                    sublist[0] == 'DBLINKS' or \
                    sublist[0] == 'ORGANISM' or \
                    sublist[0] == 'GENE':
                        d[sublist[0]] = ';'.join(sublist[1:])
                    else:
                        sublist[1:] = list(set(sublist[1:]))
                        d[sublist[0]] = ';'.join(sublist[1:])
                except:
                    pass
            All = []
            count += 1
    
            
            with connection.cursor() as cursor:
                sql = "SET sql_safe_updates = 0"
                cursor.execute(sql)
                sql = """INSERT INTO KEGG.Pathway(Entry,Name,Description,
                        Class,Organism,Gene,Other_DBs,Disease,Ko_Pathway,
                        Reaction,Orthology,Module,Drug,Compound,
                        Reference,Enzyme) 
                        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
                cursor.execute(sql,(d.get('ENTRY'),d.get('NAME'),d.get('DESCRIPTION'),
                        d.get('CLASS'),d.get('ORGANISM'),d.get('GENE'),d.get('DBLINKS'),
                        d.get('DISEASE'),d.get('KO_PATHWAY'),d.get('REACTION'),
                        d.get('ORTHOLOGY'),d.get('MODULE'),d.get('DRUG'), d.get('COMPOUND'),
                        d.get('REFERENCE'),d.get('ENZYME')))
                connection.commit()
                print 'Loaded', count, 'entries'
            d = {}
connection.close()       