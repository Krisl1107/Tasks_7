i=0
k=0
ch=0
m=1
tmp=[]
tmp_1=[]
while m!=0:
    m=float(input())
    k+=1
    if k==1:
     tmp.append(m)
    else:
     tmp.append(m)
     tmp_1.append(m)

for i in range(1,k):
    m=tmp[i-1]
    n=tmp_1[i-1]
    if m>n:
        ch+=1
    else:
        ch+=0
print(ch-1)
