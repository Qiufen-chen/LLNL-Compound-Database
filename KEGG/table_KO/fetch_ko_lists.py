import pymysql.cursors

connection = pymysql.connect(host='localhost',
                             user='root',
		                     port=3306,
                             cursorclass=pymysql.cursors.DictCursor)
cursor = connection.cursor()

with open('/Users/yingdong/Downloads/ko/ko_enzyme.list') as fh_enzyme:
    a = 0
    for line in fh_enzyme:
        col1 = (line.split()[0]).split(':')[1]
        col2 = (line.split()[1]).split(':')[1]
        a += 1
        sql = """insert into KEGG.KO_Enzyme (KO_ENTRY,Enzyme) 
                 values
                 (%s, %s)
        """
        cursor.execute(sql,(col1,col2))
        print a, col1, col2

with open('/Users/yingdong/Downloads/ko/ko_drug.list') as fh_drug:
    a = 0
    for line in fh_drug:
        col1 = (line.split()[0]).split(':')[1]
        col2 = (line.split()[1]).split(':')[1]
        a += 1
        sql = """insert into KEGG.KO_Drug (KO_ENTRY,Drug)
                 values
                 (%s, %s)
        """
        cursor.execute(sql,(col1,col2))
        print a, col1, col2

with open('/Users/yingdong/Downloads/ko/ko_disease.list') as fh_disease:
    a = 0
    for line in fh_disease:
        col1 = (line.split()[0]).split(':')[1]
        col2 = (line.split()[1]).split(':')[1]
        a += 1
        sql = """insert ignore into KEGG.KO_Disease (KO_ENTRY,Disease)
                 values
                 (%s, %s)
        """
        cursor.execute(sql,(col1,col2))
        print a, col1, col2

with open('/Users/yingdong/Downloads/ko/ko_dgroup.list') as fh_dgroup:
    a = 0
    for line in fh_dgroup:
        col1 = (line.split()[0]).split(':')[1]
        col2 = (line.split()[1]).split(':')[1]
        a += 1
        sql = """insert into KEGG.KO_Dgroup (KO_ENTRY,Dgroup)
                 values
                 (%s, %s)
        """
        cursor.execute(sql,(col1,col2))
        print a, col1, col2

with open('/Users/yingdong/Downloads/ko/ko_cog.list') as fh_cog:
    a = 0
    for line in fh_cog:
        col1 = (line.split()[0]).split(':')[1]
        col2 = (line.split()[1]).split(':')[1]
        a += 1
        sql = """insert into KEGG.KO_Cog (KO_ENTRY,Cog)
                 values
                 (%s, %s)
        """
        cursor.execute(sql,(col1,col2))
        print a, col1, col2

with open('/Users/yingdong/Downloads/ko/ko_cazy.list') as fh_cazy:
    a = 0
    for line in fh_cazy:
        col1 = (line.split()[0]).split(':')[1]
        col2 = (line.split()[1]).split(':')[1]
        a += 1
        sql = """insert into KEGG.KO_Cazy (KO_ENTRY,Cazy)
                 values
                 (%s, %s)
        """
        cursor.execute(sql,(col1,col2))
        print a, col1, col2

with open('/Users/yingdong/Downloads/ko/ko_brite.list') as fh_brite:
    a = 0
    for line in fh_brite:
        col1 = (line.split()[0]).split(':')[1]
        col2 = (line.split()[1]).split(':')[1]
        a += 1
        sql = """insert into KEGG.KO_Brite (KO_ENTRY,Brite)
                 values
                 (%s, %s)
        """
        cursor.execute(sql,(col1,col2))
        print a, col1, col2

with open('/Users/yingdong/Downloads/ko/ko_module.list') as fh_module:
    a = 0
    for line in fh_module:
        col1 = (line.split()[0]).split(':')[1]
        col2 = (line.split()[1]).split(':')[1]
        a += 1
        sql = """insert ignore into KEGG.KO_Module (KO_ENTRY,Module)
                 values
                 (%s, %s)
        """
        cursor.execute(sql,(col1,col2))
        print a, col1, col2

with open('/Users/yingdong/Downloads/ko/ko_go.list') as fh_go:
    a = 0
    for line in fh_go:
        col1 = (line.split()[0]).split(':')[1]
        col2 = (line.split()[1]).split(':')[1]
        a += 1
        sql = """insert into KEGG.KO_GO (KO_ENTRY,GO)
                 values
                 (%s, %s)
        """
        cursor.execute(sql,(col1,col2))
        print a, col1, col2

with open('/Users/yingdong/Downloads/ko/ko_genes.list') as fh_genes:
    a = 0
    for line in fh_genes:
        col1 = (line.split()[0]).split(':')[1]
        col2 = line.split()[1]
        a += 1
        sql = """insert into KEGG.KO_Gene (KO_ENTRY,Gene)
                 values
                 (%s, %s)
        """
        cursor.execute(sql,(col1,col2))
        print a, col1, col2

with open('/Users/yingdong/Downloads/ko/ko_tc.list') as fh_tc:
    a = 0
    for line in fh_tc:
        col1 = (line.split()[0]).split(':')[1]
        col2 = (line.split()[1]).split(':')[1]
        a += 1
        sql = """insert into KEGG.KO_TC (KO_ENTRY,TC)
                 values
                 (%s, %s)
        """
        cursor.execute(sql,(col1,col2))
        print a, col1, col2

with open('/Users/yingdong/Downloads/ko/ko_reaction.list') as fh_reaction:
    a = 0
    for line in fh_reaction:
        col1 = (line.split()[0]).split(':')[1]
        col2 = (line.split()[1]).split(':')[1]
        a += 1
        sql = """insert into KEGG.KO_Reaction (KO_ENTRY,Reaction)
                 values
                 (%s, %s)
        """
        cursor.execute(sql,(col1,col2))
        print a, col1, col2

with open('/Users/yingdong/Downloads/ko/ko_rclass.list') as fh_rclass:
    a = 0
    for line in fh_rclass:
        col1 = (line.split()[0]).split(':')[1]
        col2 = (line.split()[1]).split(':')[1]
        a += 1
        sql = """insert into KEGG.KO_Rclass (KO_ENTRY,Rclass)
                 values
                 (%s, %s)
        """
        cursor.execute(sql,(col1,col2))
        print a, col1, col2

with open('/Users/yingdong/Downloads/ko/ko_pubmed.list') as fh_pubmed:
    a = 0
    for line in fh_pubmed:
        col1 = (line.split()[0]).split(':')[1]
        col2 = (line.split()[1]).split(':')[1]
        a += 1
        sql = """insert into KEGG.KO_Pubmed (KO_ENTRY,Pubmed)
                 values
                 (%s, %s)
        """
        cursor.execute(sql,(col1,col2))
        print a, col1, col2

with open('/Users/yingdong/Downloads/ko/ko_pathway.list') as fh_pathway:
    a = 0
    for line in fh_pathway:
        col1 = (line.split()[0]).split(':')[1]
        col2 = (line.split()[1]).split(':')[1]
        a += 1
        sql = """insert ignore into KEGG.KO_Pathway (KO_ENTRY,Pathway)
                 values
                 (%s, %s)
        """
        cursor.execute(sql,(col1,col2))
        print a, col1, col2
        connection.commit()
connection.close()


