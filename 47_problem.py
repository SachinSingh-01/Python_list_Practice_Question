'''Find all items that appear more than once
Example:
nums = [1, 2, 3, 2, 4, 1, 5, 2]'''
nums = [1, 2, 3, 2, 4, 1, 5, 2]
new_list=[]
for i in nums:
    if nums.count(i) > 1:     
        if i not in new_list:
            new_list.append(i)
print(new_list)