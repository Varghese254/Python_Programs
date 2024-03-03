#loop with condition in the middle
vowels="aeiou"
#infinite loop
while True:
    v=input("enter a letter:")
    if v in vowels:
        print(v,"is a vowel")
        break
    print("not a vowel,try another letter!")
    
