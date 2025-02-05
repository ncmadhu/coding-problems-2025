# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
#
# Example 1:
#
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:
#
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

# 1. Assume first string of the list is the longest
# 2. Iterate for each index position for that string
# 3. Inner loop iterate over each string in the input list
# 4. check whether the index is out of bounds for the current string or character is not equal with the outer string
# 5. If so return the current result
# 6. Once all the strings are tested for the current index position, then upto this index all the strings have common
#    prefix
# 7. Finally return the result

def longest_common_prefix(strs):
    result = ""
    for i in range(len(strs[0])):
        for s in strs:
            if i == len(s) or s[i] != strs[0][i]:
                return result
        result += strs[0][i]
    return result


def replay(strs):
    result = ""
    for i in range(len(strs[0])):
        for s in strs[1:]:
            if i == len(s) or s[i] != strs[0][i]:
                return result
        result += strs[0][i]
    return result


if __name__ == "__main__":
    print(longest_common_prefix(["flower","flow","flight"]))
    print(replay(["flower", "flow", "flight"]))
