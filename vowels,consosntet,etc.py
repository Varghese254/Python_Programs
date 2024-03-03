#read a sentenece-count the vowels,consonanat,digit,special char of each word
from string import digits


text=input("enter a sentenece:")
vowels=cons=digit=spec=0
for char in text:
    if char in "aeiouAEIOU":vowels+=1
    if char in "bBcCdDfFgGhHjJkKmnpPQrRsSTtUuVvWXxYyZz":cons+=1
    if char in "0123456789":digits+=1
    if char in "@#$":spec+=1
print("vowels:",vowels)
print("consosnat:",cons)
print("digit:",digits)
print("special char:",spec)

