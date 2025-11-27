'''Replace words with their lengths
Given:
words = ["apple", "hi", "banana", "dog"]
Make a new list containing length of each word.'''
words = ["apple", "hi", "banana", "dog"]
new_list=[]
for i in words:
    new_list.append(len(i))
print(new_list)
