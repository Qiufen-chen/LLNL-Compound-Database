# -*- coding: utf-8 -*-
fh = open('/Volumes/LACIE SHARE/genes/genome/genome')
titles = set()
count = 0
for line in fh:
    if not line.startswith(' ') and '///' not in line:
        titles.add(line.split()[0])
print list(titles)

# COMMENT
# DEFINITION
# DATA_SOURCE
# NAME REFERENCE
# CREATED
# TAXONOMY
# DISEASE
# STATISTICS
# PLASMID
# DBLINKS
# KEYWORDS
# ENTRY
# ANNOTATION
# CHROMOSOME
# ORIGINAL_DB
