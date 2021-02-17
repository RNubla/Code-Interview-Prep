arr = [64, 25, 12, 22, 11]
# arr = [11, 12, 22, 25, 64]

for x in range(len(arr)):
    for y in range(x+1, len(arr)):
        if arr[x] > arr[y]:
            arr[x], arr[y] = arr[y], arr[x]
for x in range(len(arr)):
    print(f'{arr[x]}')
