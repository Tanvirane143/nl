c. Study Conditional frequency distributions

Conditional frequency distributions (CFD) are a powerful tool in natural language processing and text analysis, allowing you to analyze the frequency of words or other features given specific conditions. The NLTK library in Python provides robust support for CFD through the nltk.probability.ConditionalFreqDist class.

Code : 

#process a sequence of pairs
import nltk
nltk.download('inaugural')
nltk.download('udhr')

text = ['The', 'Fulton', 'County', 'Grand', 'Jury', 'said', ...]
pairs = [('news', 'The'), ('news', 'Fulton'), ('news', 'County'), ...]
import nltk
from nltk.corpus import brown
fd = nltk.ConditionalFreqDist(
      (genre, word)
      for genre in brown.categories()
      for word in brown.words(categories=genre))
genre_word = [(genre, word)
      for genre in ['news', 'romance']
      for word in brown.words(categories=genre)]
print(len(genre_word))
print(genre_word[:4])
print(genre_word[-4:])
cfd = nltk.ConditionalFreqDist(genre_word)
print(cfd)
print(cfd.conditions())
print(cfd['news'])
print(cfd['romance'])
print(list(cfd['romance']))
from nltk.corpus import inaugural
cfd = nltk.ConditionalFreqDist(
        (target, fileid[:4])
        for fileid in inaugural.fileids()
        for w in inaugural.words(fileid)
        for target in ['america', 'citizen']
        if w.lower().startswith(target))


from nltk.corpus import udhr
languages = ['Chickasaw', 'English', 'German_Deutsch',
'Greenlandic_Inuktikut', 'Hungarian_Magyar', 'Ibibio_Efik']
cfd = nltk.ConditionalFreqDist(
        (lang, len(word))
        for lang in languages
        for word in udhr.words(lang + '-Latin1'))

cfd.tabulate(conditions=['English', 'German_Deutsch'],
        samples=range(10), cumulative=True)
