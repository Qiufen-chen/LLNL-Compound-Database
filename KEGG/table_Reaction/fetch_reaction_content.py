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
                if (line.startswith('ENTRY') or \
                line.startswith('PATHWAY') or \
                line.startswith('ORTHOLOGY') or \
                line.startswith('MODULE') or \
                line.startswith('RCLASS')):
                    All.append(Tags)
                    Tags = []
                    flag = line.split()[0]
                    content = line.lstrip(str(flag)).split()
                    Tags.append(flag)
                    Tags.append(content[0])
                    split_it = 1
                elif line.startswith('ENZYME'):
                    All.append(Tags)
                    Tags = []
                    flag = line.split()[0]
                    content = line.lstrip(str(flag)).split()
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
                elif split_it == 2:
                    for ele in line.strip().split():
                        Tags.append(ele)
                elif split_it == 5:
                    Tags.append(line.lstrip()) 
        else:
            All.append(Tags)
            for sublist in All[1:]:
                if sublist[0] == 'RCLASS' or \
                sublist[0] == 'MODULE' or \
                sublist[0] == 'ORTHOLOGY' or \
                sublist[0] == 'ENZYME' or \
                sublist[0] == 'PATHWAY':
                    sublist[1:] = list(set(sublist[1:]))
                    d[sublist[0]] = ';'.join(sublist[1:])
                elif sublist[0] == 'REFERENCE':
                    d[sublist[0]] = ''.join(sublist[1:])
                else:
                    d[sublist[0]] = ';'.join(sublist[1:])
            reaction = re.findall('R[0-9]+', str(d.get('REMARK')))
            d['REACTION'] = ';'.join(list(set(reaction)))
            All = []
            count += 1
            with connection.cursor() as cursor:
                sql = "SET sql_safe_updates = 0"
                cursor.execute(sql)
                sql = """INSERT INTO KEGG.Reaction (Entry,Name,Rclass,Definition,
                        Equation,Pathway,Enzyme,Orthology,Module,Reaction,Comment,
                        Reference) 
                        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
                cursor.execute(sql,(d.get('ENTRY'),d.get('NAME'),d.get('RCLASS'),
                        d.get('DEFINITION'),d.get('EQUATION'),d.get('PATHWAY'), 
                        d.get('ENZYME'),d.get('ORTHOLOGY'),d.get('MODULE'),d.get('REACTION'),
                        d.get('COMMENT'),d.get('REFERENCE')))
                connection.commit()
                print 'Loaded', count, 'entries'
            d = {}
connection.close()                               