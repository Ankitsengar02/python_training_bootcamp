statelist = ["Delhi", "Bihar", "Goa", "Gujarat", "Assam"]

output = ''.join(item[1] for item in statelist 
                 if item[1] in "AEIOUaeiou")
a=output.upper()
b=a[::-1]
print(b)

