# -*- coding: utf-8 -*-
# Print Titles
fh = open('/Users/yingdong/Desktop/LLNL/Project/KEGGdatabase/table_Enzyme/enzyme')
titles = set()

for line in fh:
    if not line.startswith(' ') and '///' not in line:
    	titles.add(line.split()[0])
print list(titles)



#Print subline
#num=0
#for line in fh:
	#if line.startswith('#GENES'):
		#num += 1
		#if num > 1000:break
		#print line



#ENTRY

#NAME ---
#CLASS --- ？
#REACTION ---
#ALL_REAC ---
#SUBSTRATE ---
#PRODUCT ---
#DBLINKS ---
#SYSNAME
#HISTORy
#COMMENT

#ORTHOLOGY ---
#GENES ---
#PATHWAY---




#REFERENCE
























