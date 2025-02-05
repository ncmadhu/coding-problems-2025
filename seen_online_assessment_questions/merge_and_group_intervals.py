# a list of range contains the start and end values continuous range of integers. given the list of ranges,
# find the number of ways to distribute these ranges into two groups that satisfy the constraint of each group has
# at least one range.
#
# Example 1:
# ranges = [[1,5], [3,8],[10,15], [13,14], [20,100]]
# Groups:
#         Group 1                             Group 2
#     [1,5], [3,8]                      [10,15], [13,14], [20,100]
#     [10,15], [13,14], [20,100]        [1,5], [3,8]
#     [10,15], [13,14]                  [1,5], [3,8], [20,100]
#     [1,5], [3,8], [20,100]            [10,15], [13,14]
#     [20,100]                          [1,5], [3,8], [10,15], [13,14]
#     [1,5], [3,8], [10,15], [13,14]    [20,100]




def test_function(ranges):
    merged = []
    prev = ranges[0]
    for i in range(1, len(ranges)):
        if prev[1] > ranges[i][0]:
            prev[1] = ranges[i][1]
        else:
            merged.append(prev)
            prev = ranges[i]
    merged.append(prev)
    # to calculate the possible two group combinations the formula is 2 ** n - 2
    # we subtract 2 because there cannot be an empty group
    return 2 ** len(merged) - 2


if __name__ == "__main__":
    print(test_function([[1,5], [3,8],[10,15], [13,14], [20,100]]))
