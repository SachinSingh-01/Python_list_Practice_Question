'''Given:numbers = [12, 7, 4, 9, 10, 3, 8]
Create a new list of indexes where numbers are even.'''
numbers = [12, 7, 4, 9, 10, 3, 8,7,2,8,1,9]
new_list=[]
for i in numbers:
    if i%2==0:
        new_list.append(i)
print(new_list)