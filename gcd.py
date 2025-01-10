def gcd_of_two(n1, n2):
    s = n2
    if n1 < n2:
        n1 = s
    gcd = 0
    for i in range(1, s + 1):
        if (n1 % i == 0) and (n2 % i == 0):
            gcd = i
    return gcd

if __name__ == "__main__":
    print(gcd_of_two(9,6))
