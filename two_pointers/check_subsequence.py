def check_subsequence(str1, str2):
    i = j = 0
    while i < len(str1) and j < len(str2):
        if str1[i] == str2[j]:
            i += 1
        j += 1

    # If it is a subsequence, whole str1 would have been traversed
    # and i will be equal to len(str1)
    return i == len(str1)


if __name__ == "__main__":
    print(check_subsequence("ace", "acde"))
    print(check_subsequence("ace", "ace"))
    print(check_subsequence("ace", "ac"))
