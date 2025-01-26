def problem_to_solve(num):
    memo = {}
    def fibonacci(n):
        if n <= 1:
            return n
        if n in memo:
            return memo[n]
        memo[n] = fibonacci(n-1) + fibonacci(n-2)
        return memo[n]
    return fibonacci(num)


def fibonacci_bottom_up(num):
    fib_series = [0, 1]
    if num <= 1:
        return fib_series[num]
    for i in range(2, num+1):
        fib_series.append(fib_series[i-1] + fib_series[i-2])
    return fib_series[num]


if __name__ == "__main__":
    # print(problem_to_solve(0))
    # print(problem_to_solve(1))
    # print(problem_to_solve(2))
    # print(problem_to_solve(3))
    # print(problem_to_solve(4))
    # print(problem_to_solve(5))
    print(fibonacci_bottom_up(5))


