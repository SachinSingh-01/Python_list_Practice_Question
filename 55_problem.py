'''Remove strings but keep numbers only (int + float)
Example:
data = [10, "hello", 4.5, "yes", 20]'''
data = [10, "hello", 4.5, "yes", 20]
new_list=[]
for i in data:
    if isinstance(i, (int, float)):
        new_list.append(i)
print(new_list)