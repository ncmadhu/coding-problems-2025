# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
#
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
#
# You must solve this problem without using the library's sort function.
#
# Example 1:
#
# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Example 2:
#
# Input: nums = [2,0,1]
# Output: [0,1,2]

# 1. use three pointers to indicate start, middle, end
# 2. increment start and middle for every swap with 0
# 3. decrement end for every swap with 2
# 4. if middle crosses the end return

def sort_colors(nums):
    start = middle = 0
    end = len(nums) - 1
    while middle <= end:
        if nums[middle] == 0:
            nums[start], nums[middle] = nums[middle], nums[start]
            start += 1
        else:
            nums[end], nums[middle] = nums[middle], nums[end]
            end -= 1
            # we do not need to increment middle for right swap, it can put 0 in the middle
            # to compensate default increment below we decrease by 1 here
            middle -= 1
        middle += 1
    return nums

def replay(nums):
    start = middle = 0
    end = len(nums) - 1
    while middle <= end:
        if nums[middle] == 0:
            nums[start], nums[middle] = nums[middle], nums[start]
            start += 1
        elif nums[middle] == 2:
            nums[end], nums[middle] = nums[middle], nums[end]
            end -= 1
            middle -= 1
        middle += 1
    return nums


if __name__ == "__main__":
    print(sort_colors([2,0,2,1,1,0]))
    print(replay([2, 0, 2, 1, 1, 0]))
