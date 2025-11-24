'''Swap First and Last Element
Example:
list1 = [10, 20, 30, 40]
Swap elements at index 0 and last index without using temp variable.'''
list1 = [10, 20, 30, 40]
list1[0],list1[-1]=list1[-1],list1[0]
print(list1)
