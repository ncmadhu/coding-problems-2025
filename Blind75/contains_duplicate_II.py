# Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the
# array such that nums[i] == nums[j] and abs(i - j) <= k.

# Example 1:
#
# Input: nums = [1,2,3,1], k = 3
# Output: true
# Example 2:
#
# Input: nums = [1,0,1,1], k = 1
# Output: true
# Example 3:
#
# Input: nums = [1,2,3,1,2,3], k = 2
# Output: false

def contains_duplicate_ii(nums, k):
    index_dict = {}
    for i, v in enumerate(nums):
        if v in index_dict:
            if abs(index_dict[v] - i) <= k:
                return True
        index_dict[v] = i
    return False


if __name__ == "__main__":
    print(contains_duplicate_ii([1,2,3,1,2,3], 2))
    print(contains_duplicate_ii([1,2,3,1], 3))
