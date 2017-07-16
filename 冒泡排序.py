def maopao(b):
for i in range(len(b)-1):
     for j in range(len(b)-i-1):
             if b[j] > b[j+1]:
                     b[j],b[j+1]=b[j+1],b[j]
return b
print maopao(a)
