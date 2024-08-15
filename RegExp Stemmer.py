d. RegExp Stemmer 
The RegExp Stemmer, short for Regular Expression Stemmer, is a simpler and more flexible stemming approach that uses regular expressions (regex) to define rules for reducing words to their root forms. This method relies on pattern matching and replacement techniques, making it highly customizable for specific needs. Unlike more structured algorithms like Porter or Snowball, the RegExp Stemmer is straightforward but requires careful crafting of regex patterns to ensure effectiveness.

Code : 
# Program to implement RegExp Stemmer
print("Name : Trupti Bhostekar \tRoll No : 2")
import nltk
nltk.download('punkt')
from nltk.stem import RegexpStemmer
# Defining the stemmer
regexp = RegexpStemmer('ing$|s$|e$|able$|ment$|less$|ly$', min=4)
# Performing stemming one word
print("\n1. Performing regexp stemming on one word at a time")
print(regexp.stem('cars'))
print(regexp.stem('bee'))
print(regexp.stem('compute'))
# Taking a list of word
terms = ["truptis", "stemming", "mentally", "ease","rockstar", "frictionless", "management","flowers",
"advisable"]
# Performing stemming using lancaster stemmer on words
print("\n2. Performing regexp stemming on a list of words")
for each_term in terms:
 print(regexp.stem(each_term))
