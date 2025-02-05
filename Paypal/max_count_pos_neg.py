# Example 1:
#
# Input: nums = [-2,-1,-1,1,2,3]
# Output: 3
# Explanation: There are 3 positive integers and 3 negative integers. The maximum count among them is 3.
# Example 2:
#
# Input: nums = [-3,-2,-1,0,0,1,2]
# Output: 3
# Explanation: There are 2 positive integers and 3 negative integers. The maximum count among them is 3.
# Example 3:
#
# Input: nums = [5,20,66,1314]
# Output: 4
# Explanation: There are 4 positive integers and 0 negative integers. The maximum count among them is 4.

def max_count_pos_neg(nums):
    # To take care of arrays with just zeroes
    pos, neg =  len(nums), -1
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid =  (left + right) // 2
        if nums[mid] < 0:
            neg = mid
            left  = mid + 1
        else:
            right = mid - 1
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] > 0:
            pos = mid
            right = mid - 1
        else:
            left= mid + 1
    return max(neg + 1, len(nums) - pos)




if __name__ == "__main__":
    # print(max_count_pos_neg([-2,-1,-1,1,2,3]))
    # print(max_count_pos_neg([-3,-2,-1,0,0,1,2]))
    # print(max_count_pos_neg([5,20,66,1314]))
    print(max_count_pos_neg([0,0,0,0,0,0,0,0,0,0]))
