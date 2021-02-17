S = "aaab"
a = sorted(sorted(S), key=S.count)  # lovvv
print(a)
h = len(a) // 2
print(h)
print(a[1::2])  # [o,v]
print(a[::2])  # [l,v,v]
print(a[:h])  # [l,o]
print(a[h:])  # [v,v,v]

a[1::2], a[::2] = a[:h], a[h:]
print('new A')
print(a[1::2])
print(a[::2])
print(a)
print(''.join(a) * (a[-1:] != a[-2:-1]))

# a[1::2] = a[:h]
# a[1::2] = [l,o]
# a[::2] = [v,v,v]
