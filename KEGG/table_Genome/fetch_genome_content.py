import pymysql.cursors, re

connection = pymysql.connect(host='localhost',
                             user='root',
		                     port=3306,
                             cursorclass=pymysql.cursors.DictCursor)


with open('/Users/yingdong/Downloads/genome/genome') as fh:
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
                    content = line.lstrip(str(flag)).split()
                    Tags.append(flag)
                    Tags.append(content[0])
                    split_it = 1
                elif line.startswith('DISEASE'):
                    All.append(Tags)
                    if (Tags[0] != 'DISEASE'):
                        Tags = []
                        flag = line.split()[0]
                        content = ''.join(re.findall('H[0-9]{5,5}', line))
                        Tags.append(flag)
                        Tags.append(content)
                        split_it = 6
                    else:
                        content = ''.join(re.findall('H[0-9]{5,5}', line))
                        Tags.append(content)
                        split_it = 6
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
                elif line.startswith('PLASMID'):
                    All.append(Tags)
                    if Tags[0] != 'PLASMID':
                        Tags = []
                        flag = line.split()[0]
                        content = line.lstrip().strip(str(flag)).lstrip()
                        Tags.append(flag)
                        Tags.append(content)
                        split_it = 5
                    else:
                        content = line.lstrip().strip('PLASMID').lstrip()
                        Tags.append('\n'+content)
                        split_it = 5
                elif line.startswith('CHROMOSOME'):
                    All.append(Tags)
                    if Tags[0] != 'CHROMOSOME':
                        Tags = []
                        flag = line.split()[0]
                        content = line.lstrip().strip(str(flag)).lstrip()
                        Tags.append(flag)
                        Tags.append(content)
                        split_it = 5
                    else:
                        content = line.lstrip().strip('CHROMOSOME').lstrip()
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
            elif 'LINEAGE' in line:
                All.append(Tags)
                Tags = []
                flag = line.strip().split()[0]
                content = line.strip().lstrip(str(flag)).strip().strip(';')
                Tags.append(flag)
                Tags.append(content)
            else:
                if split_it == 0:
                    Tags.append(line.strip())
                elif split_it == 1:
                    Tags.append(line.strip().split()[0])
                elif split_it == 5:
                    Tags.append(line.lstrip())
        else:
            All.append(Tags)
            for sublist in All[1:]:
                if sublist[0] == 'REFERENCE':
                    d[sublist[0]] = ''.join(sublist[1:])
                elif sublist[0] == 'PLASMID':
                    d[sublist[0]] = ''.join(sublist[1:])
                    temp = []
                    plasmid2 = []
                    i = 0
                    for ele in sublist[1:]:
                        if 'SEQUENCE' in ele or 'LENGTH' in ele:
                            ele = ele.strip('SEQUENCE').strip()
                            ele = ele.strip('LENGTH').strip()
                            temp.append(ele)
                        else:
                            temp.append(ele)
                        i += 1
                        if i % 3 == 0:
                            plasmid2.append('|'.join(temp))
                            temp = []
                    d['PLASMID1'] = '||'.join(plasmid2)
                elif sublist[0] == 'CHROMOSOME':
                    d[sublist[0]] = ''.join(sublist[1:])
                    temp = []
                    chromosome2 = []
                    i = 0
                    for ele in sublist[1:]:
                        if 'SEQUENCE' in ele or 'LENGTH' in ele:
                            ele = ele.strip('SEQUENCE').strip()
                            ele = ele.strip('LENGTH').strip()
                            temp.append(ele)
                        else:
                            temp.append(ele)
                        i += 1
                        if i % 3 == 0:
                            chromosome2.append('|'.join(temp))
                            temp = []
                    d['CHROMOSOME1'] = '||'.join(chromosome2)
                elif sublist[0] == 'DISEASE':
                    sublist[1:] = list(set(sublist[1:]))
                    d[sublist[0]] = ';'.join(sublist[1:])
                elif sublist[0] == 'STATISTICS':
                    d[sublist[0]] = '\n'.join(sublist[1:])
                else:
                    d[sublist[0]] = ';'.join(sublist[1:])
            All = []
            count += 1
            with connection.cursor() as cursor:
                sql = "SET sql_safe_updates = 0"
                cursor.execute(sql)
                sql = """INSERT INTO KEGG.Genome (Entry,Name,Definition,Annotation,
                        Taxonomy,Lineage,Data_Source,Original_DB,Keywords,Disease,Comment,Plasmid1,
                        Plasmid2,Chromosome1,Chromosome2,Statistics,Created,Reference,Other_DBs)
                        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
                cursor.execute(sql,(d.get('ENTRY'),d.get('NAME'),d.get('DEFINITION'),
                        d.get('ANNOTATION'),d.get('TAXONOMY'),d.get('LINEAGE'),
                        d.get('DATA_SOURCE'),d.get('ORIGINAL_DB'),d.get('KEYWORDS'),d.get('DISEASE'),
                        d.get('COMMENT'),d.get('PLASMID1'),d.get('PLASMID'),
                        d.get('CHROMOSOME1'),d.get('CHROMOSOME'),d.get('STATISTICS'),d.get('CREATED'),
                        d.get('REFERENCE'),d.get('DBLINKS')))
                connection.commit()
                print 'Loaded', count, 'entries'
            d = {}
connection.close()
