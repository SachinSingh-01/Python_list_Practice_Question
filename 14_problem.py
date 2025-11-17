'''Reverse a list without using:
reverse()
slicing ([::-1])'''
items = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
new_list=[]
index=len(items)-1
while index>0:
    new_list.append(items[index])
    index-=1
print(new_list)