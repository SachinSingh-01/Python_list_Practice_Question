'''Remove All Items Except Numbers
From:
mixed = [10, "hi", 20, 3.5, "apple", True, 40]
Create a list that contains only integers (no float, no string).'''
mixed = [10, "hi", 20, 3.5, "apple", True, 40]
new_list=[]
for i in mixed:
    if type(i) is int:
        new_list.append(i)
print(new_list)