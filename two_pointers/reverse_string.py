def reverse_string(string):
    string_len = len(string)
    str_list = list(string)
    mid = string_len // 2
    for i in range(mid):
        str_list[i],str_list[-1-i] = str_list[-1-i], str_list[i]
    return "".join(str_list)


def two_pointer_solution(string):
    str_list = list(string)
    str_len = len(string)
    left = 0
    right = str_len - 1
    while left < right:
        str_list[left], str_list[right] = str_list[right], str_list[left]
        left += 1
        right -= 1
    return "".join(str_list)

if __name__ == "__main__":
    print(reverse_string("eventest"))
    print(reverse_string("oddtest"))
    print(two_pointer_solution("eventest"))
    print(two_pointer_solution("oddtest"))
