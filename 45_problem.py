'''Compare List Values But Ignore Case
Given:
a = ["Apple", "banana", "MANGO"]
b = ["apple", "BANANA", "mango"]
Check if lists are same ignoring uppercase/lowercase.'''
a = ["Apple", "banana", "MANGO"]
b = ["apple", "BANANA", "mango"]
a_lower = [i.lower() for i in a]
b_lower = [i.lower() for i in b]

if a_lower == b_lower:
    print("Lists are same (ignoring case)")
else:
    print("Lists are NOT same")

