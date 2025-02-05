# Example 1:
#
# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
# Example 2:
#
# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]
# Explanation: The arrays we are merging are [1] and [].
# The result of the merge is [1].
# Example 3:
#
# Input: nums1 = [0], m = 0, nums2 = [1], n = 1
# Output: [1]
# Explanation: The arrays we are merging are [] and [1].
# The result of the merge is [1].
# Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.

def merge_sorted_array_without_using_extra_space(nums1, m, nums2, n):
    p1 = m -1
    p2 = n - 1

    for p in range(m + n -1, -1, -1):
        if p2 < 0:
            return nums1
        if p1 >= 0 and nums1[p1] >= nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
    return nums1

def retry(nums1, m, nums2, n):
    p1 = m - 1
    p2 = n - 1
    for p in range(m+n-1, -1, -1):
        if p2 < 0:
            return nums1
        if p1 >= 0 and nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
    return nums1

if __name__ == "__main__":
    # print(merge_sorted_array_without_using_extra_space( [1,2,3,0,0,0], 3, [2,5,6], 3))
    # print(merge_sorted_array_without_using_extra_space([4,0,0,0,0,0], 1, [1,2,3,5,6], 5))
    # print(merge_sorted_array_without_using_extra_space([1,2,4,5,6,0], 5, [3], 1))
    # print(retry( [1,2,3,0,0,0], 3, [2,5,6], 3))
    print(retry([4,0,0,0,0,0], 1, [1,2,3,5,6], 5))
    # print(retry([1,2,4,5,6,0], 5, [3], 1))
