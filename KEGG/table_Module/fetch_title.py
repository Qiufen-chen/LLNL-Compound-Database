# -*- coding: utf-8 -*-
# Print Titles
fh = open('/Users/yingdong/Desktop/LLNL/Project/KEGGdatabase/KEGG-Download/module/module')
titles = set()

for line in fh:
    if not line.startswith(' ') and '///' not in line:
    	titles.add(line.split()[0])
print titles



#Print subline
#fh = open('/Users/yingdong/Desktop/LLNL/Project/KEGGdatabase/KEGG-Download/module/module')
#num=0
#for line in fh:
#	if line.startswith('COMMENT'):
#		num += 1
#		if num > 1000:break
#		print num,line










#'ENTRY'
#'NAME'
#'DEFINITION'
#'ORGANISM'
#'CLASS'
###'COMPOUND'
###'RMODULE'
###'REF_MODULE'
###'PATHWAY'
###'GENE'
###'ORTHOLOGY'   ---,
###'REACTION'   ---,
###'BRITE'
#'COMMENT'
#'DBLINKS'
#'REFERENCE'















