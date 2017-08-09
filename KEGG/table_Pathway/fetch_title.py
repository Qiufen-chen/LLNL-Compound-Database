# -*- coding: utf-8 -*-
# Print Titles
fh = open('pathway_content.txt')
titles = set()
for line in fh:
    #if not line.startswith(' ') and '///' not in line:
        #titles.add(line.split()[0])
    if line.startswith('GENE'):
       titles.add(line.split()[1].lstrip())
       #print titles
       if 'HHS_0629' in titles:
           print "yes!"
#print titles

#Print Gene
#fh = open('pathway_content.txt')
#gene = set()
#num=0
#for line in fh:
#   if line.startswith('GENE'):
 #      gene.add(line.split()[1])
   #     num += 1
#geneheading = list(gene)
#print num, geneheading






#'REACTION' √
#'NAME' √
#'REFERENCE' √
#'KO_PATHWAY' √
#'ORTHOLOGY' √
#'DISEASE' √
#'MODULE' √
#'ENZYME'√
#'DRUG'√
#'DBLINKS' √
#'COMPOUND' √
#'ENTRY' √
#'GENE' √
#'ORGANISM'
#'CLASS' √
#'DESCRIPTION' √

