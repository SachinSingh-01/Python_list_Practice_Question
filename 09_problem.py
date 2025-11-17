# Write a program to remove all occurrences of 'apple' from a list.
fruit=["apple","banana","cherry","apple","doggy","apple"]
while "apple" in fruit:
    fruit.remove("apple")
print(fruit)