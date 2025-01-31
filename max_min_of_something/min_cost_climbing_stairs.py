from typing import List

def minCostClimbingStairs(cost: List[int]) -> int:
    # Bottom Up approach
    # Initialize a minCost array with one extra element indicating
    # top of the floor
    stairs = len(cost)
    minCostClimbing = [0] * (stairs + 1)

    # Start from 2 since the cost of reaching step 0 and step 1 is 0 since we can take one or two steps
    for i in range(2, stairs+1):
        # reaching current step i cost
        take_one_step = minCostClimbing[i-1] + cost[i-1]
        take_two_step = minCostClimbing[i-2] + cost[i-2]
        minCostClimbing[i] = min(take_one_step, take_two_step)
    # Last one is the top floor
    return minCostClimbing[-1]


def topDownApproach(cost: List[int]) -> int:
    memoization = {}
    def minimumCost(i):
        if i <= 1:
            return 0
        if i in memoization:
            return memoization[i]
        take_one_step = cost[i-1] + minimumCost(i-1)
        take_two_step = cost[i-2] + minimumCost(i-2)
        memoization[i] = min(take_one_step, take_two_step)
        return memoization[i]
    return minimumCost(len(cost))


def constant_space(cost):
    n = len(cost)
    if n <= 1:
        return 0
    t1 = t2 = 0
    for i in range(2, n+1):
        t1, t2 = min(t1 + cost[i-1], t2 + cost[i-2]), t1
    return t1

if __name__ == "__main__":
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    print(minCostClimbingStairs(cost))
    cost = [10,15,20]
    print(minCostClimbingStairs(cost))
    cost = [10,15,20]
    print(topDownApproach(cost))
    cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    print(topDownApproach(cost))
    print(constant_space(cost))
