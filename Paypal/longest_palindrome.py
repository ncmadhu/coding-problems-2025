# Example 1:
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
#
# Example 2:
# Input: s = "cbbd"
# Output: "bb"

# Key property 1: s[i] == s[i]
# Key property check for s[i] == s[i+1]
# Then check for all possible substring length  i : (i + 1 to n -1)
# Since we validated the previous shorter substring as  palindrome if outer edges are equal, then the whole substring
# is a palindrome
# Record whether the substring is a palindrome or not using a 2D array


def longest_palindrome(s):
    str_len = len(s)
    # array to store the palindrome state at each possible substring combination
    dp = [[False] * str_len for _ in range(str_len)]
    # Every character is a palindrome, hence we initialize with 0,0
    ans = [0,0]
    for i in range(str_len):
        dp[i][i] = True
    for i in range(str_len-1):
        if s[i] == s[i+1]:
            dp[i][i+1] = True
            ans = [i, i+1]
    # Now we check for all possible substring combinations with a length starting from 3
    for diff in range(2,str_len):
        for i in range(str_len-diff):
            j = i + diff
            if s[i] == s[j] and dp[i+1][j-1]:
                dp[i][j] = True
                ans = [i, j]
    return s[ans[0]:ans[1]+1]




if __name__ == "__main__":
    print(longest_palindrome("babad"))
    print(longest_palindrome("cbbd"))
