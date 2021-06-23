mainstr = "the quick brown fox jumped over the lazy dog. the dog slept over the verandah."
b=mainstr.split() 
i=0
c="on"
substr=" "
while i<len(b):
    if b[i]=="over":
        substr=substr+c+" "
    else:
        substr=substr+b[i]+" "
    i=i+1
print(substr)