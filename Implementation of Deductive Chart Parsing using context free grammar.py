d. Implementation of Deductive Chart Parsing using context free grammar and a given sentence.

Deductive Chart Parsing is a method for parsing sentences using a chart data structure, which stores partial parse trees as they are constructed.

Code : 
import nltk
from nltk import CFG, ChartParser, word_tokenize

# Define the context-free grammar
grammar1 = CFG.fromstring("""
S -> NP VP
PP -> P NP
NP -> Det N | Det N PP | 'I'
VP -> V NP | VP PP
Det -> 'a' | 'my'
N -> 'bird' | 'balcony'
V -> 'saw'
P -> 'in'
""")

# Define the sentence and tokenize it
sentence = "I saw a bird in my balcony"
all_tokens = word_tokenize(sentence)
print(all_tokens)

# Initialize the chart parser with the grammar
parser = ChartParser(grammar1)

# Parse the tokens and print the parse trees
for tree in parser.parse(all_tokens):
    print(tree)
    #tree.draw()
