c. Tokenization using NLTK
The Natural Language Toolkit (NLTK) is a comprehensive library for natural language processing in Python. It provides powerful tools for text processing, including tokenization, which is the process of splitting text into individual tokens (words, sentences, etc.). NLTK offers several built-in tokenizers that handle various aspects of tokenization.

Code : 
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
text = """Founded in 2002, SpaceX’s mission is to enable humans to become a spacefaring civilization and a multi-
planet
species by building a self-sustaining city on Mars. In 2008, SpaceX’s Falcon 1 became the first privately developed
liquid-fuel launch vehicle to orbit the Earth."""
a=word_tokenize(text)
print(a)
