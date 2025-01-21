def two_sum_sorted(numbers, target):
    left = 0
    right = len(numbers) - 1
    while left < right:
        if numbers[left] + numbers[right] == target:
            return left+1, right+1
        elif numbers[left] + numbers[right] < target:
            left += 1
        else:
            right -= 1


if __name__ == "__main__":
    print(two_sum_sorted([2,7,11,15], 9))
