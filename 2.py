s=input()
s_1=str(s)
for i in range(0,len(s_1)):
    if (i+1) % 3 == 0:
     print(s_1[i],end="")
