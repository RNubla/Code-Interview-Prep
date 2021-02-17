a = [2, 7, 11, 15]
# a = [3,2,4]
# a = [3, 3]
# a = [3, 2, 3]
# target = 6
target = 9

dic = {}
for x in range(len(a)):
    num = target - a[x]
    if num in dic.keys():
        print([x, dic[num]])
    dic[a[x]] = x
    print(dic)
    # print([x,dic[num]])
print(dic)
