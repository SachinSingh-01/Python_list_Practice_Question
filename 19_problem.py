'''Given:
words = ["hi", "apple", "no", "banana", "yes", "mango"]
Create a new list that contains words having length greater than 3.'''
words = ["hi", "apple", "no", "banana", "yes", "mango"]
new_list=[]
for w in words:
    if len(w)>=3:
        new_list.append(w)
print(new_list)