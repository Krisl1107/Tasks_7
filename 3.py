import math
n=int(input())
if math.sqrt(n)%1==0:
    print("Число является полным квардратом")
else:
    print("Число не является полным квардратом")
m=int(input())
while math.sqrt(m)%1!=0:
    m = int(input("Введите другое число"))
    if math.sqrt(m) % 1 == 0:
        print("Число является полным квардратом")
