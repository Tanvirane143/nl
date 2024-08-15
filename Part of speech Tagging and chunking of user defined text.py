a. Part of speech Tagging and chunking of user defined text. 

Theory: POS Tagging (Parts of Speech Tagging) is a process to mark up the words in text format for a particular part of a speech based on its definition and context. It is responsible for text reading in a language and assigning some specific token (Parts of Speech) to each word. It is also called grammatical tagging.

Code : 
import nltk
from nltk import pos_tag
from nltk import RegexpParser
nltk.download()
text ="This is practical no 6".split()
print("After Split:",text)
nltk.download('averaged_perceptron_tagger')
# averaged_perceptron_tagger is used for tagging words with their parts of speech (POS)
tokens_tag = pos_tag(text)
print("After Token:",tokens_tag)
patterns= """mychunk:{<NN.?>*<VBD.?>*<JJ.?>*<CC>?}"""
chunker = RegexpParser(patterns)
print("After Regex:",chunker)
output = chunker.parse(tokens_tag)
print("After Chunking",output)
