def mystery(n):
    if n < 0:
        n = -n
    if n == 0:
        return n * 10 == 0
    else:
        return (n - n)  == 0


if __name__ == "__main__":
    print(mystery(10))
    print(mystery(-10))
    print(mystery(0))
