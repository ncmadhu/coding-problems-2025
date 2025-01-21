def power_of_three(num):
    if num == 0:
        return False
    while num % 3 == 0:
        num = num // 3
    return num == 1


if __name__ == "__main__":
    print(power_of_three(9))
    print(power_of_three(3))
