#Identity operators

x = [1, 2, 3]
y = x
print(x is y)  

x = [1, 2, 3]
y = [1, 2, 3]
print(x is not y)  
print("_______________")
x1=5
y1=5
x2="hello"
y2="hello"
x3=[1,2,3]
y3=[1,2,3]
print(x1 is not y1)#False
print(x2 is not y2)#False
print(x3 is not y3)#True

