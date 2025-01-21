# Input: nums = [-3,2,-3,4,2]
# Output: 5
# Explanation: If you choose startValue = 4, in the third iteration your step by step sum is less than 1.
# step by step sum
# startValue = 4 | startValue = 5 | nums
#   (4 -3 ) = 1  | (5 -3 ) = 2    |  -3
#   (1 +2 ) = 3  | (2 +2 ) = 4    |   2
#   (3 -3 ) = 0  | (4 -3 ) = 1    |  -3
#   (0 +4 ) = 4  | (1 +4 ) = 5    |   4
#   (4 +2 ) = 6  | (5 +2 ) = 7    |   2

def min_step_by_step_positive(nums):
    # Find the lowest sum we will reach in the array at each  index
    # Then flip it and add one to become positive
    start_value = 0
    sum = 0
    for n in nums:
        sum += n
        start_value = min(start_value, sum)
    return -start_value + 1


if __name__ == "__main__":
    print(min_step_by_step_positive([-3,2,-3,4,2]))
