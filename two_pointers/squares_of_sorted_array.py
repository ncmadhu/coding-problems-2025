def squares_of_sorted_array(arr):
    arr_len = len(arr)
    left = 0
    right = arr_len - 1
    squared = [0] * arr_len
    for i in range(arr_len - 1, -1, -1):
        if abs(arr[left]) < abs(arr[right]):
            square = arr[right]
            right -= 1
        else:
            square = arr[left]
            left += 1
        squared[i] = square * square
    return squared


if __name__ == "__main__":
    print(squares_of_sorted_array([-4,-1,0,3,10]))
    # print(squares_of_sorted_array([-7,-3,2,3,11]))
