# Example 1:
import collections


# Input: nums = [1,2,3,1]
#
# Output: true
#
# Explanation:
#
# The element 1 occurs at the indices 0 and 3.
#
# Example 2:
#
# Input: nums = [1,2,3,4]
#
# Output: false
#
# Explanation:
#
# All elements are distinct.
#
# Example 3:
#
# Input: nums = [1,1,1,3,3,4,3,2,4,2]
#
# Output: true


def contains_duplicate(nums):
    seen_values = collections.defaultdict(int)
    for n in nums:
        if n in seen_values:
            return True
        else:
            seen_values[n] += 1
    return False


if __name__ == "__main__":
    print(contains_duplicate([1,1,1,3,3,4,3,2,4,2]))
