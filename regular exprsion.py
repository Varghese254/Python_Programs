#regular exprssion
import re
line="python is simple"
matchobj=re.match("fun",line)
if matchobj:
    print("match found:")
else:
    print("match not found")
    
