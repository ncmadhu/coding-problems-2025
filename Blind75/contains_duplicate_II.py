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


def replay(nums, k):
    # 1. Index position is needed, Hence we cannot use sort
    # 2. Array is not sorted, Hence we cannot use two pointer
    # 3. Since we need to find an element already seen, we can use hash map
    # 4. Iterate the array, add the element to the hashmap if not already present with element has key and index has value
    # 5. If the element is present, check for equality and if equal check the index difference == k
    # 6. If equal to k return true
    seen_elements = {}
    for index, value in enumerate(nums):
        if value in seen_elements and abs(seen_elements[value] - index) + 1 <= k:
            return True
        else:
            seen_elements[value] = index
    return False


if __name__ == "__main__":
    print(replay([99, 99], 2))
    # print(contains_duplicate_ii([1,2,3,1,2,4], 2))
    # print(contains_duplicate_ii([1,2,3,1], 3))
    # print(contains_duplicate_ii([1, 2, 3, 1], 2))

