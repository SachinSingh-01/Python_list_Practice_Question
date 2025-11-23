'''For:
colors = ['red', 'blue', 'yellow', 'green']
Insert "black" exactly at the middle index (calculate dynamically).'''
colors = ['red', 'blue', 'yellow', 'green']
pos=colors.index("yellow")
colors.insert(pos,"black")
print(pos)
print(colors)