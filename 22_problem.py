'''Given:
a = [10, 20, 30]
b = [10, 50, 30]
Count how many indexes have the same value.'''
a = [10, 20, 30]
b = [10, 50, 30]
count=0
for i in range (len(a)):
    if a[i]==b[i]:
        count+=1
print(count)