#implement the method of Dictionary
set1={1,2}
set2={1,2,3,"hi"}

set1.add(3)
print(set1)

l=[2,3,4,5]
Set3=set(l)
print(Set3)
Set3.update([7,8,9])
print(Set3)
Set3.remove(9)
print(Set3)

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set3 = {1,2,3}
union_set = set1 | set2 # all the element without repeating
print(union_set)

intersection_set = set1 & set2
print(intersection_set) # only matching element

difference_set = set1 - set2 #first set element which is not in the second set
print(difference_set)

sym_Diff = set1 ^ set2 #all the element which in not common in both the sets
print(sym_Diff)

is_subset = set1 <= set2
print(is_subset)    # set1 is subset of set2 or not
is_subset = set3 <= set1
print(is_subset) # set3 is subset of set1 or not

is_superset = set1 >= set3 # set3 is superset of set1 or not
print(is_superset)