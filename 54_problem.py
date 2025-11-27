'''Create list of items that start AND end with same letter
Example:
words = ["level", "apple", "wow", "mango"]'''
words = ["level", "apple", "wow", "mango"]
new_list=[]
for i in words:
    if i[0]==i[-1]:
        new_list.append(i)
print(new_list)


