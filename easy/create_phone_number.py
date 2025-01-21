def create_phone_number(n):
    prefix = ''.join([str(x) for x in n[0:3]])
    middle = ''.join([str(x) for x in n[3:6]])
    end = ''.join([str(x) for x in n[6:]])
    return f'({prefix}) {middle}-{end}'


if __name__ == "__main__":
    print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
