Studying tagged corpora involves analyzing text data where each word is associated with a part-of-speech (POS) tag. Parts of speech are also known as word classes or lexical categories. The collection of tags used for a particular task is known as a tagset. This tagging provides valuable syntactic information that can be used for various natural language processing (NLP) tasks. NLTK offers several tagged corpora, such as the Brown Corpus, and provides methods like tagged_sents and tagged_words to access this tagged data.

Tagged Words: Returns a list of (word, tag) tuples.
Tagged Sentences: Returns a list of sentences, where each sentence is a list of (word, tag) tuples.

Code : 

import nltk
from nltk import tokenize
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('words')

para = "And now we are going to learn something new"
sents = tokenize.sent_tokenize(para)
print("\nsentence tokenization\n===================\n",sents)

# word tokenization
print("\nword tokenization\n===================\n")
for index in range(len(sents)):
  words = tokenize.word_tokenize(sents[index])
  print(nltk.pos_tag(words))


import nltk
nltk.corpus.brown.tagged_words()


nltk.download('treebank')
nltk.corpus.treebank.tagged_words()
