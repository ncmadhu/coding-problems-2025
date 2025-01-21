# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
#
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"

# Example 1:
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
#
# Example 2:
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
# P     I    N
# A   L S  I G
# Y A   H R
# P     I
#
# Example 3:
# Input: s = "A", numRows = 1
# Output: "A"

# Initialize an n * n matrix
# iterate over each character in the string
# start from 0 th row and step as 1
# when either boundary is reached flip the step
# merge the rows and return the merged string


def zig_zag_conversion(s, rows):
    zig_zag_rows = [[] for _ in range(rows)]
    step = 1
    curr_row = 0
    for ch in s:
        zig_zag_rows[curr_row].append(ch)
        curr_row += step
        if curr_row == 0 or curr_row == rows-1:
            step = -step

    merged = []
    for row in zig_zag_rows:
        merged.extend(row)
    return "".join(merged)


if __name__ == "__main__":
    print(zig_zag_conversion("PAYPALISHIRING", 3))
    print(zig_zag_conversion("PAYPALISHIRING", 4))
