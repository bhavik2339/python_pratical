a={10,20,30,40}
b={30,40,50,60}

#add
a.add(17)
print(a)

#update
a.update([60,70])
print(a)

#copy
cp=a.copy()
print(cp)

#pop
a.pop()
print("remove all item",a)

#remove
a.remove(10)
print(a)

#discard
a.discard(20)
print(a)

#union
print("union",a.union(b))

#intersection
print("intersection",a.intersection(b))


#diffrence
print("difference",a.difference(b))