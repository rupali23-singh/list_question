number = 30
n = [10, 11, 12, 13, 14, 17, 18, 19] 
i=0
a=[]
while i<len(n):
    j=0
    while j<len(n):
        if n[i]+n[j]==30:
            sum_n=[n[i],n[j]]
            a.append(sum_n)
        j=j+1
    i+=1
print(a)