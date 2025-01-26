# Given an integer array nums, return the length of the longest strictly increasing
# subsequence
#
# Example 1:
#
# Input: nums = [10,9,2,5,3,7,101,18]
# Output: 4
# Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
#
# Example 2:
#
# Input: nums = [0,1,0,3,2,3]
# Output: 4
#
# Example 3:
#
# Input: nums = [7,7,7,7,7,7,7]
# Output: 1

# 1. A subsequence is not need to be consecutive elements, that is substring or subarray
# 2. Use dynamic programming because each selection can affect the count
# 3. At each index we need to check possibility of elements lesser than it occurs before and by selecting it how many
#    elements lesser than that selected element occurs to satisfy the condition
# 4. Use memoization to reduce time


def problem_to_solve(nums):
    memoization = {}
    def dp(i):
        count = 1 # base case where this the only element and no element lesser than this occurs before
        # try branching out from all elements lesser than the current element and calculate the count
        for j in range(i):
            if nums[j] < nums[i]:
                memoization[j] = dp(j)
                count = max(memoization[j] + 1, count)
        return count
    return max(dp(i) for i in range(len(nums)))


if __name__ == "__main__":
    print(problem_to_solve([10,9,2,5,3,7,101,18]))
    print(problem_to_solve([0,1,0,3,2,3]))
    print(problem_to_solve([7,7,7,7,7,7,7]))
