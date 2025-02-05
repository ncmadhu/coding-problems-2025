# You are given an array of integers nums, there is a sliding window of size k which is moving from the very
# left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window
# moves right by one position. Return the max sliding window.
#
# Example 1:
#
# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation:
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
# Example 2:
#
# Input: nums = [1], k = 1
# Output: [1]
import collections


def naive_solution(nums, k):
    ans = []
    for i in range(len(nums)- k + 1):
        max_element =  nums[i]
        for j in range(i+1, i+k):
            if nums[j] > max_element:
                max_element = nums[j]
        ans.append(max_element)
    return ans

def sliding_window_maximum(nums, k):
    # It provides option to add and remove from both the ends
    # used when we need to maintain a fixed buffer of recent items
    queue = collections.deque()
    ans = []
    # Iterate the elements
    for i in range(len(nums)):
        # We need to maintain monotonically decreasing property of the queue
        # queue holds first max, second max ..
        # If the current element is greater than the last element in queue
        # it Violates the monotonic stack property
        # Hence we remove all the elements which are violating this from the queue
        while queue and nums[queue[-1]] < nums[i]:
            # pops from the right end
            queue.pop()
        queue.append(i)
        # check the element at the front of the queue is still in the window
        if queue[0] + k == i:
            queue.popleft()

        # Wait to add to the answer until we pass the window size
        if i + 1 >= k:
            ans.append(nums[queue[0]])
    return ans


def replay(nums, k):
    ans = []
    monotonic_q = collections.deque() # allows operation on both the ends
    for i in range(len(nums)):
        while monotonic_q and nums[monotonic_q[-1]] < nums[i]: # we maintain a monotonic decreasing queue
            monotonic_q.pop()
        monotonic_q.append(i)
        if monotonic_q[0] + k == i:
            monotonic_q.popleft()
        if i + 1 >= k:
            ans.append(nums[monotonic_q[0]])
    return ans


if __name__ == "__main__":
    print(naive_solution([1,3,-1,-3,5,3,6,7], 3))
    print(sliding_window_maximum([1, 3, -1, -3, 5, 3, 6, 7], 3))
    print(replay([1, 3, -1, -3, 5, 3, 6, 7], 3))
