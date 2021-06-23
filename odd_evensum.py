list=[23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43]
i=0
sum=0
sum1=0
sum_all=0
while i<len(list):
    sum_all+=list[i]
    if list[i]%2==0:
        sum+=list[i]
    else:
        sum1+=list[i]
    i=i+1
print(sum,sum1,sum_all)