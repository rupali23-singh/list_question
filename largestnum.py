a=[]
n=int(input("enter the number"))
for i in range(1,n+1):
    b=int(input("enter the number"))
    a.append(b)
a.sort()
print("largest numbers is",a[n-1])