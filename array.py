def getMaxSumOfArray(arr1: list, arr2: list):
    arr1.sort(reverse=True)
    arr2.sort()
    print(arr1)
    print(arr2)
    result = 0
    for i in range(len(arr1)):
        result += (i+1) * (arr2[i] - arr1[i])
    return result

if __name__ == '__main__':
    print(getMaxSumOfArray([1,2,3],[10,10,10]))