str=["orange","white","red","cyan","green","magenta","cyan","pink","white"]
str1=set(str)
str2=sorted(str1)
print(str2)

str=["orange","white","red","cyan","green","magenta","cyan","pink","white"]
str1=set(str)
str2=','.join(sorted(str1))
print(str2)

str = ["orange", "white", "red", "cyan", "green", "magenta", "cyan", "pink", "white"]
str1 = sorted(list(set(str)))   #we can remove list as well
print(str1)

str = ["orange", "white", "red", "cyan", "green", "magenta", "cyan", "pink", "white"]
str1 = sorted(set(str), key=lambda str: (str.index(str), str))
print(str1)


str = ["orange", "white", "red", "cyan", "green", "magenta", "cyan", "pink", "white"]
str1 = []
for item in str:
    if item not in str1:
        str1.append(item)
str1.sort()
print(str1)

