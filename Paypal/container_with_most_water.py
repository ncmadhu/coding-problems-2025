# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.
#
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
# Example 2:
#
# Input: height = [1,1]
# Output: 1

def container_with_most_water(height):
    left = 0
    right = len(height) - 1
    max_area = 0
    while left < right:
        curr_width = right - left
        curr_height = min(height[left], height[right])
        max_area = max(max_area, curr_width * curr_height)
        if height[left] > height[right]:
            right -= 1
        elif height[left] < height[right]:
            left += 1
        else:
            left += 1
            right -= 1
    return max_area


if __name__ == "__main__":
    print(container_with_most_water([1,8,6,2,5,4,8,3,7]))
    print(container_with_most_water([1,1]))
