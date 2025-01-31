# Exmaple arr = [-2,2,4]
# possible combos (-2,2) , (-2,4), (2,4)
# abs(-2-2), abs(-2-4), abs(2-4) --- 4,6,2
# answer is 2
def problem_to_solve(arr):
    n = len(arr)
    arr.sort()
    min_difference = float('inf')
    for i in range(n-1):
        min_difference = min(min_difference, abs(arr[i]-arr[i+1]))
    return min_difference


if __name__ == "__main__":
    print(problem_to_solve([3,-7,0]))
    print(problem_to_solve([-59, -36, -13, 1, -53, -92, -2, -96, -54, 75]))
    print(problem_to_solve([1, -3, 71, 68, 1,7]))

