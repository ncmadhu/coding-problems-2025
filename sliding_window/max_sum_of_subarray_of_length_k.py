# Given an integer array nums and an integer k, find the sum of the subarray with the largest sum whose length is k.

def max_sum_of_subarray_of_length_k(arr, k):
    curr_sum = 0
    for i in range(k):
        curr_sum += arr[i]
    max_sum =  curr_sum
    for right in range(k, len(arr)):
        curr_sum += arr[right] - arr[right-k]
        max_sum = max(max_sum, curr_sum)
    return max_sum


if __name__ == "__main__":
    print(max_sum_of_subarray_of_length_k([3, -1, 4, 12, -8, 5, 6], 4))
