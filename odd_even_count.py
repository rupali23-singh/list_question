list=[23,14,56,12,19,9,15,25,31,42,43]
i=0
c=0
sum=0
while i<len(list):
    if list[i]%2==0:
        sum+=list[i]
    else:
        sum+list[i]
        c=c+1
    i=i+1
sum=sum/c
print(sum