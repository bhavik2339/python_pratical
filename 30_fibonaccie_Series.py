num = int(input("Enter a number: "))
a,b = 0,1

print("fibonacci series :")

if num<=0:
    print("please enter the positive number")
else:
    print("fibonacci series :")
    for i in range(1,num+1):
        print(a,end=" ")
        a,b = b,a+b