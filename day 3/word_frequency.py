def word_count(sentence):
    words = sentence.lower().split()
    frequency = {}

    for word in words:
        frequency[word] = frequency.get(word, 0) + 1

    return frequency

sentence = "python is easy and python is powerful"

result = word_count(sentence)

sorted_result = sorted(result.items(), key=lambda x: x[1], reverse=True)

for word, count in sorted_result:
    print(f"{word}: {count}")