'''Make a List of Squares Only for Odd Numbers
From list [1to10], make:
[1, 9, 25, 49, 81]'''
lst=[1,2,3,4,5,6,7,8,9]
new_list=[]
square=0
for i in lst:
    if i%2!=0:
        square=i*i
        new_list.append(square)
print(new_list)