# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true
#
# Example 2:
# Input: s = "rat", t = "car"
# Output: false
import collections
from collections import defaultdict


def valid_anagram(s, t):
    s_map = collections.defaultdict(int)
    t_map = collections.defaultdict(int)
    if len(s) != len(t):
        return False
    for i in range(len(s)):
        s_map[s[i]] += 1
        t_map[t[i]] += 1

    for key in s_map.keys():
        if key not in t_map or t_map[key] != s_map[key]:
            return False

    return True


def alternate_solution(s, t):
    if len(s) != len(t):
        return False
    c_map = collections.defaultdict(int)
    for i in range(len(s)):
        c_map[s[i]] += 1
        c_map[t[i]] -= 1

    for count in c_map.values():
        if count > 0:
            return False
    return True


def replay(s, t):
    counter = defaultdict(int)
    if len(s) != len(t):
        return False
    for i in range(len(s)):
        counter[s[i]] += 1
        counter[t[i]] -= 1
    for value in counter.values():
        if value != 0:
            return False
    return True


if __name__ == "__main__":
    print(alternate_solution("anagram", t = "nagaram"))
    print(alternate_solution("rat", t="car"))
    print(alternate_solution("aaa", t="bbb"))
    print(replay("anagram", t = "nagaram"))
    print(replay("rat", t="car"))
    print(replay("aaa", t="bbb"))
