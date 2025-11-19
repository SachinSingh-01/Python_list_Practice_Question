# Write a program to check if two lists are exactly same (same order & values) without using == operator.
list1 = [1, 2, 3]
list2 = [1, 2, 3]
if len(list1)!=len(list2):
    print("Not Equal list")
else:
    equal=True
for i in range (len(list1)):
    if list1[i]!=list2[i]:
        equal=False
        break
if equal:
    print("Equal list")
else:
    print("Not Equal list")

