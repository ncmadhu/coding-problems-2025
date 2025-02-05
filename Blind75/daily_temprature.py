# Given an array of integers temperatures represents the daily temperatures, return an array answer such that
# answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no
# future day for which this is possible, keep answer[i] == 0 instead.

# Example 1:
#
# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
# Example 2:
#
# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]
# Example 3:
#
# Input: temperatures = [30,60,90]
# Output: [1,1,0]

def next_warmer_temprature_naive(tempratures):
    ans = []
    for i in range(len(tempratures)):
        days = 0
        for j in range(i+1, len(tempratures)):
            if tempratures[j] > tempratures[i]:
                days = j-i
                break
        ans.append(days)
    return ans


def next_warmer_temprature_monotonic_increasing_stack(tempratures):
    stack = [] # Monotonic stack
    ans = [0] * len(tempratures)

    for i in range(len(tempratures)-1, -1, -1):
        while stack and tempratures[stack[-1]] < tempratures[i]:
            stack.pop()
        if stack:
            ans[i] =  stack[-1] - i
        stack.append(i)
    return ans


def next_warmer_temprature_monotonic_decreasing_stack(tempratures):
    stack = []
    ans = [0] * len(tempratures)
    for i in range(len(tempratures)):
        # we are building a monotonically decreasing stack
        # Hence if the current element is greater than the last element
        # in the stack, it would violate the property. Hence removing the elements
        # lesser than the current element, before adding the current element to the stack
        while stack and tempratures[stack[-1]] <= tempratures[i]:
            # We store the index of the elements, since we are targeting to find the distance two elements
            # rather than the difference between the temperatures
            j = stack.pop()
            ans[j] = i - j    # for the element at index j the current element at i is the next biggest element
        # Add the current element to the stack
        stack.append(i)
    return ans


def replay(tempratures):
    stack = []
    ans = [0] * len(tempratures)

    for i in range(len(tempratures)):
        while stack and tempratures[stack[-1]] < tempratures[i]:
            j = stack.pop()
            ans[j] = i - j
        stack.append(i)

    return ans




if __name__ == "__main__":
    print(next_warmer_temprature_naive([73, 74, 75, 71, 69, 72, 76, 73]))
    print(next_warmer_temprature_naive([30, 60, 90]))
    print(next_warmer_temprature_naive([90, 60, 30]))
    print(next_warmer_temprature_naive([90]))
    print(next_warmer_temprature_monotonic_increasing_stack([73, 74, 75, 71, 69, 72, 76, 73]))
    print(next_warmer_temprature_monotonic_increasing_stack([30, 60, 90]))
    print(next_warmer_temprature_monotonic_increasing_stack([90, 60, 30]))
    print(next_warmer_temprature_monotonic_increasing_stack([90]))
    print(next_warmer_temprature_monotonic_decreasing_stack([73, 74, 75, 71, 69, 72, 76, 73]))
    print(next_warmer_temprature_monotonic_decreasing_stack([30, 60, 90]))
    print(next_warmer_temprature_monotonic_decreasing_stack([90, 60, 30]))
    print(next_warmer_temprature_monotonic_decreasing_stack([90]))