# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]
#
# Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

def rotate_image(matrix):
     l, r =  0, len(matrix) - 1
     while l < r:
         for i in range(r - l):
             top, bottom = l, r

             # save top left for now
             top_left = matrix[top][l+i]

             # bottom left to the top left
             matrix[top][l+i] = matrix[bottom-i][l]

             # bottom right to the bottom left
             matrix[bottom-i][l] = matrix[bottom][r-i]

             # top right to bottom right
             matrix[bottom][r-i] = matrix[top+i][r]

             # top left to top right
             matrix[top+i][r] = top_left
         l += 1
         r -= 1
     return matrix


def transpose_reflect(matrix):
    n = len(matrix)

    # transpose --- reflect items on diagonal
    for i in range(n):
        for j in range(i+1, n): # we start from i+1 because diagonal elements occur after that
            # Transpose = changing row to column -- [i][j] = [j][i]
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reflect -- reflect items on horizontally

    for i in range(n):
        for j in range(n // 2):
            matrix[i][j], matrix[i][n-1-j] = matrix[i][n-1-j], matrix[i][j]

    return matrix



if __name__ == "__main__":
    print(rotate_image([[1,2,3],[4,5,6],[7,8,9]]))
    print(transpose_reflect([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))