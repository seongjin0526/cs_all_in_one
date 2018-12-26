'''
    some_list=[1,"1","one",,4.567,{1:"one"}]
    some_list의 요소를 str 객체의 요소인 list로 출력
    filter, lambda, isinstance 내장함수사용
'''

some_list=[1,"1","one",4.567,{1:"one"}]
result=list(filter(lambda x: isinstance(x, str) == True, some_list))
print(result)
