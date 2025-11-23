'''Example:
data = [10, "apple", True, "banana", 3.14, "cat"]
Count how many items are strings without using type() directly inside if.'''
data = [10, "apple", True, "banana", 3.14, "cat"]
count=0
for i in data:
    s=str(i)
    if s==i:
        count+=1
print("No. of string item=",count)