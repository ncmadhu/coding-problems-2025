def palindrome_check(string):
    str_len = len(string)
    mid = str_len // 2

    for i in range(mid):
        if string[i] != string[str_len-1-i]:
            return False
    return True

if __name__ == "__main__":
    print(palindrome_check("ABBA"))
    print(palindrome_check("ABBBA"))
    print(palindrome_check("ACDBA"))
    print(palindrome_check("CDBA"))