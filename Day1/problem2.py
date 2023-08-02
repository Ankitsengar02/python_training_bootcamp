p_phrase="was it a car or a cat I saw"

words = p_phrase.split()
print(words)
reversed_words = [word[::-1].upper() for word in words]
print(reversed_words)
output_sentence = " ".join(reversed_words)
print(output_sentence)