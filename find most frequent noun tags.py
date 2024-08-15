d. Write a program to find the most frequent noun tags.

To find the most frequent noun tags in a tagged corpus using NLTK, you can follow these steps:
Access the tagged words from a corpus.
Filter out the noun tags.
Compute the frequency distribution of these tags.
Identify the most frequent noun tags.

Code : 

nltk.download('universal_tagset')
from nltk.corpus import brown
noundist = nltk.FreqDist(w2 for ((w1, t1), (w2, t2)) in
      nltk.bigrams(brown.tagged_words(tagset="universal"))
      if w1.lower() == "the" and t2 == "NOUN")
noundist.most_common(10)
