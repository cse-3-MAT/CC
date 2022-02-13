def maxArr(arr, l, m, h):
    sm = 0
    left_sum = 0
    for i in range(m, l - 1, -1):
        sm = sm + arr[i]

        if (sm > left_sum):
            left_sum = sm

    sm = 0
    right_sum = 0
    for i in range(m + 1, h + 1):
        sm = sm + arr[i]

        if (sm > right_sum):
            right_sum = sm

    return max(left_sum + right_sum, left_sum, right_sum)

def maxSub(arr, l, h):

    if (l == h):
        return arr[l]
    m = (l + h) // 2
    return max(maxSub(arr, l, m),
               maxSub(arr, m + 1, h),
               maxArr(arr, l, m, h))


arr = list(map(int,input().split()))
n = len(arr)

max_sum = maxSub(arr, 0, n - 1)
print("Maximum contiguous sum is ", max_sum)
