# Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous)
# subarray of arr. Since the answer may be large, return the answer modulo 10^9 + 7.
#
# Example 1:
#
# Input: arr = [3,1,2,4]
# Output: 17
# Explanation:
# Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4].
# Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
# Sum is 17.
# Example 2:
#
# Input: arr = [11,81,94,43,3]
# Output: 444

def sum_of_subarray_minimums_naive(nums):
    res = 0
    for i in range(len(nums)):
        min_element = nums[i]
        for j in range(i, len(nums)):
            min_element = min(min_element, nums[j])
            res += res + min_element * (j - i + 1)
    return res % (pow(10, 9) + 7)


if __name__ == "__main__":
    print(sum_of_subarray_minimums_naive([3,1,2,4]))
