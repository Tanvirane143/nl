a. Study of various Corpus – Brown, Inaugural, Reuters, udhr with various methods like
fields, raw, words, sents, categories. 

As just mentioned, a text corpus is a large body of text. Many corpora are designed to contain
a careful balance of material in one or more genres. We examined some small text collections, such as the speeches known as the US Presidential Inaugural Addresses. 
This particular corpus actually contains dozens of individual texts — one per address — but for convenience we glued them end-to-end and treated them as a single text, also used various predefined texts that we accessed by typing from nltk.book import *. However, since we want to be able to work with other texts, this section examines a variety of text corpora. We'll see how to select individual texts, and how to work with them.

The Brown Corpus is a balanced corpus consisting of 500 text samples from 15 different categories.
Fields: Metadata about the corpus.
Raw Text: Full raw text of a specific file.
Words: Tokenized words in the corpus.
Sentences: Tokenized sentences in the corpus.
Categories: Accessing different categories of the corpus.

Code : 

import nltk
nltk.download('brown')
from nltk.corpus import brown
brown.categories()

brown.fileids()

brown.words(categories = 'news')

brown.words(fileids='cg22')

brown.sents(categories=['news','editorial','reviews'])

