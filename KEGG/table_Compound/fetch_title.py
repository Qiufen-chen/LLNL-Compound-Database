# -*- coding: utf-8 -*-
# Print Titles
fh = open('/Users/yingdong/Desktop/LLNL/Project/KEGGdatabase/table_Compound/compound')
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































