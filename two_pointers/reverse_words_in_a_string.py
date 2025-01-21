# Example 1:
#
# Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
# Example 2:
#
# Input: s = "Mr Ding"
# Output: "rM gniD"

def reverse_words_in_a_string(sentence):
    sen_list = list(sentence)
    sen_length = len(sen_list)
    left = right = 0
    for right in range(sen_length):
        if sen_list[right] == ' ':
            # reverse the words
            mid = (left + right) // 2
            end = right - 1
            while left < mid:
                sen_list[left], sen_list[end] = sen_list[end], sen_list[left]
                left += 1
                end -= 1
            left =  right + 1
    mid = (left + right) // 2
    end = right
    while left < mid:
        sen_list[left], sen_list[end] = sen_list[end], sen_list[left]
        left += 1
        end -= 1
    return "".join(sen_list)

def alternate_solution(sentence):
    left = right = 0
    s_list = list(sentence)
    s_len = len(s_list)
    for right in range(s_len):
        if s_list[right] == ' ':
            reverse_str(s_list, left, right-1)
            left = right + 1
    reverse_str(s_list, left, right)
    return "".join(s_list)

def reverse_str( word, start, end):
    mid = (start + end) // 2
    while start <= mid:
        word[start], word[end] = word[end], word[start]
        start += 1
        end -= 1


if __name__ == "__main__":
    print(reverse_words_in_a_string("Let's take LeetCode contest"))
    print(alternate_solution("Let's take LeetCode contest"))
