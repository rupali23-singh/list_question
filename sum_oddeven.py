list=[23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
sum=0
while i<len(list):
    if list[i]%2==0:
        sum+=list[i]
    else:
        sum+=list[i]
    i=i+1
print(sum)