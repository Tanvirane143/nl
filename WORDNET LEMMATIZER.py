PART B : STUDY WORDNET LEMMATIZER

The WordNet Lemmatizer is a tool used in natural language processing (NLP) to reduce words to their base or dictionary form, known as the lemma. Unlike stemming, which often produces root forms by simply stripping suffixes, lemmatization considers the context and grammatical structure of the word to ensure the resulting lemma is a valid word.

Code : 
# Program to implement WordNet Lemmatizer
print("Name : Trupti bhostekar \tRoll No : 2")
import nltk
nltk.download('wordnet')
nltk.download('punkt')
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
# Initializing the Wordnet Lemmatizer
wordnet = WordNetLemmatizer()
# Performing WordNet lemmatization on single Words
print("\n1. Performing WordNet lemmatization on single Words")
print(wordnet.lemmatize("corpora"))
print(wordnet.lemmatize("best"))
print(wordnet.lemmatize("geese"))
print(wordnet.lemmatize("feet"))
print(wordnet.lemmatize("cacti"))
#Performing WordNet lemmatization on a sentence

print("\n2. Performing WordNet lemmatization on a sentence")
# Taking a sentence
sentence = "Heyaa trupti, how are you doing? Keep digging in for the sentences to observe lemmatization!"
# Tokenizing i.e. spliting the sentence into words
list_words = nltk.word_tokenize(sentence)
print("\nConverting the sentence into a list of words")
print(list_words)
# Lemmatize list of words and join
final = ' '.join([wordnet.lemmatize(each_word, pos = 'v') for each_word in list_words])
print("\nAfter applying wordnet lemmatizer, the result is....")
print(final)
