lis=[10,20,30,40,50]

new_list=[value for index, value in enumerate(lis)
    if index not in [0,2,3,4]]

print("originally value",lis)
print("new value",lis)