file = open("demo1.txt","r")
count=file.readlines()
for count in reversed(count):
    print(count.strip())