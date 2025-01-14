def merge_sort(unsorted_arr):
    arr_len = len(unsorted_arr)
    if arr_len <= 1:
        return unsorted_arr
    m1 = merge_sort(unsorted_arr[0: arr_len // 2])
    m2 = merge_sort(unsorted_arr[arr_len // 2:])
    sorted_arr = []
    while m1 and m2:
        if m1[0] < m2[0]:
            sorted_arr.append(m1.pop(0))
        else:
            sorted_arr.append(m2.pop(0))
    if m1:
        sorted_arr.extend(m1)
    if m2:
        sorted_arr.extend(m2)
    return sorted_arr



if __name__ == "__main__":
    print(merge_sort([2,7,11,15]))
    print(merge_sort([2, 7, 11, 15, 0]))
