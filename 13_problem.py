# From the same items list, find how many times 'apple' appears (without using count() method).
items = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
count=0
for fruits in items:
    if "apple" in fruits:
        count+=1
print("No. of times apple present",count)