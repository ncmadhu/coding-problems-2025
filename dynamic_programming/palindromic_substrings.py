# Given a string s, return the number of palindromic substrings in it.
#
# A string is a palindrome when it reads the same backward as forward.
#
# A substring is a contiguous sequence of characters within the string.
# Example 1:
#
# Input: s = "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
# Example 2:
#
# Input: s = "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

def problem_to_solve(s):
    str_len = len(s)
    dp = [[False] * str_len for _ in range(str_len)]
    count = str_len
    for i in range(str_len):
        dp[i][i] = True
    for i in range(str_len-1):
        if s[i] == s[i+1]:
            dp[i][i+1] = True
            count += 1
    for diff in range(2, str_len):
        for i in range(str_len-diff):
            j = i + diff
            if s[i] == s[j] and dp[i+1][j-1]:
                dp[i][j] = True
                count += 1
    return count


if __name__ == "__main__":
    print(problem_to_solve("abc"))
    print(problem_to_solve("aaa"))
