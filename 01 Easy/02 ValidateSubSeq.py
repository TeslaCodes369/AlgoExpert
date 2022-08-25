# Validate Subsequence

# O(n)
def IsSubsequence(arr, subs):
    len1 = len(arr)
    len2 = len(subs)

    if len1 < len2:
        return False

    i = 0
    for j in range(len1):
        if subs[i] == arr[j]:
            i += 1

        if i == len2:
            break

    if i == len2:
        return True

    return False


if __name__ == '__main__':
    arr = [5, 1, 22, 25, 6, -1, 8, 10]
    subs = [11, 6, -1, 8]
    print(IsSubsequence(arr, subs))
    subs = [1, 6, -1, 8]
    print(IsSubsequence(arr, subs))
