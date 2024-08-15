a. Study of Wordnet Dictionary with methods as synsets, definitions, examples, antonyms.

WordNet is a large lexical database of English, developed at Princeton University. It groups English words into sets of synonyms called synsets, provides short definitions and usage examples, and records a number of relations among these synonym sets or their members.

Synsets : Synsets are sets of cognitive synonyms (synonyms that express the same concept). Each synset represents a distinct concept and contains a group of words that are interchangeable in some context.

Definitions : Each synset comes with a short definition that explains the concept it represents.

Examples : WordNet provides usage examples for synsets to illustrate how the words in the synset can be used in context.

Antonyms : WordNet includes antonyms for some words. Antonyms are words with opposite meanings.

Code : 
import nltk
nltk.download('wordnet')

from nltk.corpus import wordnet
print(wordnet.synsets("computer"))
# definition and example of the word ‘computer’
print(wordnet.synset("computer.n.01").definition())

#examples
print("Examples:", wordnet.synset("computer.n.01").examples())

#get Antonyms
print(wordnet.lemma('buy.v.01.buy').antonyms())
