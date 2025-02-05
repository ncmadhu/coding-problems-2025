# Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of
# the string.
#
# If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to
# k characters, then reverse the first k characters and leave the other as original.
#
# Example 1:
#
# Input: s = "abcdefg", k = 2
# Output: "bacdfeg"
# Example 2:
#
# Input: s = "abcd", k = 2
# Output: "bacd"

def test_function(s, k):
    n = len(s)
    s_list = list(s)
    left = 0
    while left < n:
        if left + 2 * k < n or left + k < n:
            reverse_str(s_list, left, left+k)
        else:
            reverse_str(s_list, left, n)
        left = left + 2 * k
    return "".join(s_list)

def reverse_str(s, l, r):
    mid = (l + r) // 2
    while l < mid:
        s[l], s[r-1] = s[r-1], s[l]
        l += 1
        r -= 1


if __name__ == "__main__":
    # print(test_function("abcdefg", 2))
    # print(test_function("abcd", 2))
    print(test_function("abcdefgh", 3))
