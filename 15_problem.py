# Given:colors = ["red", "blue", "black"]
# Insert "yellow" just before "black" (not using index number directly).
colors = ["red", "blue", "black"]
pos = colors.index("black") 
colors.insert(pos, "yellow")  
print(pos)
