# Example 1:
#
# Input
# arr = [1, 2, 3, [4, 5, 6], [7, 8, [9, 10, 11], 12], [13, 14, 15]]
# n = 0
# Output
# [1, 2, 3, [4, 5, 6], [7, 8, [9, 10, 11], 12], [13, 14, 15]]
#
# Explanation
# Passing a depth of n=0 will always result in the original array. This is because the smallest possible depth of a
# subarray (0) is not less than n=0. Thus, no subarray should be flattened.
# Example 2:
#
# Input
# arr = [1, 2, 3, [4, 5, 6], [7, 8, [9, 10, 11], 12], [13, 14, 15]]
# n = 1
# Output
# [1, 2, 3, 4, 5, 6, 7, 8, [9, 10, 11], 12, 13, 14, 15]
#
# Explanation
# The subarrays starting with 4, 7, and 13 are all flattened. This is because their depth of 0 is less than 1.
# However [9, 10, 11] remains unflattened because its depth is 1.
# Example 3:
#
# Input
# arr = [[1, 2, 3], [4, 5, 6], [7, 8, [9, 10, 11], 12], [13, 14, 15]]
# n = 2
# Output
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
#
# Explanation
# The maximum depth of any subarray is 1. Thus, all of them are flattened.

def flatten_deeply_nested_array(nums, n):
    if n == 0:
        return nums
    res = []
    for num in nums:
        if isinstance(num, list):
            res.extend(num)
        else:
            res.append(num)
    if len(res) != len(nums):
        return flatten_deeply_nested_array(res, n-1)
    else:
        return nums


if __name__ == "__main__":
    print(flatten_deeply_nested_array([1, 2, 3, [4, 5, 6], [7, 8, [9, 10, 11], 12], [13, 14, 15]], 0))
    print(flatten_deeply_nested_array([1, 2, 3, [4, 5, 6], [7, 8, [9, 10, 11], 12], [13, 14, 15]], 1))
    print(flatten_deeply_nested_array([1, 2, 3, [4, 5, 6], [7, 8, [9, 10, 11], 12], [13, 14, 15]], 2))
    print(flatten_deeply_nested_array([1, 2, 3, [4, 5, 6], [7, 8, [9, 10, 11], 12], [13, 14, 15]], 5))
