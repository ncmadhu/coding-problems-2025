# Given a sorted array of unique integers and a target integer, return true
# if there exists a pair of numbers that sum to target, false otherwise.
# This problem is similar to Two Sum. (In Two Sum, the input is not sorted).
# For example, given nums = [1, 2, 4, 6, 8, 9, 14, 15] and target = 13, return true because 4 + 9 = 13.

def sorted_array_target_sum(arr, target):
    arr_len = len(arr)
    left = 0
    right = arr_len - 1
    while left < right:
        curr_sum = arr[left] + arr[right]
        if  curr_sum > target:
            right -= 1
        elif curr_sum < target:
            left += 1
        else:
            return left, right
    return -1,-1

if __name__ == "__main__":
    print(sorted_array_target_sum([1, 2, 4, 6, 8, 9, 14, 15], target=13))