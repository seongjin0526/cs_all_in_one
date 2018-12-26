def pivo(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return pivo(n-1)+pivo(n-2)

num = int(input("구하고싶은 피보나치 수얄의 n 값은? "))
print(pivo(num))
