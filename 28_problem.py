'''Find common elements (intersection)
Given
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]'''
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
intersection=[]
for item in a:
    if item in b:
        intersection.append(item)
print(intersection)
   