for i in range(0,6):
    for j in range(0,i):
        print(i,end=" ")
    print(end="\n")

"""
print("A")
print("A B")
print("A B C")
print("A B C D")
print("A B C D E")
print("A B C D F")
"""

for i in range(0,6):
    for j in range(i):
        print(chr(65+j),end=" ")
    print("\n")


for i in range(5,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()