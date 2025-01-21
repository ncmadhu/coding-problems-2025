# Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
# Output: 10
# Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

def max_consecutive_ones(nums, k):
    left = zero_count = max_ones = 0
    for right in range(len(nums)):
        if nums[right] == 0:
            zero_count += 1
        while zero_count > k:
            if nums[left] == 0:
                zero_count -= 1
            left += 1
        max_ones = max(max_ones, right - left + 1)
    return max_ones




if __name__ == "__main__":
    print(max_consecutive_ones([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))
