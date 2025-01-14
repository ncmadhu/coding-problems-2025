def minMax(arr, sub_array_len):
    arr_len = len(arr)
    if sub_array_len > arr_len:
        return
    left = 0
    right = sub_array_len - 1
    minSofar = 0
    maxSoFar = 0
    for i in range(sub_array_len):
        minSofar += arr[i]
        maxSoFar += arr[i]
    left += 1
    right += 1
    while right < arr_len:
        currentMin = minSofar - arr[left-1] + arr[right]
        currentMax = maxSoFar - arr[left - 1] + arr[right]
        if currentMin < minSofar:
            minSofar = currentMin
        if currentMax > maxSoFar:
            maxSoFar = currentMax
        left += 1
        right += 1
    return minSofar, maxSoFar


if __name__ == "__main__":
    # print(minMax([1,3,5,7,9], 4))
    print(minMax([7,69,2,221,8974], 4))



