# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.
# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

def running_sum_of_array(nums):
    running_sum = [nums[0]]
    for i in range(1, len(nums)):
        running_sum.append(nums[i] + running_sum[-1])
    return running_sum



if __name__ == "__main__":
    print(running_sum_of_array([1,2,3,4]))
