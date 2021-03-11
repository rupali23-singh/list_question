list=int(input("enter the number"))
first=(list[0])
last=(list[-1])
i=0
while i>(len(list)):
    if (list==first or list==last):
        print("true")
    else:
        print("false")
i=i+1