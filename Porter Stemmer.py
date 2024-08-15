a. Porter Stemmer
The Porter Stemmer, developed by Martin Porter in 1980, is a widely used algorithm in natural language processing (NLP) for reducing words to their root forms, or stems. This process helps in standardizing words and improving the performance of text-based applications, such as search engines and information retrieval systems.

Code :
# Program to implement Porter Stemmer
print("Name : Trupti Bhostekar \tRoll No : 2")
import nltk
nltk.download('punkt')
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
# Defining the stemmer
porter = PorterStemmer()
# Taking words which have a similar stem
terms = ["gene", "genes", "genesis", "genetic", "generic", "general"]

# Performing stemming using porter stemmer on words
print("\n1. Performing porter stemming on the words")
for each_term in terms:
 print(porter.stem(each_term))

# Taking a sentence
sentence = "Heya Reeba, do you know it is important to be pythonly while pythoning with pythonlanguage. Stay being a pythoner"

# Performing stemming using porter stemmer on a sentence
print("\n2. Performing porter stemming on a sentence")
words = word_tokenize(sentence, language = 'english')
for each_word in words:
 print(porter.stem(each_word))
