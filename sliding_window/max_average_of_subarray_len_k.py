# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75
def max_average_subarray_of_len_k(arr, k):
    curr_sum = 0
    for i in range(k):
        curr_sum += arr[i]
    max_average = curr_sum / k
    for right in range(k, len(arr)):
        curr_sum += arr[right] - arr[right-k]
        max_average = max(max_average, curr_sum / k)
    return max_average


if __name__ == "__main__":
    print(max_average_subarray_of_len_k([1,12,-5,-6,50,3], 4))
