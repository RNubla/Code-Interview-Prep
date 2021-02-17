arr = [64, 25, 12, 22, 11]

for x in range(len(arr)):
    min_val_idx = x
    for y in range(x+1, len(arr)):
        if arr[min_val_idx] > arr[y]:
            min_val_idx = y

    arr[x], arr[min_val_idx] = arr[min_val_idx], arr[x]

for i in range(len(arr)):
    print(f'{arr[i]}')
