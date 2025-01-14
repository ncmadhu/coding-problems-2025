def unsorted_array_target_sum(arr, target):
    remainders = {}
    for i, n in enumerate(arr)
        if target - n in remainders:
            return remainders[target-n], i
        else:
            remainders[n] = i



if __name__ == "__main__":
    print(unsorted_array_target_sum([2,7,11,15], target=13))

