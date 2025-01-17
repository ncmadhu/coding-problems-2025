# Given an array of positive integers nums and an integer k, find the length of the longest subarray
# whose sum is less than or equal to k.
# nums = [3, 1, 2, 7, 4, 2, 1, 1, 5] and k = 8

def longest_subarray_less_than_k(arr, k):
    left = 0
    arr_len = len(arr)
    max_sub_array_len = 0
    curr = 0
    for right in range(arr_len):
        curr += arr[right]
        while curr > k:
            curr -= arr[left]
            left += 1
        max_sub_array_len = max(max_sub_array_len, right - left + 1)
    return max_sub_array_len


if __name__ == "__main__":
    print(longest_subarray_less_than_k([3, 1, 2, 7, 4, 2, 1, 1, 5], 8))
    print(longest_subarray_less_than_k([3, 1, 2, 7, 4, 1, 1, 1, 1], 8))
    print(longest_subarray_less_than_k([3, 1, 2, 7, 4, 1, 1, 1, 1], 1))