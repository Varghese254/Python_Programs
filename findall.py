#find all numbers
import re
a="hello 134"
print(a)
numbers=re.findall("\d+",a)
print(numbers)
