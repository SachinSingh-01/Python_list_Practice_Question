'''Convert Nested List to Single List
For:list1 = [[1, 2], [3, 4], [5]]'''
list1 = [[1, 2], [3, 4], [5]]
new_list=[]
for i in list1:
    for value in i:
        new_list.append(value)
print(new_list)