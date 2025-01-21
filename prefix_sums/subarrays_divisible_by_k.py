# Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.
# A subarray is a contiguous part of an array.
import collections


# Example 1:
# Input: nums = [4,5,0,-2,-3,1], k = 5
# Output: 7
# Explanation: There are 7 subarrays with a sum divisible by k = 5:
# [4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
#
# Example 2:
# Input: nums = [5], k = 9
# Output: 0

# Instead of prefix sums we are going to track the modulo
# Key property is : elements between i + 1 and j are divisible by K if remainder at i and remainder at j are equal
# Array         : [4,5,0,-2,-3,1]
# Prefix Sum    : [4,9,9,7,4,5]
# Prefix Mod    : [4,4,4,2,4,0]
# Idea is if the sum at i is removed, the remainder will become zero at j
# Possible sub array count divisible by k between, i and j is, how many times the remainder at j occurs between, i and j

def subarrays_divisible_by_k(nums, k):

    subarray_count = 0
    curr_sum = 0
    prefix_remainder_count = collections.defaultdict(int)
    # We initialize with prefix_remainder_count[0] = 1 to statisfy the condition if the first element itself is
    # divisible by K.
    prefix_remainder_count[0] = 1
    for right in range(len(nums)):
        curr_sum += nums[right]
        curr_remainder = curr_sum % k
        if curr_remainder in prefix_remainder_count:
            subarray_count += prefix_remainder_count[curr_remainder]
        prefix_remainder_count[curr_remainder] += 1
    return subarray_count



if __name__ == "__main__":
    print(subarrays_divisible_by_k([4,5,0,-2,-3,1], 5))
    print(subarrays_divisible_by_k([5], 9))
