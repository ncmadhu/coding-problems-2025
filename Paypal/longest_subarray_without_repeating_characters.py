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


# Sliding window pattern
# use hashmap to keep track of seen characters
# constraint is in the current window, there should not be repeating characters
# count the length of current window and compare it with the largest


def length_of_longest_substring_without_repeating_character(s):
    left = right = 0
    seen_characters = collections.defaultdict(int)
    largest_substring = 0
    while right < len(s):
        seen_characters[s[right]] += 1
        while seen_characters[s[right]] > 1:
            seen_characters[s[left]] -= 1
            left += 1
        largest_substring = max(largest_substring, right-left+1)
        right += 1
    return largest_substring


if __name__ == "__main__":
    print(length_of_longest_substring_without_repeating_character("tmmzuxt"))
    print(length_of_longest_substring_without_repeating_character("pwwkew"))
    print(length_of_longest_substring_without_repeating_character("bbbb"))
    print(length_of_longest_substring_without_repeating_character("abcabcbb"))
