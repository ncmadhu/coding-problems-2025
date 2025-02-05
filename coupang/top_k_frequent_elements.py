# Given an integer array nums and an integer k, return the k most frequent elements.
# You may return the answer in any order.
import collections
import heapq
import random


# Example 1:
#
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:
#
# Input: nums = [1], k = 1
# Output: [1]

def test_function(nums, k):
    counter = collections.defaultdict(int)
    for n in nums:
        counter[n] += 1
    freq_list = []
    for n, count in counter.items():
        freq_list.append([count, n])
    freq_list.sort(reverse=True)
    result = []
    for i in range(k):
        result.append(freq_list[i][1])
    return result


def alternate_solution(nums, k):
    if k == len(nums): return nums
    freq_counter = collections.Counter(nums)
    return heapq.nlargest(k, freq_counter.keys(), key=freq_counter.get)


def using_buckets(nums, k):
    if k == len(nums): return nums
    freq_counter = collections.Counter(nums)
    freq_bucket = collections.defaultdict(list)
    for n, count in freq_counter.items():
        freq_bucket[count].append(n)
    result = []
    for i in range(len(nums), 0, -1):
        if i in freq_bucket:
            result.extend(freq_bucket[i])
    return result[:k]


def using_quick_select(nums, k):
    if k == len(nums): return nums
    freq_counter = collections.Counter(nums)
    unique_nums = list(freq_counter.keys())
    def partition(left, right, pivot_index):
        pivot_freq = freq_counter[unique_nums[pivot_index]]
        # swap pivot with right
        unique_nums[pivot_index], unique_nums[right] = unique_nums[right], unique_nums[pivot_index]
        store_index = left
        for i in range(left, right):
            if freq_counter[unique_nums[i]] < pivot_freq:
                unique_nums[i], unique_nums[store_index] = unique_nums[store_index], unique_nums[i]
                store_index += 1
        unique_nums[store_index], unique_nums[right] = unique_nums[right], unique_nums[store_index]
        return store_index


    def quick_select(left, right, k_smallest):
        if left == right:
            return
        pivot_index = random.randint(left, right)
        pivot_index = partition(left, right, pivot_index)
        if k_smallest == pivot_index:
            return
        elif k_smallest < pivot_index:
            quick_select(left, pivot_index-1, k_smallest)
        else:
            quick_select(pivot_index+1, right, k_smallest)

    n = len(unique_nums)
    quick_select(0, n-1, n-k)
    return unique_nums[n-k:]


if __name__ == "__main__":
    print(test_function([1,1,1,2,2,3], 2))
    print(alternate_solution([1, 1, 1, 2, 2, 3], 2))
    print(using_buckets([1, 1, 1, 2, 2, 3], 2))
    print(using_quick_select([1, 1, 1, 2, 2, 3], 2))