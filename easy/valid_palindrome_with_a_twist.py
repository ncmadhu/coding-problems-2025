# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
#
# Given a string s, return true if it is a palindrome, or false otherwise.
#
# Example 1:
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
#
# Example 2:
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
#
# Example 3:
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric characters.
# Since an empty string reads the same forward and backward, it is a palindrome.

def valid_palindrome_with_a_twist(string):
    left = 0
    right = len(string) - 1
    while left < right:
        while left < right  and not string[left].isalnum():
            left += 1
        while right > left and not string[right].isalnum():
            right -= 1
        if string[left].lower() != string[right].lower():
            return False
        left += 1
        right -= 1
    return True


if __name__ == "__main__":
    print(valid_palindrome_with_a_twist("A man, a plan, a canal: Panama"))
    print(valid_palindrome_with_a_twist(" "))
    print(valid_palindrome_with_a_twist("race a car"))
