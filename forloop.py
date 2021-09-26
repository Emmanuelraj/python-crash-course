# for loop
for i in range (10):
    print(i)

# start, stop, step for loops 
for i in range (10, -1, -1): 
    print(i) # dec

# iterte the list

list = [1,4,5,2,3,5]

for i in range (len(list)):
    print('list',list[i])


# enumerate  will provide both index and value(element)

for i, element in enumerate(list):
    print(i,element)
    print('element',element)    
