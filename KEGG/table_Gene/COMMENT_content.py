# fetch_COMMENT_content

fh = open('/Volumes/LACIE SHARE/genes/genome/genome')
count = 0
Tags = []
All = []
for line in fh:
    if not line.startswith('///'):
        if not line.startswith(' '):
            if line.startswith('COMMENT'):
                count += 1
                All.append(Tags)
                flags = line.split()[0]
                content = line.strip(str(flags))
                Tags = []
                Tags.append(flags)
                print count,content