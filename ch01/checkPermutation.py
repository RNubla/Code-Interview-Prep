def checkPermutation(s1: str, s2: str):
    s1Dict = {x: x+x for x, in s1}
    s2Dict = {x: x+x for x, in s2}
    print(s1Dict)
    print(s2Dict)
    for x in s1Dict.keys():
        if x not in s2Dict:
            print('Not a permuation')
        else:
            print("Is a permutation")


if __name__ == '__main__':
    s1 = "abc"
    s2 = 'baa'
    checkPermutation(s1, s2)
