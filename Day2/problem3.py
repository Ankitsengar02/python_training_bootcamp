statelist = ["Delhi", "Telangana", "Goa", "AP", "Kerala"]
output = ''.join(item[0] + item[-1] for item in statelist)
a=output.swapcase()
print(a)



