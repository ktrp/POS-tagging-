import nltk
from nltk.tokenize import sent_tokenize, word_tokenize, PunktSentenceTokenizer
from nltk import pos_tag

example_text = input('Please enter the text:')


# print(sent_tokenize(example_text))

# print(word_tokenize(example_text))


print("Sentece seperated")
sentence = sent_tokenize(example_text)
print(sentence)

print("Words seperated")
words = word_tokenize(example_text)
print(words)

print(nltk.wordpunct_tokenize(example_text))

print("Parts of Speech:")
print(nltk.pos_tag(words))
