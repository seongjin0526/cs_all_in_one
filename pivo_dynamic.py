def pivo(n):
    '''
    피보나치 수열의 초기값을 정해둔 후 2번째 이후부터 값을 계산한다.
    '''
    fi_list=[0,1]
    for i in range(2,n+1):
        fi_list.append(fi_list[i-1]+fi_list[i-2])
    return fi_list[-1]

num = int(input("구하고싶은 피보나치 수얄의 n 값은? "))
print(pivo(num))
