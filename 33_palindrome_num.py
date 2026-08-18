num=int(input("enter a number:"))
original=num
reverse=0

while num>0:
    digit=num%10
    reverse=reverse*10+digit
    num=num//10

if original==reverse:
    print(original,"is palindrome")
else:
    print(original,"is not a palindrome")