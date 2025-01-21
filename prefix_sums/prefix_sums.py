def prefix_sums_arr(nums):
    arr_len = len(nums)
    prefix_sums = [0] * arr_len
    prefix_sums[0] = nums[0]
    for i in range(1,arr_len):
        prefix_sums[i] = prefix_sums[i-1] + nums[i]
    return prefix_sums


if __name__ == "__main__":
    print(prefix_sums_arr([5, 2, 1, 6, 3, 8]))
