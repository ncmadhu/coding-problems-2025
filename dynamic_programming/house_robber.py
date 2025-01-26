# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed,
# the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and
# it will automatically contact the police if two adjacent houses were broken into on the same night.
#
# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you
# can rob tonight without alerting the police.

# Example 1:
#
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
#
# Example 2:
#
# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.


# 1. Base case is money at house greater than length is 0
# 2. Max money can be robbed at house i is max of total robbed money until i + 1 house or
#    total robbed money until i + 2 house + money at house i
# 3. Why because we cannot rob from adjacent houses, hence we will not add current house money if we choose the next
#    house


def problem_to_solve(nums):
    memoization = {}
    def rob_from(index, nums):
        if index >= len(nums):
            # There is no money to rob at non-existent house
            return 0

        if index in memoization:
            return memoization[index]

        max_money = max(rob_from(index+1, nums), rob_from(index+2, nums) + nums[index])
        memoization[index] = max_money
        return memoization[index]
    return rob_from(0, nums)

def iterative_approach(nums):
    # Base case
    max_amount = [0] * (len(nums) + 1)
    max_amount[len(nums) - 1] = nums[-1]

    for i in range(len(nums)-2, -1, -1):
        max_amount[i] = max(max_amount[i+1], max_amount[i+2] + nums[i])
    return max_amount[0]


def constant_space(nums):
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]
    t1 = t2  = 0
    for i in range(len(nums)):
        temp = t1
        t1 = max(t1, t2 + nums[i])
        t2 = temp
    return t2


if __name__ == "__main__":
    print(problem_to_solve([2,7,9,3,1]))
    print(iterative_approach([2,1,1,2]))
    print(iterative_approach([2,1,1,2]))