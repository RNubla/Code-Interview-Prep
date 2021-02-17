def median(arr1: list, arr2: list):
    midPointIndex1 = len(arr1) // 2
    midPointIndex2 = len(arr2) // 2

    result = (arr1[midPointIndex1] + arr2[midPointIndex2]) / 2
    print(result)


if __name__ == '__main__':
    arr1 = [1, 3, 5, 8]
    arr2 = [2, 4, 6, 9]
    median(arr1=arr1, arr2=arr2)
