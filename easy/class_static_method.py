class Number:
    test = 1
    def __init__(self, value):
        self.value = value

    @classmethod
    def create_from_string(cls, string_value):
        return cls(float(string_value))


class IntNumber(Number):
    def __init__(self, value):
        super().__init__(int(value))


if __name__ == "__main__":
    num = Number.create_from_string("10.5")
    print(num.value)
    print(type(num))
    print(type(num.value))
    num2 = Number(2)
    print(num2.test)
    Number.test = 4
    num3 = Number(3)
    print(num3.test)
    intNum = IntNumber.create_from_string("10.5")
    print(intNum.value)
    print(type(intNum))
    print(type(intNum.value))
    print(intNum.test)