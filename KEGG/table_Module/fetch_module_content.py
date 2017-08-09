# -*- coding: utf-8 -*-
import pymysql.cursors, re, sys, string

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
        line = line.replace('+',',')   
        if not line.startswith('///'):
            if not line.startswith(' '):
                if line.startswith('ENTRY') or \
                line.startswith('ORTHOLOGY') or \
                line.startswith('PATHWAY') or \
                line.startswith('REACTION')  or \
                line.startswith('COMPOUND')  or \
                line.startswith('REF_MODULE') or \
                line.startswith('GENE'):
                    
                    All.append(Tags)
                    Tags = []
                    flag = line.split()[0]
                    content = line.strip(str(flag)).strip().split()
                    Tags.append(flag)
                    if ',' in content[0]:
                        for ele in content[0].split(','): Tags.append(ele)
                    #elif '+' in content[0]:
                        #for ele in content[0].split('+'): Tags.append(ele)
                    else:
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
                    content = line.lstrip(str(flag)).strip().rstrip(';')
                    Tags.append(flag)
                    Tags.append(content)
                    split_it = 0
                    
            else:
                if split_it == 0:
                    Tags.append(line.strip().strip(';'))
                elif split_it == 1:
                    tag = line.strip().split()[0]
                    if ',' in tag:
                        for ele in tag.split(','): Tags.append(ele)
                    #elif '+' in tag:
                        #for ele in tag.split('+'): Tags.append(ele)
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
                    elif sublist[0] == 'ORTHOLOGY' or \
                    sublist[0] == 'PATHWAY' or \
                    sublist[0] == 'REACTION' or \
                    sublist[0] == 'COMPOUND' or \
                    sublist[0] == 'BRITE' or \
                    sublist[0] == 'GENE' or \
                    sublist[0] == 'RMODULE' or \
                    sublist[0] == 'REF_MODULE':
                        sublist[1:] = list(set(sublist[1:]))
                        d[sublist[0]] = ';'.join(sublist[1:])
                    else:
                        d[sublist[0]] = ';'.join(sublist[1:])
                except:
                    pass
            All = []
            count += 1
            #if count >  100:break
            
            with connection.cursor() as cursor:
                sql = "SET sql_safe_updates = 0"
                cursor.execute(sql)
                sql = """INSERT INTO KEGG.Module (Entry,Name,Definition,
                        Class,Organism,Gene,Other_DBs,Brite,Rmodule,
                        Comment,Orthology,Pathway,Reaction,Compound,Ref_Module,
                        Reference) 
                        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
                cursor.execute(sql,(d.get('ENTRY'),d.get('NAME'),d.get('DEFINITION'),
                        d.get('CLASS'),d.get('ORGANISM'),d.get('GENE'),d.get('DBLINKS'),
                        d.get('BRITE'),d.get('RMODULE'),d.get('COMMENT'),d.get('ORTHOLOGY'),
                        d.get('PATHWAY'),d.get('REACTION'), d.get('COMPOUND'),d.get('REF_MODULE'),
                        d.get('REFERENCE')))
                connection.commit()
                print 'Loaded', count, 'entries'
            d = {}
connection.close()       