# Given an array of positive integers nums and an integer k, return the number of subarrays where the sum of
# all the elements in the subarray is strictly less than k.
# For example, given the input nums = [10, 5, 2, 6], k = 16, the answer is 8.
# The sub arrays with products less than k are:
# [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]

def subarray_sum_less_than_k(nums, k):
    left = subarray_count = 0
    sum = 0
    for right in range(len(nums)):
        sum += nums[right]
        while sum >= k:
            sum -= nums[left]
            left += 1
        subarray_count += right - left + 1
    return subarray_count


if __name__ == "__main__":
    print(subarray_sum_less_than_k([10, 5, 2, 6], 16))
