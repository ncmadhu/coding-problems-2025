# Given an array of positive integers nums and an integer k, find the length of the longest subarray
# whose sum is less than or equal to k.
# nums = [3, 1, 2, 7, 4, 2, 1, 1, 5] and k = 8
def longest_subarray_less_than_k(arr, k):
    left = 0
    curr = 0
    max_subarray_length = 0
    for right in range(len(arr)):
        curr += arr[right]
        while curr > k:
            curr -= arr[left]
            left += 1
        max_subarray_length = max(max_subarray_length, right - left + 1)
    return max_subarray_length



if __name__ == "__main__":
    print(longest_subarray_less_than_k([3, 1, 2, 7, 4, 2, 1, 1, 5], 8))
    print(longest_subarray_less_than_k([3, 1, 2, 7, 4, 1, 1, 1, 1], 8))
    print(longest_subarray_less_than_k([3, 1, 2, 7, 4, 1, 1, 1, 1], 1))
