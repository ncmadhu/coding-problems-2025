def min_max(arr):
    min = max = arr[0]
    sum = 0
    for n in arr:
        if n < min:
            min = n
        elif n < max:
            max = n
        sum += n
    return sum - max, sum - min


if __name__ == "__main__":
    print(min_max([7, 69, 2, 221, 8974]))
