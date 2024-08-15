d. Tokenization using the spaCy library 
spaCy is a powerful and efficient library for natural language processing in Python. It provides a variety of advanced NLP capabilities, including tokenization, which is the process of breaking down text into individual tokens (such as words and punctuation marks). spaCy's tokenization is particularly robust, as it handles a wide range of linguistic features out-of-the-box.

Code : 
#pip install -U spacy
#python -m spacy download en
from spacy.lang.en import English
# Load English tokenizer, tagger, parser, NER and word vectors
nlp = English()
text = """Founded in 2002, SpaceX’s mission is to enable humans to become a spacefaring civilization and a multi-planet
species by building a self-sustaining city on Mars. In 2008, SpaceX’s Falcon 1 became the first privately developed
liquid-fuel launch vehicle to orbit the Earth."""
# "nlp" Object is used to create documents with linguistic annotations.
my_doc = nlp(text)
# Create list of word tokens
token_list = []
for token in my_doc:
 token_list.append(token.text)
token_list
print(token_list)
