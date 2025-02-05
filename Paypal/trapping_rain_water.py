# Given n non-negative integers representing an elevation map where the width of each bar is 1,
# compute how much water it can trap after raining.
#
# Example 1:
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case,
# 6 units of rain water (blue section) are being trapped.
#
# Example 2:
#
# Input: height = [4,2,0,3,2,5]
# Output: 9

def trapping_rain_water(heights):
    ans = 0
    left = 0
    right = len(heights) - 1
    max_left = heights[left]
    max_right = heights[right]

    while left < right:
        if max_left < max_right:
            left += 1
            max_left = max(max_left, heights[left])
            ans += max_left - heights[left]
        else:
            right -= 1
            max_right = max(max_right, heights[right])
            ans += max_right - heights[right]
    return ans


def naive_solution(heights):
    ans = 0
    n = len(heights)
    # Run iteration from 1 to n-1.Because before 0 nothing exists to hold water,
    # similarly after n-1 nothing to hold water
    for i in range(1, n-1):
        max_left = 0
        max_right = 0
        # for each height try to find the left and right max heights
        for j in range(i, -1, -1):
            max_left = max(max_left, heights[j])
        for j in range(i, n):
            max_right = max(max_right, heights[j])
        # Find the min of max_left and max_right, because that is the limiting factor to trap rain water
        ans += min(max_left, max_right) - heights[i]
    return ans


if __name__ == "__main__":
    print(trapping_rain_water([0,1,0,2,1,0,1,3,2,1,2,1]))
    print(trapping_rain_water([4,2,0,3,2,5]))
    print(naive_solution([0,1,0,2,1,0,1,3,2,1,2,1]))
    print(naive_solution([4,2,0,3,2,5]))