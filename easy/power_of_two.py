def power_of_two(num):
    remainder = 0
    while num > 1 and remainder == 0:
        remainder = num % 2
        num = num // 2
        if remainder:
            return False
    return True

def neat_solution(num):
    if num == 0:
        return False
    while num % 2 == 0:
        num = num // 2
    return num == 1


if __name__ == "__main__":
    print(power_of_two(8))
    print(neat_solution(8))
