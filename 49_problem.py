'''Move all zeros to the end
Example:
nums = [0, 1, 0, 3, 12]'''
nums = [0, 1, 0, 3, 12]
new_list=[]
for i in nums:
    if i!=0:
        new_list.append(i)
zero_count=nums.count(0)
for j in range(zero_count):
    new_list.append(0)
print(new_list)
