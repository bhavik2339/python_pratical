#break statement
group=[1,2,3,4,5,6]
search=int(input("enter element to search"))

for element in group:
    if search==element:
        print("element found in group")
        break
else:
    print("element not found in group")



#pass statement
num=[1,2,3,-4,-5,-6,-7,-8,-9]
for i in num:
    if(i<0):
        pass
    else:
        print(i)

#countinue statement
for i in range(1,11):
    if i==6:
        continue
    print(i)