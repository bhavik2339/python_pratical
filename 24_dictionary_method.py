student=dict(name="BHAVIK",age=21,designation="PSI")
print(student)

print("length",len(student))

demo=student.copy()
demo.clear()
print("after clear",demo)

print("get name ",student.get("name"))

temp=student.copy()
r_val=temp.pop("age")
print("after pop",r_val)

temp=student.copy()
r_val=temp.popitem()
print("remove",r_val)
print("after remove",temp)

print("key",student.keys())

print("value",student.values())
print("len",len(student))