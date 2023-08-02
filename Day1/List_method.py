#implement the method of List
list = [2, 1, 3, 4, 5]
list2= [1,"Genzeon",4.5]
list3= [list2,list]
print(list3)
print(list3[1][2])
print(list2[::-1])

list.append(6) #It will append the 6
print(list)  

list.extend([7, 8, 9]) #It will append the more than 1 element
print(list)  

list.insert(2, 100) #insert at index 2
print(list)  

list.remove(100) #remove the element from the list
print(list)  

popped_element = list.pop(4) #pop the element from index 4
print(list)  
print(list) 

list.sort() # sort the element in acending order
print(list)  

list.reverse() # reverse the list
print(list)  

count_of_3 = list.count(3) # count the number of specific element
print(count_of_3)  

list1=list.copy() # copy the list 
print(list1)

list1.clear() # remove the all the element
print(list1)
