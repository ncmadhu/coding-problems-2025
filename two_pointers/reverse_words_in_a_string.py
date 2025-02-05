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
    n = len(sentence)
    s = list(sentence)
    left = right = 0
    while right < n:
        if s[right] == " ":
            reverse_word(s, left, right)
            left = right + 1
        right += 1
    reverse_word(s, left, right)
    return "".join(s)

def reverse_word(s, left, right):
    mid = (left + right) // 2
    while left < mid:
        s[left], s[right-1] = s[right-1], s[left]
        left += 1
        right -= 1


if __name__ == "__main__":
    # print(reverse_words_in_a_string("Let's take LeetCode contest"))
    print(alternate_solution("Let's take LeetCode contest"))
