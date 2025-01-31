# You are given a 0-indexed 2D integer array questions where questions[i] = [pointsi, brainpoweri].
#
# The array describes the questions of an exam, where you have to process the questions in order
# (i.e., starting from question 0) and make a decision whether to solve or skip each question.
# Solving question i will earn you pointsi points but you will be unable to solve each of the next
# brainpoweri questions. If you skip question i, you get to make the decision on the next question.
#
# For example, given questions = [[3, 2], [4, 3], [4, 4], [2, 5]]:
#     If question 0 is solved, you will earn 3 points but you will be unable to solve questions 1 and 2.
#     If instead, question 0 is skipped and question 1 is solved, you will earn 4 points but you will be unable to
#     solve questions 2 and 3.
#
# Return the maximum points you can earn for the exam.

# Input: questions = [[3,2],[4,3],[4,4],[2,5]]
# The maximum points can be earned by solving questions 0 and 3.
# Total points earned: 3 + 2 = 5. There is no other way to earn 5 or more points.
#
# Input: questions = [[1,1],[2,2],[3,3],[4,4],[5,5]]
# The maximum points can be earned by solving questions 1 and 4.
# Total points earned: 2 + 5 = 7. There is no other way to earn 7 or more points.


def problem_to_solve(questions):
    n = len(questions)
    dp = [0] * n
    # 1. We solve using top down approach
    # 2. Hence initialize dp[-1] with the point of the last question
    dp[-1] = questions[-1][0]
    # 3. we start the loop from next question to the last
    for i in range(n-2, -1, -1):
        # 4. We initialize with the current questions point, assuming we are going to use it
        dp[i] = questions[i][0]
        skip = questions[i][1]
        # 5. Check we have questions after the given skip count
        if i + skip + 1 < n:
            # 6. Add that questions point to the current questions point
            dp[i] += dp[i+skip+1]
        # 7. Determine whether we use this question or skip it
        dp[i] = max(dp[i], dp[i+1])
    # 8. Return the last value which will be the maximum
    return dp[0]


def alternate_solution(questions):
    n = len(questions)
    dp = [0] * n
    def point(i):
        if i >= n:
            return 0
        if dp[i]:
            return dp[i]
        curr_point, skip = questions[i]
        dp[i] = max(curr_point + point(i+skip+1), point(i+1))
        return dp[i]
    return point(0)


if __name__ == "__main__":
    print(problem_to_solve([[3,2],[4,3],[4,4],[2,5]]))
    print(problem_to_solve([[1,1],[2,2],[3,3],[4,4],[5,5]]))
    print(problem_to_solve([[12,46],[78,19],[63,15],[79,62],[13,10]]))
    print(alternate_solution([[12, 46], [78, 19], [63, 15], [79, 62], [13, 10]]))
