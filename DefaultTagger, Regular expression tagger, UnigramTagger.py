These taggers can be used individually or in combination to build more sophisticated taggers or to handle different tagging tasks effectively.

A. DefaultTagger
The DefaultTagger assigns a specific tag to every word in the text. It's useful as a baseline tagger or when dealing with unknown words.

Code : 
from nltk.corpus import brown
nltk.download('brown')
tags = [tag for (word, tag) in brown.tagged_words(categories='news')]
nltk.FreqDist(tags).max()
raw = 'I do not like green eggs and ham, I do not like them Sam I am!'
tokens = nltk.word_tokenize(raw)
default_tagger = nltk.DefaultTagger('NN')
default_tagger.tag(tokens)




B. Regular Expression Tagger:
The Regular Expression Tagger assigns tags based on matching patterns defined using regular expressions. It's useful for tagging specific patterns of words.

Code : 
import nltk
nltk.download('brown')
nltk.download('punkt')
from nltk.corpus import brown
from nltk import word_tokenize
from nltk import RegexpTagger
brown_sents = brown.sents(categories = 'news')
brown_tagged_sents = brown.tagged_sents(categories = 'news')
import nltk
nltk.download('brown')
nltk.download('punkt')
from nltk.corpus import brown
from nltk import word_tokenize
from nltk import RegexpTagger
brown_sents = brown.sents(categories = 'news')
brown_tagged_sents = brown.tagged_sents(categories = 'news')
patterns = [
(r'.*ing$', 'VBG'), # gerunds
(r'.*ed$', 'VBD'), # simple past
(r'.*es$', 'VBZ'), # 3rd singular present
(r'.*ould$', 'MD'), # modals
(r'.*\'s$', 'NN$'), # possessive nouns
(r'.*s$', 'NNS'), # plural nouns
(r'^-?[0-9]+(\.[0-9]+)?$', 'CD'), # cardinal numbers
(r'.*', 'NN') # nouns (default)
]
regexp_tagger = nltk.RegexpTagger(patterns)
regexp_tagger.tag(brown_sents[3])



C. Unigram Tagger
The UnigramTagger assigns tags based on the most frequent tag for each word in the training data. It's a basic but effective tagger that often performs well, especially for languages with relatively free word order.

Code : 
import nltk
nltk.download('brown')
nltk.download('punkt')
from nltk.corpus import brown
from nltk import UnigramTagger
brown_tagged_sents = brown.tagged_sents(categories = 'news')
brown_sents = brown.sents(categories = 'news')
unigram_tagger = nltk.UnigramTagger(brown_tagged_sents)
tags = unigram_tagger.tag(brown_sents[2007])
print("\nDisplaying the tags from brown sents : \n", tags)
evaluation = unigram_tagger.evaluate(brown_tagged_sents)
print("\nEvaluation of brown tagged sents : ", evaluation


