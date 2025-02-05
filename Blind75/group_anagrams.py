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
import collections


# Two approaches
# use hash map to track processed strings
# iterate for each string
# sort the string and use that as key for hash map and add the string to the existing list
# Finally return all the lists stored in the hash map

# use the count of the characters as a key for hash map and store the string in the existing list


def group_anagrams_by_sorting(strs):
    str_group = collections.defaultdict(list)
    for s in strs:
        # tuple because list cannot be a dictionary key since it is mutable
        str_group[tuple(sorted(s))].append(s)
    return list(str_group.values())

def group_anagrams_by_count(strs):
    str_group = collections.defaultdict(list)
    for s in strs:
        key_obj = [0] * 26
        for ch in s:
            key_obj[ord(ch) - ord('a')] += 1
        str_group[tuple(key_obj)].append(s)
    return list(str_group.values())



if __name__ == "__main__":
    print(group_anagrams_by_sorting(["eat","tea","tan","ate","nat","bat"]))
    print(group_anagrams_by_count(["eat", "tea", "tan", "ate", "nat", "bat"]))
