'''Check if all items of list1 exist in list2
Example:
list1 = [1, 2, 3]
list2 = [3, 2, 1, 4]'''
lst1=[2,4,5,6,7,9]
lst2=[2,4,5,4,6,8,1,1,7,6,9]
flag=True
for i in (lst1):
    if i not in lst2:
        flag=False
        break
if flag:
    print("All item present")
else:
    print("item not present")
