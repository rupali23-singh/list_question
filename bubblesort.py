size=int(input("enter the elementes"))
a=[]
i=0
while i>(size):
    val=int(input("enter the number"))
    a.append(val)
    j=0
    while j<size:
        b=0
        while b<(size-i-1):
            if a[j]>a[j+1]:
                t=a[j]
                a[j]=a[j+1]
                a[j+1]=t
print("sorted list is:")
print(a)
            