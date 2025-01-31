from functools import partial

def power(a, b):
    return a ** b

power2 = partial(power, b=2)

if __name__ == "__main__":
    print(power(2,3))
    print(power2(2))
    print(power2.func)
    print(power2.args)
    print(power2.keywords)
