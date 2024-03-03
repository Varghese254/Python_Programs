#reguklar expresion -sub() searcg and replace
import re
zipcode="2009#-098$-765a"
print(zipcode)
num=re.sub(r'\d',"@",zipcode)
print(num)
