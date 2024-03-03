#read a string-eg: "apples are from africa" - replece with $ at 'a' position expect the 1st word.
str=input("enter the string:")
char=str[0]
str=str.replace(char,"$")
str=char+str[1:]
print(str)
