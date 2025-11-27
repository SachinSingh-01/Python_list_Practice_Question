'''Given:

a = [5, 10, 15, 20]
b = [5, 10, 30, 20]
Check if first three elements are same.'''
a = [5, 10, 15, 20]
b = [5, 10, 30, 20]
same=True
for i in range(3):
    if a[i]!=b[i]:
        same=False
print(same)

