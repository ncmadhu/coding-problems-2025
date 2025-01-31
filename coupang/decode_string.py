# Given an encoded string, return its decoded string.
#
# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated
# exactly k times. Note that k is guaranteed to be a positive integer.
#
# You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed,
# etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for
# those repeat numbers, k. For example, there will not be input like 3a or 2[4].
#
# The test cases are generated so that the length of the output will never exceed 105.

# Example 1:
#
# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"
# Example 2:
#
# Input: s = "3[a2[c]]"
# Output: "accaccacc"
# Example 3:
#
# Input: s = "2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"

def problem_to_solve(s):
    stack = []
    result_str = []
    decode_str = ""
    right = 0
    while right < len(s):
        if s[right] == "]":
            while stack and stack[-1] != '[':
                decode_str = stack.pop() + decode_str
            stack.pop()
            result_str.append(decode_str * int(stack.pop()))


        else:
            stack.append(s[right])
        right += 1
    return decode_str


if __name__ == "__main__":
    print(problem_to_solve("3[a2[c]]"))
    print(problem_to_solve("2[abc]3[cd]ef"))
