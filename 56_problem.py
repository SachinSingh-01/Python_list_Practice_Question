'''Flatten nested list up to 2 levels
Given:
data = [1, [2, 3], [4, [5]], 6]'''
data = [1, [2, 3], [4, [5]], 6]
new_list=[]
for i in data:
    if isinstance(i,list):
        for x in i:
            if isinstance(x,list):
                for y in x:
                    new_list.append(y)
            else:
                new_list.append(x) 
    else:        
        new_list.append(i)
print(new_list)