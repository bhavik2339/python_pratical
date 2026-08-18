#if statement
num=1
if num==1:
    print("one")
    print("two")
    print("third")


#if else statement
x=int(input("enter any number:"))
if x%2==0:
    print("number is even")
else:
    print("number is odd")


#if elif else statement
no1=45
no2=20
no3=10
if no1>no2 and no1>no3:
    print("number 1 is big")
elif no2>no1 and no2>no3:
    print("number 2 is big")
else:
    print("number 3 is big")
