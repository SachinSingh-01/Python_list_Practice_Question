# Q1. Create a list of 5 numbers and print it.
lst=[4,6,6,7,3]
print(lst)

# Q2. Print the first and last item of a list.
lst=[4,6,6,7,3]
print("first element",lst[0])
print("last element",lst[4])

# Q3. Print the length of a list without using loops.
lst=[5,6,7,2,1,7,8]
print("The length of the list=",len(lst))

# Q4. Change the 2nd item of a list to "banana".
fruits=["apple","cherry","kiwi","mango","papaya"]
fruits[1]=("banana")
print(fruits)

# Q5. Add "kiwi" at the end of a list.
fruits=["apple","cherry","banana","mango","papaya"]
fruits.append("kiwi")
print(fruits)

# Q6. Insert "orange" at index 1.
fruits=["apple","cherry","banana","mango","papaya"]
fruits.insert(1,"orange")
print(fruits)

# Q7. Remove the last item using pop().
fruits=["apple","cherry","banana","mango","papaya"]
fruits.pop(-1)
print(fruits)

# Q8. Remove a specific item like "apple" using remove().
fruits=["apple","cherry","banana","mango","papaya"]
fruits.remove("apple")
print(fruits)

# Q9. Make a list of 3 fruits and print each fruit in a loop.
lst=["apple","banana","kiwi"]
for i in lst:
    print(i)

# Q10. Make a list and print items with their index.
lst=["apple","banana","kiwi","cherry","orange","watermelon"]
for i in lst:
    print(i,":",lst.index(i))
