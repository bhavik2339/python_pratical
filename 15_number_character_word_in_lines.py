file=open("demo.txt","r")
content=file.read()

char=len(content)
wor=content.split()
lin=content.splitlines()

print("number of character ",char)
print("numebr of words",wor)
print("number of lines",lin)
