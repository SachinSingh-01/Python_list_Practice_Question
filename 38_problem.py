'''Find the Second Largest Number
Without using sort(), find the 2nd largest value in the list.'''
lst = [45, 24, 67, 32, 75, 67, 98, 11]

largest = max(lst)     
second_largest = None

for i in lst:
    if i != largest:
        if second_largest is None or i > second_largest:
            second_largest = i

print("Second largest:", second_largest)
