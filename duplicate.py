a=[10,20,30,10,"anil","anil","mukesh"]
b=[]
for x in a:
    if x not in b:
        b.append(x)
print(b)