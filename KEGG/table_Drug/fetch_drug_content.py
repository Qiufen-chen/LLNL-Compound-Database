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
                if (line.startswith('FORMULA') or \
                line.startswith('OTHER_MAP') or \
                line.startswith('MOL_WEIGHT') or \
                line.startswith('EXACT_MASS') or \
                line.startswith('STR_MAP') or \
                line.startswith('ENTRY')):
                    All.append(Tags)
                    Tags = []
                    flag = line.split()[0]
                    content = line.lstrip(str(flag)).split()
                    Tags.append(flag)
                    Tags.append(content[0])
                    split_it = 1
                elif (line.startswith('CLASS') or \
                line.startswith('BRITE') or \
                line.startswith('ATOM') or \
                line.startswith('BOND') or \
                line.startswith('BRACKET') or \
                line.startswith('PRODUCT') or \
                line.startswith('SEQUENCE')):
                    All.append(Tags)
                    Tags = []
                    flag = line.split()[0]
                    content = line.replace(flag, ' '*len(flag))
                    Tags.append(flag)
                    Tags.append(content)
                    split_it = 4
                else:
                    All.append(Tags)
                    Tags = []
                    flag = line.split()[0]
                    content = line.strip().lstrip(str(flag)).strip().strip(';')
                    Tags.append(flag)
                    Tags.append(content)
                    split_it = 0
            else:
                if split_it == 0:
                    Tags.append(line.strip().strip(';'))
                elif split_it == 1:
                    Tags.append(line.strip().split()[0])
                elif split_it == 4:
                    Tags.append(line)
        else:
            All.append(Tags)
            for sublist in All[1:]:
                try:
                    if sublist[0] == 'CLASS' or \
                    sublist[0] == 'BRITE' or \
                    sublist[0] == 'ATOM' or \
                    sublist[0] == 'BOND' or \
                    sublist[0] == 'BRACKET' or \
                    sublist[0] == 'PRODUCT' or \
                    sublist[0] == 'SEQUENCE':
                        d[sublist[0]] = ''.join(sublist[1:])
                    else:
                        d[sublist[0]] = ';'.join(sublist[1:])
                except:
                    pass

            d['ATOM_BOND'] = 'ATOM' + '\n' + str(d.get('ATOM')) + '\n' + \
                            'BOND' + '\n' + str(d.get('BOND')) + '\n' + \
                            'BRACKET' + '\n' + str(d.get('BRACKET')) + '\n'
            all_map = set()
            try:
                for ele in (d.get('STR_MAP')).split(';'):
                    all_map.add(ele)
                for ele in (d.get('OTHER_MAP')).split(';'):
                    all_map.add(ele)
            except:pass
            d['ALL_MAP'] = ';'.join(list(all_map))
            try:
                d.pop('ATOM')
                d.pop('BOND')
                d.pop('BRACKET')
                d.pop('OTHER_MAP')
                d.pop('STR_MAP')
            except: 
                pass
            d['COMPOUND'] = ';'.join(re.findall('C[0-9]{5,5}',str(d.get('REMARK'))))
            d['CHEMICAL'] = ';'.join(re.findall('DG[0-9]{5,5}',str(d.get('REMARK'))))
            d['ATC_CODE'] = ';'.join(re.findall('[A-Z][0-9]{2,2}[A-Z]{2,2}[0-9]{2,2}',str(d.get('REMARK'))))
            d['THERAPRUTIC'] = ';'.join(re.findall('\s[0-9]{4,4}',str(d.get('REMARK')))).replace(' ','')
            All = []
            count += 1
            with connection.cursor() as cursor:
                sql = "SET sql_safe_updates = 0"
                cursor.execute(sql)
                sql = """INSERT INTO KEGG.Drug (Entry,Name,Formula,Exact_mass,
                        Mol_weight,Remark,Target,Metabolism,Activity,Product,
                        Component,All_Map,Interaction,Brite,Other_DBs,Atom_Bond,
                        Class,Sequence,Comment,Source,Compound,Drug_Group,
                        ATC_Code,Therapeutic_Category) 
                        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
                        %s,%s,%s,%s,%s,%s,%s,%s)"""
                cursor.execute(sql,(d.get('ENTRY'),d.get('NAME'),d.get('FORMULA'),
                        d.get('EXACT_MASS'),d.get('MOL_WEIGHT'),d.get('REMARK'), 
                        d.get('TARGET'),d.get('METABOLISM'),d.get('ACTIVITY'),
                        d.get('PRODUCT'),d.get('COMPONENT'),d.get('ALL_MAP'),
                        d.get('INTERACTION'),d.get('BRITE'),d.get('DBLINKS'),
                        d.get('ATOM_BOND'),d.get('CLASS'),d.get('SEQUENCE'),
                        d.get('COMMENT'),d.get('SOURCE'),d.get('COMPOUND'),
                        d.get('CHEMICAL'),d.get('ATC_CODE'),d.get('THERAPRUTIC')))
                connection.commit()
                print 'Loaded', count, 'entries'
                d = {}
connection.close()                               