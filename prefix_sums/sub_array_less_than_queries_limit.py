# Example 1: Given an integer array nums, an array queries where queries[i] = [x, y] and
# an integer limit, return a boolean array that represents the answer to each query.
# A query is true if the sum of the subarray from x to y is less than limit, or false otherwise.
# For example, given nums = [1, 6, 3, 2, 7, 2], queries = [[0, 3], [2, 5], [2, 4]], and limit = 13,
# the answer is [true, false, true]. For each query, the subarray sums are [12, 14, 12].

def subarray_queries_less_than_limit(nums, queries, limit):
    arr_len = len(nums)
    query_result = []
    prefix_sums = [0] * arr_len
    prefix_sums[0] = nums[0]
    for i in range(1, arr_len):
        prefix_sums[i] = prefix_sums[i-1] + nums[i]

    for x, y in queries:
        sub_array_sum = prefix_sums[y] - prefix_sums[x] + nums[x]
        query_result.append(sub_array_sum < limit)
    return query_result


if __name__ == "__main__":
    print(subarray_queries_less_than_limit([1, 6, 3, 2, 7, 2], [[0, 3], [2, 5], [2, 4]], 13))
