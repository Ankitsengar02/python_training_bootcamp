statelist = ["Delhi", "Bihar","UP", "Goa", "Gujarat", "Assam", "AP"]
output = ''.join(item[-2] for item in statelist 
                 if item[-2] in "AEIOUaeiou")
a=output.upper()
b=a[::-1]
print(b)
