'''Find all indexes of "apple" in:
fruits = ["apple", "banana", "apple", "cherry", "apple", "kiwi"]'''
fruits = ["apple", "banana", "apple", "cherry", "apple", "kiwi"]
for i in range(len(fruits)):
    if fruits[i]=="apple":
        print(i)