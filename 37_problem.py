'''Given:
a = [1, 2, 2, 3, 3]
b = [3, 1, 2]
Check if they contain the same unique elements.'''
a = [1, 2, 2, 3, 3]
b = [3, 1, 2]
unique_list1=set(a)
unique_list2=set(b)
print(unique_list1)
print(unique_list2)
if unique_list1==unique_list2:
    print("All match")
else:
    print("not match")