# Given a square matrix, calculate the absolute difference between the sums of its diagonals.
#
# For example, the square matrix  is shown below:
#
# 1 2 3
# 4 5 6
# 9 8 9
# The left-to-right diagonal = 1 + 5 + 9 The right to left diagonal = 3 + 5 + 9 Their absolute difference is |15 -17|

# For every iteration decrease the j alone
# it moves the position diagonally

def diagonal_difference(arr):
    j = len(arr) - 1
    l_diagonal_sum = r_diagonal_sum = 0
    for i in range(len(arr)):
        l_diagonal_sum += arr[i][i]
        r_diagonal_sum += arr[i][j]
        j -= 1
    return abs(l_diagonal_sum - r_diagonal_sum)


if __name__ == "__main__":
    print(diagonal_difference([[1,2,3], [4,5,6], [9,8,9]]))
