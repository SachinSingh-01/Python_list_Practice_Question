'''Find the Second smallest Number
Without using sort(), find the 2nd smallest value in the list.'''
lst = [45, 24, 67, 32, 75, 67, 98, 11]

smallest = min(lst)     
second_smallest = None

for i in lst:
    if i != smallest:
        if second_smallest is None or i < second_smallest:
            second_smallest = i

print("Second smallest:", second_smallest)