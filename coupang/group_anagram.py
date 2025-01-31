# Given an array of strings strs, group the anagrams together. You can return the answer in any order.
# Example 1:
#
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
#
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
#
# Explanation:
#
# There is no string in strs that can be rearranged to form "bat".
# The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
# The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
# Example 2:
#
# Input: strs = [""]
#
# Output: [[""]]
#
# Example 3:
#
# Input: strs = ["a"]
#
# Output: [["a"]]
from collections import defaultdict


def problem_to_solve(strs):
    anagrams_group = defaultdict(list)
    for str in strs:
        key = [0] * 26
        for c in str:
            key[ord(c) - ord('a')] += 1
        anagrams_group[tuple(key)].append(str)
    return [value for value in anagrams_group.values()]



if __name__ == "__main__":
    print(problem_to_solve(["eat","tea","tan","ate","nat","bat"]))
