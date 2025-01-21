def two_sum(nums, target):
    remainder = {}
    for i in range(len(nums)):
        if target - nums[i] in remainder:
            return remainder[target-nums[i]], i
        remainder[nums[i]] = i


if __name__ == "__main__":
    print(two_sum([2,7,11,15],9))
