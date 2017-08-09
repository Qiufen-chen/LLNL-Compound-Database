import pymysql.cursors, sys, re

connection = pymysql.connect(host='localhost',
                             user='root',
		             port=3306,
                             cursorclass=pymysql.cursors.DictCursor)
                             
with open(sys.argv[1]) as fh: 
    # split_it = 0, do not split
    # split_it = 1, split the line but only save the first value
    # split_it = 2, split the line and save all the values
    split_it = 0
    Tags = []
    All = []
    d = {}
    count = 0
    for line in fh:   
        if not line.startswith('///'):
            if not line.startswith(' '):
                if line.startswith('NAME') or \
                line.startswith('REMARK') or \
                line.startswith('DBLINKS') or \
                line.startswith('COMMENT')  or \
                line.startswith('FORMULA')  or \
                line.startswith('EXACT_MASS') or \
                line.startswith('MOL_WEIGHT'):
                    All.append(Tags)
                    Tags = []
                    flag = line.split()[0]
                    content = line.lstrip(str(flag)).strip().rstrip(';')
                    Tags.append(flag)
                    Tags.append(content)
                    split_it = 0
                elif line.startswith('ENTRY') or \
                line.startswith('PATHWAY') or \
                line.startswith('MODULE'):
                    All.append(Tags)
                    Tags = []
                    flag = line.split()[0]
                    content = line.strip(str(flag)).strip().split()
                    Tags.append(flag)
                    Tags.append(content[0])
                    split_it = 1
                elif line.startswith('REACTION') or \
                line.startswith('ENZYME'):
                    All.append(Tags)
                    Tags = []
                    flag = line.split()[0]
                    content = line.strip(str(flag)).strip().split()
                    Tags.append(flag)
                    for ele in content: Tags.append(ele)
                    split_it = 2
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
                    content = line.replace(flag, ' '*len(flag))
                    Tags.append(flag)
                    Tags.append(content)
                    split_it = 4
                    
            else:
                if split_it == 0:
                    Tags.append(line.strip().strip(';'))
                elif split_it == 1:
                    Tags.append(line.strip().split()[0])
                elif split_it == 2:
                    content = line.strip().split()
                    for ele in content: Tags.append(ele)
                elif split_it == 4:
                    Tags.append(line)
                elif split_it == 5:
                    Tags.append(line.lstrip()) 
                              
        else:
            All.append(Tags)
            for sublist in All[1:]:
                try:
                    if sublist[0] == 'BRITE' or \
                    sublist[0] == 'ATOM' or \
                    sublist[0] == 'BOND' or \
                    sublist[0] == 'BRACKET' or \
                    sublist[0] == 'REFERENCE' or \
                    sublist[0] == 'SEQUENCE':
                        d[sublist[0]] = ''.join(sublist[1:])
                    elif sublist[0] == 'REACTION' or \
                    sublist[0] == 'MODULE' or \
                    sublist[0] == 'ENZYME' or \
                    sublist[0] == 'PATHWAY':
                        sublist[1:] = list(set(sublist[1:]))
                        d[sublist[0]] = ';'.join(sublist[1:])
                    else:
                        d[sublist[0]] = ';'.join(sublist[1:])
                except:
                    pass

            d['ATOM_BOND'] = 'ATOM' + '\n' + str(d.get('ATOM')) + '\n' + \
                            'BOND' + '\n' + str(d.get('BOND')) + '\n' + \
                            'BRACKET' + '\n' + str(d.get('BRACKET')) + '\n'
            try:
                d.pop('ATOM')
                d.pop('BOND')
                d.pop('BRACKET')
            except: 
                pass
            d['DRUG'] = ';'.join(re.findall('D[0-9]{5,5}',str(d.get('REMARK'))))
            d['DRUG_GROUP'] = ';'.join(re.findall('DG[0-9]{5,5}',str(d.get('REMARK'))))
            d['ATC_CODE'] = ';'.join(re.findall('[A-Z][0-9]{2,2}[A-Z]{2,2}[0-9]{2,2}',str(d.get('REMARK'))))
            d['CHEBI'] = ';'.join(re.findall('ChEBI:\s([0-9]+)',str(d.get('DBLINKS'))))
            d['CHEMBL'] = ';'.join(re.findall('CHEMBL[0-9]+',str(d.get('DBLINKS'))))
            All = []
            count += 1
            
            with connection.cursor() as cursor:
                sql = "SET sql_safe_updates = 0"
                cursor.execute(sql)
                sql = """INSERT INTO KEGG.Compound (Entry, Name, Formula,
                        Exact_mass,Mol_weight,Remark,Drug,Drug_Group,ATC_Code,
                        Reaction,Module,Pathway,Enzyme,Brite,Other_DBs,ChEBI,ChEMBL,
                        Atom_Bond,Sequence,Comment,Reference) 
                        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
                        %s,%s,%s,%s,%s)"""
                cursor.execute(sql,(d.get('ENTRY'),d.get('NAME'),d.get('FORMULA'),
                        d.get('EXACT_MASS'),d.get('MOL_WEIGHT'),d.get('REMARK'), 
                        d.get('DRUG'),d.get('DRUG_GROUP'),d.get('ATC_CODE'),
                        d.get('REACTION'),d.get('MODULE'),d.get('PATHWAY'),d.get('ENZYME'),
                        d.get('BRITE'),d.get('DBLINKS'),d.get('CHEBI'),d.get('CHEMBL'),
                        d.get('ATOM_BOND'),d.get('SEQUENCE'),d.get('COMMENT'),
                        d.get('REFERENCE')))
                connection.commit()
                print 'Loaded', count, 'entries'
            d = {}
connection.close()       