# -*- coding: utf-8 -*-
fh = open('/Users/yingdong/Downloads/ko')
titles = set()
count = 0
for line in fh:
    if not line.startswith(' ') and '///' not in line:
        titles.add(line.split()[0])
print list(titles)

# BRITE
# NAME
# REFERENCE
# DEFINITION
# GENES
# DISEASE
# MODULE
# DBLINKS
# ENTRY
# PATHWAY
