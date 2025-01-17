def mergeAlternately(word1: str, word2: str) -> str:
    merge_str = ""
    word1_index = 0
    word2_index = 0
    word_1_len = len(word1)
    word_2_len = len(word2)
    if not word1 and not word2:
        return merge_str
    while True:
        merged = True
        if word1_index < word_1_len:
            merge_str += word1[word1_index]
            word1_index += 1
            merged = False
        if word2_index < word_2_len:
            merge_str += word2[word2_index]
            word2_index += 1
            merged = False
        if merged:
            break
    return merge_str


def alternate_solution(word1: str, word2: str) -> str:
    result = []
    word_1_len = len(word1)
    word_2_len = len(word2)
    max_n = max(word_1_len, word_2_len)
    for i in range(max_n):
        if i < word_1_len:
            result.append(word1[i])
        if i < word_2_len:
            result.append(word2[i])
    return "".join(result)


if __name__ == "__main__":
    print(mergeAlternately("abcd", "efgh"))
    print(mergeAlternately("ab", "efgh"))
    print(mergeAlternately("abcd", "ef"))
    print(mergeAlternately("", "ef"))
    print(mergeAlternately("ab", ""))
    print(mergeAlternately("", ""))

    print(alternate_solution("abcd", "ef"))
