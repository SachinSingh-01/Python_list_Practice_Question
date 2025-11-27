'''Reverse only half of the list
For:
nums = [10, 20, 30, 40, 50, 60]'''
nums = [10, 20, 30, 40, 50, 60]
new_list=[]
for i in nums:
    if len(i)>3:
        nums.reverse()
        new_list.append(i)
print(new_list)