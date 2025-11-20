'''Compare lists manually
Given:
x = [1, 2, 3]
y = [1, 2, 3]
Check if they are exactly same without using ==.'''
x=[1,5,6]
y=[1,2,5,6]
lst=True
if len(x)!=len(y):
    lst=False
for i in range(len(x)):
    if x[i]!=y[i]:
        lst=False
        break
if lst:
    print("Equal list")
else:
    print("Not equal list")