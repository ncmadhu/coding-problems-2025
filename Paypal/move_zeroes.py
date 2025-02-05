# Example 1:
#
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:
#
# Input: nums = [0]
# Output: [0]

def move_zeroes(nums):
    left = right = 0
    while right < len(nums):
        while right < len(nums) and nums[right] == 0:
            right += 1
        if right < len(nums):
            nums[left] = nums[right]
            left += 1
        right += 1

    while left < len(nums):
        nums[left] = 0
        left += 1
    return nums


def replay(nums):
    left = right = 0
    while right < len(nums):
        while right < len(nums) and nums[right] == 0:
            right += 1
        if right < len(nums):
            nums[left] = nums[right]
            left += 1
            right += 1
    while left < len(nums):
        nums[left] = 0
        left += 1
    return nums


if __name__ == "__main__":
    print(move_zeroes([0,1,0,3,12]))
    print(replay([0, 1, 0, 3, 12]))
