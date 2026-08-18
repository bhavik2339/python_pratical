number = int(input("Enter a number:"))
original = number
order=len(str(number))
total=0

while number>0:
    digit=number%10
    total+=digit**order
    number//=10

if total==original:
    print(original,"is a aramstrong number")
else:
    print(original,"is not a aramstrong number")