# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and
# j != k, and nums[i] + nums[j] + nums[k] == 0.
#
# Notice that the solution set must not contain duplicate triplets.

# Example 1:
#
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation:
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
# Example 2:
#
# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
# Example 3:
#
# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.

# solution algorithm
# Sort the elements in the array
# Iterate over each element in the array
# If the current element is greater than zero , break the loop since the array is sorted, the next elements will
# not add to zero
# If the successive elements are not of same value, use two sum to find the next two possible elements


def three_sum(nums):
    nums.sort()
    res = []
    for i in range(len(nums)):
        if nums[i] > 0:
            break
        if i == 0 or nums[i] != nums[i-1]:
            two_sum(nums, i, res)
    return res

def two_sum(nums, i, res):
    j = i + 1
    seen = {}
    while j < len(nums):
        complement = -nums[i] - nums[j]
        if complement in seen:
            res.append([nums[i], nums[j], complement])
            while j + 1 < len(nums) and nums[j+1] == nums[j]:
                j += 1
        seen[nums[j]] = j
        j += 1



if __name__ == "__main__":
    # print(three_sum([-1,0,1,2,-1,-4]))
    print(three_sum([0,0,0,0]))
