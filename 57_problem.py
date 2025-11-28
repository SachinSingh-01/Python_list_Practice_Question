'''Find difference of two lists (items in list1 not in list2)
Example:
a = [1, 2, 3, 4]
b = [2, 4, 5]'''
a = [1, 2, 3, 4]
b = [2, 4, 5]
new_list=[]
for i in a:
    if i not in b:
        new_list.append(i)
print(new_list)
        
