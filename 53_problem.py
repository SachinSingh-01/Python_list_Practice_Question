'''Separate numbers into even and odd lists
Example:
nums = [1, 2, 3, 4, 5, 6]'''
nums = [1, 2, 3, 4, 5, 6]
even_list=[]
odd_list=[]
for i in nums:
    if i%2==0:
        even_list.append(i)
    else:
        odd_list.append(i)
print(even_list)
print(odd_list)
