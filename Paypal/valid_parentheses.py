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
    parentheses_map = {']': '[', '}': '{', ')': '('}
    for ch in parentheses:
        if ch in parentheses_map:
            top_element = stack.pop() if stack else '#'
            if parentheses_map[ch] != top_element:
                return False
        else:
            stack.append(ch)
    return not stack



if __name__ == "__main__":
    print(valid_parentheses("()"))
    print(valid_parentheses("()[]{}"))
    print(valid_parentheses("([{}])"))
    print(valid_parentheses("([{]()"))
    print(valid_parentheses("[{]()"))
