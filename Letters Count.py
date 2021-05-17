sentence = input("Enter a sentence :")
sentence_dict = {}
for i in sentence:
    letter_count = sentence.count(i)
    sentence_dict [i] = letter_count
print(sentence_dict)