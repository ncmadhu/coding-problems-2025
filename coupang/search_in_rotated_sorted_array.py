# There is an integer array nums sorted in ascending order (with distinct values).
#
# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length)
# such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
# For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
#
# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums,
# or -1 if it is not in nums.
#
# You must write an algorithm with O(log n) runtime complexity.

# Example 1:
#
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:
#
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# Example 3:
#
# Input: nums = [1], target = 0
# Output: -1

def binary_search(nums, start, end, target):
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return -1

def test_function(nums, target):
    n = len(nums)
    left = 0
    right = n - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] > nums[-1]:
            left = mid + 1
        else:
            right = mid - 1
    if target > nums[-1]:
        return binary_search(nums, 0, left -1, target)
    else:
        return binary_search(nums, left, n-1, target)


def one_binary_search(nums, target):
    n = len(nums)
    left  = 0
    right = n - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1


if __name__ == "__main__":
    print(test_function([4,5,6,7,0,1,2], 0))
    print(test_function([4, 5, 6, 7, 0, 1, 2], 3))
    print(one_binary_search([4, 5, 6, 7, 0, 1, 2], 0))
    print(one_binary_search([4, 5, 6, 7, 0, 1, 2], 3))
