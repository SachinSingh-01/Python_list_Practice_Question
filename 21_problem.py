n1=int(input("Enter how many element you want to store in a list1="))
lst1=[]
for i in range (n1):
    value=input("Enter the element in the list1:")
    lst1.append(value)
n2=int(input("Enter how many element you want to store in a list2="))
lst2=[]
for i in range (n2):
    value=input("Enter the element in the list2:")
    lst2.append(value)
if len(lst1)!=len(lst2):
    print("Not same length")
else:
    print("Same length")