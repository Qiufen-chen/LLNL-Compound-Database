import pymysql.cursors

connection = pymysql.connect(host='localhost',
                             user='root',
		                     port=3306,
                             cursorclass=pymysql.cursors.DictCursor)
cursor = connection.cursor()

with open('/Users/yingdong/Downloads/genome/genome_tax.list') as fh_tax:
    a = 0
    for line in fh_tax:
        col1 = (line.split()[0]).split(':')[1]
        col2 = (line.split()[1]).split(':')[1]
        a += 1
        sql = """insert into KEGG.Genome_Tax (Genome,Taxonomy) 
                 values
                 (%s, %s)
        """
        cursor.execute(sql,(col1,col2))
        print a, "tax loaded"

with open('/Users/yingdong/Downloads/genome/genome_refseq.list') as fh_refseq:
    b = 0
    for line in fh_refseq:
        col1 = (line.split()[0]).split(':')[1]
        col2 = (line.split()[1]).split(':')[1]
        b += 1
        sql = """insert into KEGG.Genome_Refseq (Genome,Refseq) 
                 values
                 (%s, %s)
        """
        cursor.execute(sql,(col1,col2))
        print b, "refseq loaded"

with open('/Users/yingdong/Downloads/genome/genome_pubmed.list') as fh_pubmed:
    c = 0
    for line in fh_pubmed:
        col1 = (line.split()[0]).split(':')[1]
        col2 = (line.split()[1]).split(':')[1]
        c += 1
        sql = """insert into KEGG.Genome_Pubmed (Genome,Pubmed) 
                 values
                 (%s, %s)
        """
        cursor.execute(sql,(col1,col2))
        print c, "pubmed loaded"


with open('/Users/yingdong/Downloads/genome/genome_pathway.list') as fh_pathway:
    d = 0
    for line in fh_pathway:
        col1 = (line.split()[0]).split(':')[1]
        col2 = (line.split()[1]).split(':')[1]
        d += 1
        sql = """insert into KEGG.Genome_Pathway (Genome,Pathway) 
                 values
                 (%s, %s)
        """
        cursor.execute(sql,(col1,col2))
        print d, "pathway loaded"

with open('/Users/yingdong/Downloads/genome/genome_module.list') as fh_module:
    e = 0
    for line in fh_module:
        col1 = (line.split()[0]).split(':')[1]
        try:
            col2 = (line.split()[1]).split(':')[1]
        except:
            pass
        e += 1
        sql = """insert into KEGG.Genome_Module (Genome,Module) 
                 values
                 (%s, %s)
        """
        cursor.execute(sql,(col1,col2))
        print e, "module loaded"

with open('/Users/yingdong/Downloads/genome/genome_genbank.list') as fh_genbank:
    f = 0
    for line in fh_genbank:
        col1 = (line.split()[0]).split(':')[1]
        col2 = (line.split()[1]).split(':')[1]
        f += 1
        sql = """insert into KEGG.Genome_Genbank (Genome,Genbank) 
                 values
                 (%s, %s)
        """
        cursor.execute(sql,(col1,col2))
        print f, "genbank loaded"

with open('/Users/yingdong/Downloads/genome/genome_disease.list') as fh_disease:
    g = 0
    for line in fh_disease:
        col1 = (line.split()[0]).split(':')[1]
        col2 = (line.split()[1]).split(':')[1]
        g += 1
        # combind the disease data from 'genome_disease.list' with 'genome' into the same table.
        sql = """insert ignore into KEGG.Genome_Disease (Entry,Disease) 
                 values
                 (%s, %s)
        """
        cursor.execute(sql,(col1,col2))
        print g, "disease loaded"

with open('/Users/yingdong/Downloads/genome/genome_compound.list') as fh_compound:
    h = 0
    for line in fh_compound:
        col1 = (line.split()[0]).split(':')[1]
        col2 = (line.split()[1]).split(':')[1]
        h += 1
        sql = """insert into KEGG.Genome_Compound (Genome,Compound) 
                 values
                 (%s, %s)
        """
        cursor.execute(sql,(col1,col2))
        print h, "compound loaded"

with open('/Users/yingdong/Downloads/genome/genome_brite.list') as fh_brite:
    i = 0
    for line in fh_brite:
        col1 = (line.split()[0]).split(':')[1]
        col2 = (line.split()[1]).split(':')[1]
        i += 1
        sql = """insert into KEGG.Genome_Brite (Genome,Brite) 
                 values
                 (%s, %s)
        """
        cursor.execute(sql,(col1,col2))
        print i, "brite loaded"

with open('/Users/yingdong/Downloads/genome/genome_assembly.list') as fh_assembly:
    j = 0
    for line in fh_assembly:
        col1 = (line.split()[0]).split(':')[1]
        col2 = (line.split()[1]).split(':')[1]
        j += 1
        sql = """insert into KEGG.Genome_Assembly (Genome,Assembly) 
                 values
                 (%s, %s)
        """
        cursor.execute(sql,(col1,col2))
        print j, "assembly loaded"
        connection.commit()
connection.close()


