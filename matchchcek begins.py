import re
line="python"
#search fuction
searchobj=re.search('gram',line,re.I)
if searchobj:
    print("serch found")
else:
    print("search not found")
