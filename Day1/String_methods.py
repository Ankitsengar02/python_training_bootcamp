#implement the method of string

str="Genzeon Healthcare"
a=str.capitalize() #first latter of string become capital
print(a)

b=str.count("e") #count the word or string
print(b)

c=str.index("z") #it will give error or exit the program if index not found
print(c)

d=str.isalnum() #returns true if it is alphanumeric string(No space should be there)
print(d)

e=str.istitle() #true if it is title (every word first letter is Capital)
print(e)

f=str.swapcase()
print(f) #upper to lower or lower to upper

g=str.endswith("e") #return true or false
print(g)

h=str.isprintable() #returns true if ther\n then return false
print(h)

str1="  "
print(str1.isspace()) #true if whole string is in space

str2="Genzeon!!!"
print(str2.rstrip("!")) #t will remove ! from the tailing string