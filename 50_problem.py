'''Count how many items are lists
Example:
data = [1, [2, 3], "hi", [4], True]'''
data = [1, [2, 3], "hi", [4], True]
count=0
for i in data:
    if type(i)== list:
        count+=1
print(count)