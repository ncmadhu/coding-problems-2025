# Using the Python language, have the function longest_word_in_sentence take the sen parameter being passed and return
# the largest word in the string. If there are two or more words that are the same length, return the first word from
# the string with that length. Ignore punctuation and assume sen will not be empty.

def longest_word_in_sentence(sentence):
    left = 0
    largest = 0
    largest_l = largest_r = 0
    for right in range(len(sentence)):
        while right < len(sentence) and sentence[right] != ' ':
            right += 1
        curr_word_length = right - left
        if curr_word_length > largest:
            largest_l = left
            largest_r = right
            largest = curr_word_length
        left = right + 1
    return sentence[largest_l:largest_r]





if __name__ == "__main__":
    print(longest_word_in_sentence("Longest word in the sentenc Largest"))
