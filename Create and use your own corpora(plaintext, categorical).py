b. Create and use your own corpora(plaintext, categorical)

Building a custom corpus can be useful for specific text analysis or natural language processing (NLP) tasks. In the following Python recipe, we are going to create a custom corpora which must be within one of the paths defined by NLTK. It is so because it can be found by NLTK. In order to avoid conflict with the official NLTK data package, let us create a custom natural_language_toolkit_data directory in our home directory.

Code : 

import os, os.path
path = os.path.expanduser('~/natural_language_toolkit_data')
if not os.path.exists(path):
  os.mkdir(path)
os.path.exists(path)



Now we will make a wordlist file, named wordfile.txt and put it in nltk_data directory (content/wordfile.txt) and will load it by using nltk.data.load 

Corpus readers
NLTK provides various CorpusReader classes.

Creating wordlist corpus
NLTK has WordListCorpusReader class that provides access to the file containing a list of
words. For the following we need to create a wordlist file which can be CSV or
normal text file. For example, we have created a file named ‘list’ that contains the following
data .

Code : 


#Creating wordlist corpus
from nltk.corpus.reader import WordListCorpusReader
reader_corpus = WordListCorpusReader('.',['wordfile.txt'])
reader_corpus.words()
