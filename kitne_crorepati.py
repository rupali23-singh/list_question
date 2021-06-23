kitna_paisa_hai= [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510, 4100] 
a=0
b=0
c=0
d=kitna_paisa_hai[0]
i=0
while i<len(kitna_paisa_hai):
    if kitna_paisa_hai[i]>10000000:
        c+=1
    elif kitna_paisa_hai[i]>100000:
        a+=1
    else:
        b+=1
    i=i+1
print(c,"crorepati")
print(a,"lakhpati")
print(b,"dilwale")