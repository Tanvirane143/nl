f. Tokenization using Gensim. 
Gensim is a robust library for topic modeling and document similarity analysis in Python, and it includes utilities for text preprocessing, including tokenization. Gensim's gensim.utils module provides simple and effective functions for tokenizing text.

Code : 
from gensim.utils import tokenize
text = """Founded in 2002, SpaceX’s mission is to enable humans to become a spacefa
ring civilization and a multi-planet
species by building a selfsustaining city on Mars. In 2008, SpaceX’s Falcon 1 became the first privately deve
loped
liquid-fuel launch vehicle to orbit the Earth."""
list(tokenize(text))
