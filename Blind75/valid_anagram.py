# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true
#
# Example 2:
# Input: s = "rat", t = "car"
# Output: false
import collections


# solution
# have a counter map for each character
# add the counter for occurrence in one of the string
# decrease the counter for occurrence in the other string
def valid_anagram(s, t):
    if len(s) != len(t):
        return False
    char_counter = collections.defaultdict(int)
    for i in range(len(s)):
        char_counter[s[i]] += 1
        char_counter[t[i]] -= 1
    for count in char_counter.values():
         if count > 0:
             return False
    return True


def replay(s, t):
    if len(s) != len(t):
        return False
    ch_counter = collections.defaultdict(int)

    for i in range(len(s)):
        ch_counter[s[i]] += 1
        ch_counter[t[i]] -= 1

    for value in ch_counter.values():
        if value != 0:
            return False
    return True


if __name__ == "__main__":
    print(valid_anagram("anagram", t="nagaram"))
    print(valid_anagram("rat", t="car"))
    print(replay("anagram", t="nagaram"))
    print(replay("rat", t="car"))
