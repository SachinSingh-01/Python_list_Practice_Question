'''Remove duplicates but keep last occurrence
Given:
a = [1, 2, 3, 2, 1, 4]'''
a = [1, 2, 3, 2, 1, 4]
new_list=[]
for i in reversed(a):
    if i not in new_list:
        new_list.append(i)
new_list.reverse()
print(new_list)
