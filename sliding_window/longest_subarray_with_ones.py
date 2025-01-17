# You are given a binary string s (a string containing only "0" and "1"). You may choose up to one "0"
# and flip it to a "1". What is the length of the longest substring achievable that contains only "1"?
# For example, given s = "1101100111", the answer is 5. If you perform the flip at index 2, the string becomes 1111100111

def longest_subarray_with_one(s):
    left = zero_count = sub_arr_len = 0
    for right in range(len(s)):
        if s[right] == '0':
            zero_count += 1
        while zero_count > 1:
            if s[left] == '0':
                zero_count -= 1
            left += 1
        sub_arr_len = max(sub_arr_len, right - left + 1)
    return sub_arr_len


if __name__ == "__main__":
    print(longest_subarray_with_one("1101100111"))
