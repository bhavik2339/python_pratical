file=open("demo.txt","r")
stor=file.read()

frequency={}
for chr in stor:
    if chr in frequency:
        frequency[chr]+=1
    else:
        frequency[chr]=1

print(frequency)