list_1=[6,1,3,5,6,3,1]
i=0
empty=[]
c=0
while i<len(list_1):
    if list_1 != empty:
        c+=1
    if list_1[i] not in(empty):
        empty.append(list_1[i])
    i=i+1
print(empty)
  