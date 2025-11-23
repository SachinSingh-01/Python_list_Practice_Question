# # Q11. Replace the first 3 items of a list with ["a", "b", "c"].
lst=["apple","banana","cherry","watermelon"]
lst[0:2]=["a", "b", "c"]
print(lst)

# Q12. Check if "apple" is present in the list.
lst=["apple","banana","cherry","watermelon"]
if "apple" in lst:
    print("Yes it is present")
else:
    print("No not present")

# Q13. Count how many times 10 appears in the list using loop.
lst=[1,45,76,10,98,34,10,45,10,34,10]
count=0
for i in lst:
    if i==10:
        count+=1
print("No. of time 10 appears in list:",count)

# Q14. Create a new list containing only even numbers from [1–10].
lst=[1,2,3,4,5,6,7,8,9,10]
new_lst=[]
for i in lst:
    if i%2==0:
        new_lst.append(i)
print("List of even number:",new_lst)

# Q15. Print list items in reverse order using a loop (no slicing).
lst=[1,2,3,4,5,6,7,8,9,10]
new_list=[]
index=len(lst)-1
while index>=0:
    new_list.append(lst[index])
    index-=1
print(new_list)

# Q15.using for loop
lst=[1,2,3,4,5,6,7,8,9,10]
new_list=[]
for i in range(len(lst)-1,-1,-1):
    new_list.append(lst[i])
print(new_list)

# Q16. Add all items of list2 into list1 using extend().
lst1=[1,2,3,4,5,6,7,8,9,10]
lst2=["apple","banana","cherry","watermelon"]
lst2.extend(lst1)
print(lst2)

# Q17. Find the largest and smallest number in a list (no max(),min()).
lst=[34,65,23,87,98,12,34,76,87]
largest=lst[0]
smallest=lst[0]
for i in lst:
    if i>largest:
        largest=i
    elif i<smallest:
        smallest=i
print("largest number:",largest)
print("smallest number:",smallest)

# Q19. Create a list of names and print only names with length > 4.
lst=["sachin","moni","ajay","vid","sak","umberlla"]
new_list=[]
for i in lst:
    if len(i)>4:
        new_list.append(i)
print(new_list)

# Q20. Create a new list with uppercase versions of all strings (list comprehension allowed).
lst=["sachin","moni","ajay","vid","sak","umberlla"]
new_list=[]
for i in lst:
    if i.upper():
        new_list.append(i.upper())
print(new_list)