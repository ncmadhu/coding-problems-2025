# Given a string s, return the length of the longest repeating substrings. If no repeating substring exists, return 0
# Example 1:
#
# Input: s = "abcd"
# Output: 0
# Explanation: There is no repeating substring.
# Example 2:
#
# Input: s = "abbaba"
# Output: 2
# Explanation: The longest repeating substrings are "ab" and "ba", each of which occurs twice.
# Example 3:
#
# Input: s = "aabcaabdaab"
# Output: 3
# Explanation: The longest repeating substring is "aab", which occurs 3 times.

def problem_to_solve(s):
    n = len(s)
    substr_set = set()
    max_length = 0
    for j in range(n):
        for i in range(j+1):
            sub_str = s[i:j+1]
            if sub_str not in substr_set:
                substr_set.add(sub_str)
            else:
                max_length = max(max_length, len(sub_str))
    return max_length

def using_binary_search(s):
    n = len(s)
    left = 0
    right = n - 1 # substring needs to be less than the actual string. Hence, we decrease right by 1

    def find_repeating_substring(length):
        seen = set()
        for i in range(n-length+1): # we add 1 to have the right most index also to be inclusive
            sub_str = s[i:i+length]
            h_str = hash(sub_str) # to decrease the space complexity
            if h_str in seen:
                return True
            seen.add(h_str)
        return False

    while left < right:
        # adding 1 to avoid infinite loop in certain conditions.
        # Using left + (right-left) instead of left + right to avoid overflow errors
        mid = left + (right - left + 1) // 2
        # using binary search we are trying to find a repeating substring of max length == mid
        # if there is a repeating substring we try to increase the length by increasing left,
        # which increases mid i.e. length
        if find_repeating_substring(mid):
            left = mid
        else:
            right = mid -1
        # finally right and left will point to the length of the substring
    return left # or right since both will be equal at this point



if __name__ == "__main__":
    print(problem_to_solve("abbaba"))
    print(using_binary_search("abbaba"))
    print(problem_to_solve("aabcaabdaab"))
    print(using_binary_search("aabcaabdaab"))
