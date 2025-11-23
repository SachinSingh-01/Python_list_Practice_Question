# For:a = [1, 2, 3, 4, 5]
# Remove the middle element (without using index directly)
a = [1, 2, 3, 4, 5]

middle_index = len(a) // 2      
middle_value = a[middle_index]  
a.remove(middle_value)         
print(a)
