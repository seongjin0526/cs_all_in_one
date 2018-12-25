list1 = range(1,10+1)
list2 = ['one', 'two','three','four','five','six','seven','eight','nine','ten']
dict1 = {}
for i,j in zip(list1,list2):
    dict1[i] = j
print(dict1)
