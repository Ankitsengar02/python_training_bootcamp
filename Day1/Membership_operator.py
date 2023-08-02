#membership operator
#it will return true or false

list = [1, 2, 3, 4, 5]
print(3 in list)  

str = "Hello, World!"
print('H' in str) 

print(6 not in list)  
print('Z' not in str) 

fruits = ['Java', 'MERN', 'Python']
choice = input("Enter a TECH: ")

if choice in fruits:
    print("You chose a TECH from the list.")
else:
    print("The TECH you entered is not in the list.")
