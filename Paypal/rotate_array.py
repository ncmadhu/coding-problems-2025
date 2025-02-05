# Example 1:
#
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
# Example 2:
#
# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation:
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]

# 1. Use curr and swap variables
# 2. Use modulo to keep check of index out of range
# 3. Use start to break out of infinite loop


def rotate_array(nums, k):

    swaps = 0
    k =  k % len(nums)
    if k == 0:
        return nums
    for i in range(len(nums)):
        start = i
        prev = nums[i]
        while True:
            next = (i + k) % len(nums)
            curr = nums[next]
            nums[next] = prev
            prev = curr
            swaps += 1
            i = next
            if i == start:
                break
        if swaps == len(nums):
            break
    return nums


def naive_solution(nums, k):
    k %= len(nums)
    for i in range(k):
        previous = nums[-1]
        for j in range(len(nums)):
            nums[j], previous = previous, nums[j]
    return nums


def replay(nums, k):
    if k == 0:
        return nums
    k %= len(nums)
    swaps = 0
    for i in range(len(nums)):
        start = i
        prev = nums[i]
        while True:
            next = (i + k) % len(nums)
            curr = nums[next]
            nums[next] = prev
            prev = curr
            i = next
            swaps += 1
            if i == start:
                break
        if swaps == len(nums):
            break
    return nums





if __name__ == "__main__":
    print(rotate_array([1,2,3,4,5,6,7], 3))
    print(naive_solution([1, 2, 3, 4, 5, 6, 7], 3))
    print(replay([1, 2, 3, 4, 5, 6, 7], 3))