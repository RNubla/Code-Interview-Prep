def isUnique(s: str):
    unique = []
    rep = []

    for x in s:
        if x not in unique:
            unique.append(x)
        elif x in unique:
            rep.append(x)
    if len(rep) > 0:
        print('Not unique')
    else:
        print('Is Unique')


if __name__ == "__main__":
    s = 'string'
    isUnique(s)
