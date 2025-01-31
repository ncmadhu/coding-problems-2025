def my_decorator(func):
    def wrapper():
        print("Before function execution")
        result = func()
        print("After function execution")
        return result
    return wrapper

@my_decorator
def test_decorator():
    print("From the function")


def decorator_with_args(times):
    def actual_decorator(func):
        def wrapper():
            for i in range(times):
                print(f"Before function execution {i}")
                result = func()
                print(f"After function execution {i}")
            return times
        return wrapper
    return actual_decorator

@decorator_with_args(3)
def test_decorator_with_args():
    print("From the function")


def decorator_for_func_with_args(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            print(arg)
        for key, value in kwargs.items():
            print(f'{key}: {value}')
    return wrapper

@decorator_for_func_with_args
def test_decorator_with_func_args(a,b, c=None,d=None):
    print("From the function")


if __name__ == "__main__":
    test_decorator()
    test_decorator_with_args()
    test_decorator_with_func_args("a", "b", c="c", d="d")