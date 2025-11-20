# Write a program that prints the first position where two lists are different.
# lst1=[2,4,5,6]
# lst2=[2,4,5,5]
# for i in range(len(lst1)):
#     if lst1[i]!=lst2[i]:
#         print("Position of the different index value:",i)
#         break

# If you want to find all the positions where two lists are different, not just the first one, then you must:
a=[2,4,6,7,8]
b=[2,4,9,3,8]
different_index=[]
for i in range(len(a)):
    if a[i]!=b[i]:
        different_index.append(i)
print("Position of the different index value:",different_index)