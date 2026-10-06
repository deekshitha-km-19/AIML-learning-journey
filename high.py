def find_words(words, k):
    result = []
    for i in words:
        if len(i) > k:
            result.append(i)
    return result

word_list = ["apple", "banana", "cherry", "date", "elderberry", "dragonfruit"]
k = 5
long_words = find_words(word_list, k)

print(f"Words longer than {k} characters: {long_words}")