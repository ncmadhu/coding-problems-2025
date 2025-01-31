# Given a string s, find the length of the longest substring without repeating characters.
#
# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
#
# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
#
# Example 3:
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
import collections
from collections import defaultdict


# Sliding window pattern
# use hashmap to keep track of seen characters
# constraint is in the current window, there should not be repeating characters
# count the length of current window and compare it with the largest
def problem_to_solve(str):
    seen_ch_count = defaultdict(int)
    left = right = 0
    max_length = 0
    while right < len(str):
        seen_ch_count[str[right]] += 1
        while seen_ch_count[str[right]] > 1:
            seen_ch_count[str[left]] -= 1
            left += 1
        max_length = max(max_length, right-left+1)
        right += 1
    return max_length




if __name__ == "__main__":
    print(problem_to_solve("tmmzuxt"))
    print(problem_to_solve("pwwkew"))
    print(problem_to_solve("bbbb"))
    print(problem_to_solve("abcabcbb"))
