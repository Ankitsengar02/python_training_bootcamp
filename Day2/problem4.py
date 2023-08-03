statelist = ["Delhi", "Bihar", "Goa", "Gujarat", "Assam"]

output = ''.join(item[len(item)//2] for item in statelist 
                 if item[len(item)//2] in "AEIOUaeiou")
a=output.upper()
b=a[::-1]
print(b)

