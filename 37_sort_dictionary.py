dic={
    'a':1,
    'b':2,
    'c':3,
    'd':4,
}

assending=dict(sorted(dic.items(),key=lambda item:item[1]))
desanding=dict(sorted(dic.items(),key=lambda item:item[1],reverse=True))
print(assending)
print(desanding)