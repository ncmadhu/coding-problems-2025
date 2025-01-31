# Example
# Given, s = "axxb??".
# The two question marks can be replaced with the characters 'a' and 'b' respectively to form a string s =
# "axxbab". The string can be rearranged to "abxxba" which is the lexicographically smallest palindrome
# possible by interpolating the string.
# Function Description
# Complete the function getSmallestPalindrome in the editor below.
# getSmallestPalindrome has the following parameter:
# string s: a string
# Returns
# string: the lexicographically smallest palindrome possible or -1
# Constraints
# 1 ≤ |s| ≤ 10
# String s contains only lowercase English letters and '?'s
#
# Sample Input For Custom Testing
# STDIN FUNCTION
# ----- --------
# yh??tx → s = "yh??tx"
# Sample Output
# -1
# Explanation
# It is not possible to replace '?'s in such a way that the string can be rearranged to form a palindrome.
# 1. Get the string length
# 2. The idea is to replace question marks with the odd count characters in the string
# 3. Because for palindrome, except one character everything else should be of even count in odd length string
# 4. In even length string, all characters should be of even count to be a palindrome
# 5. calculate the count of each character and total odd characters count in the string
# 6. If question marks count is less than odd count, we cannot attain palindrome by substituting them with odd character
# 7. Increase the character count of each odd character by one until odd count becomes zero
# 8. start building the palindrome string by adding each character by half count
# 9. take a copy of the reverse of this string
# 10. If the length of the original string was odd add 'a' as padding character in the middle between new_string
#     and its reverse or just return the new_string + reverse_string
import string
from collections import defaultdict


def problem_to_solve(s):
    n = len(s)
    ch_count = {}
    for c in string.ascii_lowercase:
        ch_count[c] = s.count(c)
    q_count = s.count('?')
    odd_ch_count = 0
    for ch, count in ch_count.items():
        if count % 2:
            odd_ch_count += 1
    if odd_ch_count > 0:
        odd_ch_count -= n % 2
    if q_count < odd_ch_count:
        return -1
    extra_q = q_count - odd_ch_count
    for ch, count in ch_count.items():
        if odd_ch_count > 0 and count % 2:
            ch_count[ch] += 1
            odd_ch_count -= 1
    ch_count['a'] += extra_q
    pad_character = 'a'
    new_str = ''
    for ch, count in ch_count.items():
        new_str += ch * (count // 2)
        if count % 2:
            pad_character = ch
    palindrome = new_str + pad_character + new_str[::-1] if n % 2 else new_str + new_str[::-1]
    return palindrome 


if __name__ == "__main__":
    print(problem_to_solve("axxb??"))
    print(problem_to_solve("axxdb??"))
    # print(alternate_solution("axxb??"))
