# Given an integer array nums, find the number of ways to split the array into two parts so that
# the first section has a sum greater than or equal to the sum of the second section.
# The second section should have at least one number.
# Input: nums = [10,4,-8,7]
# Output: [10,4] [-8,7], [10,4,-8] [7] = 2 splits

def num_ways_to_split_array(nums):
    split_count = 0
    arr_len = len(nums)
    prefix_sums = [nums[0]]
    for i in range(1, arr_len):
        prefix_sums.append(prefix_sums[i-1] + nums[i])
    for i in range(arr_len - 1):
        left = prefix_sums[i]
        right = prefix_sums[-1] - prefix_sums[i]
        if left >= right:
            split_count += 1
    return split_count


def alternate_way(nums):
    # we do not need the prefix array at all
    # we can calculate the left sum on the fly by adding the current element to sum so far
    # for right section we can subtract the current left sum - total sum of the array
    total_sum = sum(nums)
    left = split_count = 0
    for i in range(len(nums) - 1):
        left += nums[i]
        if left >= total_sum - left:
            split_count += 1
    return split_count


if __name__ == "__main__":
    print(num_ways_to_split_array([10,4,-8,7]))
    print(alternate_way([10, 4, -8, 7]))
