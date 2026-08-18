#list
a=list("python")
print("list is a",a)

#length
num=[1,2,3,4,5,6,7,7,8,9]
print("len = ",len(num))

#count
print("count = ",num.count(7))

#index
print("index = ",num.index(7))

#append
num.append(25)
print("append = ",num)

#insert
num.insert(1,25)
print("insert = ",num)

#extend
num.extend([20,10])
print("extend = ",num)

#remove
num.remove(7)
print("remove = ",num)

#pop
num.pop(2)
print("pop = ",num)

#reverse
num.reverse()
print("reverse = ",num)

#sort
num.sort()
print("sort = ",num)

#copy
num.copy()
print("copy = ",num)

#clear
num.clear()
print("clear = ",num)