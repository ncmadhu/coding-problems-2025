# Given an array of positive integers nums and an integer k, return the number of subarrays where the product of
# all the elements in the subarray is strictly less than k.
# For example, given the input nums = [10, 5, 2, 6], k = 100, the answer is 8.
# The sub arrays with products less than k are:
# [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]

def subarray_product_less_than_k(arr, k):
    left = sub_array_count = 0
    product = 1
    for right in range(len(arr)):
        product *= arr[right]
        while product >= k:

            product //= arr[left]
            left += 1
        sub_array_count += right - left + 1
    return sub_array_count



if __name__ == "__main__":
    print(subarray_product_less_than_k([10, 5, 2, 6], 100))
