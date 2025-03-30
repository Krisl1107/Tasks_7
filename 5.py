N=int(input())
s=0
s_1=0
for i in range(1,10000):
 if s<N and s_1<N:
  s=i**3
  s_1=(i+1)**3
  print(s,end=" ")
 else:
     break
