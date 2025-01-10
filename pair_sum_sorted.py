# Given an array of integers sorted in ascending order and a target value, return the indexes of any pair of numbers in
# the array that sum to the target. The order of the indexes in the result
# doesn't matter. If no pair is found, return an empty array.
# Input: nums = [-5, -2, 3, 4, 6], target = 7
# Output: [2, 3]

def pair_sum_sorted(nums, target):
    length = len(nums)
    for i in range(length - 1):
        for j in range(i+1,length):
            if nums[i] + nums[j] == target:
                print(i,j)
                return [i,j]

if __name__ == "__main__":
    print(pair_sum_sorted([-5,-2,3,4,6], 7))