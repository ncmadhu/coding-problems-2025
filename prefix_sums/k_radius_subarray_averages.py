# Input: nums = [7,4,3,9,1,8,5,2,6], k = 3
# Output: [-1,-1,-1,5,4,4,-1,-1,-1]
# Explanation:
# - avg[0], avg[1], and avg[2] are -1 because there are less than k elements before each index.
# - The sum of the subarray centered at index 3 with radius 3 is: 7 + 4 + 3 + 9 + 1 + 8 + 5 = 37.
#   Using integer division, avg[3] = 37 / 7 = 5.
# - For the subarray centered at index 4, avg[4] = (4 + 3 + 9 + 1 + 8 + 5 + 2) / 7 = 4.
# - For the subarray centered at index 5, avg[5] = (3 + 9 + 1 + 8 + 5 + 2 + 6) / 7 = 4.
# - avg[6], avg[7], and avg[8] are -1 because there are less than k elements after each index.

def k_radius_subarray_averages(nums, k):
    # Variation of average of sub arrays length 2k + 1
    curr_sum = 0
    arr_len = len(nums)
    window_size = 2*k + 1
    # # Initialize the averages array with -1
    averages = [-1] * arr_len

    # array should have spaces at both the end, hence window size cannot be greater than given array
    if k > window_size:
        return averages
    for i in range(window_size):
        curr_sum += nums[i]

    averages[k] = curr_sum // window_size
    for right in range(window_size, arr_len):
        curr_sum += nums[right] - nums[right - window_size]
        averages[right-k] = curr_sum // window_size
    return averages





if __name__ == "__main__":
    print(k_radius_subarray_averages([7,4,3,9,1,8,5,2,6],3))
