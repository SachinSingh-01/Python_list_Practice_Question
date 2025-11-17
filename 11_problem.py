'''From the list
num_list = [2, 7, 8, 11, 14, 21, 24, 33]
Remove all even numbers using loop (not remove() multiple times).'''
num_list = [2, 7, 8, 11, 14, 21, 24, 33]
new_list=[]
for nums in num_list:
    if (nums%2!=0):
        new_list.append(nums)
print(new_list)