'''Are two lists reverse of each other?
Example:
a = [1, 2, 3]
b = [3, 2, 1]
Check if b is the reverse version of a.'''
a = [1, 2, 3]
b = [5, 2, 1]
rev=True
for i in range(len(a)):
    if b[i]!=a[len(a) - 1 - i]:
        rev=False
        break
if rev:
    print("Reverse version")
else:
    print("not a reverse order")