N,K,R=map(int,input().split())
d=1
while N<=R:
    N*=(1+K/100)
    d+=1
print(d)
