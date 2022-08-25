# array of distinct integer value
# target sum is given
# find whether pair of number is target sum


# O(n^2)
def IsPairTargetSum(arr, sum):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[j] == sum - arr[i]:
                print(arr[j], arr[i])
                return True

    return False


# O(n)
def IsPairtTargetSumV2(arr, sum):
    setArr = set()
    for i in range(len(arr)):
        if sum - arr[i] in setArr:
            return True
        else:
            setArr.add(arr[i])

    return False


# O(n log n)
def IsPairtTargetSumV3(arr, sum):
    arr.sort()

    start = 0
    end = len(arr)-1

    while start < end:
        temp = arr[start] + arr[end]
        if temp == sum:
            return True
        elif temp < sum:
            start += 1
        else:
            end -= 1

    return False


if __name__ == '__main__':
    arr = [5, 9, 11, -3, 4, 6]
    print(IsPairTargetSum(arr, 113))
    print(IsPairtTargetSumV2(arr, 11))
    print(IsPairtTargetSumV3(arr, 112))
