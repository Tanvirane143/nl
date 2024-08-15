c. Snowball Stemmer
The Snowball Stemmer, also known as the Porter2 Stemmer, is an advanced and more versatile version of the original Porter Stemmer, created by Martin Porter. Introduced in 2001, it provides more consistent and maintainable stemming rules and supports multiple languages, making it a robust tool in natural language processing (NLP).

Code : 
# Program to implement Snowball Stemmer
print("Name : Trupti Bhostekar \tRoll No : 2")
import nltk
nltk.download('punkt')
from nltk.stem.snowball import SnowballStemmer
# Defining the stemmer
snowball_english = SnowballStemmer("english")
snowball_english = SnowballStemmer("dutch")
# Performing stemming on one word
print("\n1. Performing snowball stemming one word")
word = snowball_english.stem("Vibing")
print(word)
# Taking a list of english words
terms = ["trupti", "cheerful", "bravery","drawing", "satisfactorily", "publisher", "painful", "hardworking",
"keys"]
# Performing stemming using snowball stemmer on words
print("\n2. Performing snowball stemming on a set of english language words")
for each_term in terms:
 print(snowball_english.stem(each_term))
# Taking a list of dutch words
# trupti = trupti, bessen = berries, vriendelijkheid = friendliness, hobbelig = bumpy
terms2 = ["trupti", "bessen", "vriendelijkheid", "hobbelig"]
print("\n3. Performing snowball stemming on a set of dutch language words")
for each_term in terms2:
 print(snowball_english.stem(each_term))
