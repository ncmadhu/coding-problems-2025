# Example 1:
# Input: s = "()"
# Output: true
#
# Example 2:
# Input: s = "()[]{}"
# Output: true
#
# Example 3:
# Input: s = "(]"
# Output: false
#
# Example 4:
# Input: s = "([])"
# Output: true

def valid_parentheses(parentheses):
    if len(parentheses) <= 1:
        return False
    stack = []
    for ch in parentheses:
        if ch == '}' and stack and stack[-1] == '{':
            stack.pop(-1)
        elif ch == ']' and stack and stack[-1] == '[':
            stack.pop(-1)
        elif ch == ')' and stack and stack[-1] == '(':
            stack.pop(-1)
        else:
            stack.append(ch)
    return not stack


if __name__ == "__main__":
    print(valid_parentheses("()"))
    print(valid_parentheses("()[]{}"))
    print(valid_parentheses("([{}])"))
    print(valid_parentheses("([{]()"))
    print(valid_parentheses("[{]()"))
