# Write a program to check if two lists have the same length.
# lst1=[1,2,4]
# lst2=[1,2,2]
# if len(lst1)!=len(lst2):
#     print("Not same length")
# else:
#     print("Same lenght")


lst1=input(("Enter the value of list1="))
lst2=input(("Enter the value of list2="))
lst1=[]
lst2=[]
if len(lst1)!=len(lst2):
    print(f"{lst1} and {lst2} are not equal")
else:
    print(f"{lst1} and {lst2} are same")