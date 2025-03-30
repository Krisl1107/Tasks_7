N=int(input())
while N>0:
    N/=2
    if N==1:
        print("Верно")
        break
    elif N<1:
        print("Неверно")
        break
