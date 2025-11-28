'''Check if list is strictly increasing
Example:
[1, 2, 5, 7] → True
[1, 3, 3, 4] → False'''
lst=[1, 2, 5, 7]
strictly=True
for i in range(1,len(lst)):
    if lst[i]<=lst[i-1]:
        strictly=False
        break
if strictly:
    print("yes increase")
else:
    print("no not increase")