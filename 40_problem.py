'''Create a New List of Items Starting With a or A
Given:fruits = ["apple", "Banana", "avocado", "Cherry", "Apricot"]'''
fruits = ["apple", "Banana", "avocado", "Cherry", "Apricot"]
new_list=[]
for i in fruits:
    if i.startswith("a") or i.startswith("A"):
        new_list.append(i)
print(new_list)