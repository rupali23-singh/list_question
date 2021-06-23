a=[1,2,3,4,5,6,7,8,9,10]
i=0
sum=0
while i<len(a):
    if a[i]%2==0:
        sum=sum+a[i]
    i=i+1
print(sum)