'''Compare two lists but ignore order AND duplicates
Given:
a = [1, 2, 2, 3]
b = [3, 1, 2]'''
a = [1, 2, 2, 3]
b = [3, 1, 2]
print(set(a))
print(set(b))
if set(a)==set(b):
    print("Equal")
else:
    print("Equal")
