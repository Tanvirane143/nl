b. Study lemmas, hyponyms, hypernyms, entailments

Lemmatization usually refers to doing things properly with the use of a vocabulary and
morphological analysis of words, normally aiming to remove inflectional endings only and to
return the base or dictionary form of a word, which is known as the lemma .
Hyponyms: More specific terms. Both come to picture as Synsets are organized in a structure
similar to that of an inheritance tree. This tree can be traced all the way up to a root hypernym.
Hypernyms provide a way to categorize and group words based on their similarity to each
other.
Hypernym extraction is a crucial task for semantically motivated NLP tasks such as taxonomy
and ontology learning, textual entailment or paraphrase identification. ... Our experiments
confirm that both syntactic and definitional information play a crucial role in
the hypernym extraction task.
Textual entailment (TE) in natural language processing is a directional relation between text
fragments. The relation holds whenever the truth of one text fragment follows from another
text. In the TE framework, the entailing and entailed texts are termed text (t) and hypothesis
(h), respectively.

Code : 

import nltk
from nltk.corpus import wordnet
print(wordnet.synsets("computer"))
print(wordnet.synset("computer.n.01").lemma_names())

#all lemmas for each synset.
for e in wordnet.synsets("computer"):
  print(f'{e} --> {e.lemma_names()}')

#print all lemmas for a given synset
print(wordnet.synset('computer.n.01').lemmas())

#get the synset corresponding to lemma
print(wordnet.lemma('computer.n.01.computing_device').synset())

#Get the name of the lemma
print(wordnet.lemma('computer.n.01.computing_device').name())

#Hyponyms give abstract concepts of the word that are much more specific
#the list of hyponyms words of the computer
syn = wordnet.synset('computer.n.01')
print(syn.hyponyms)
print([lemma.name() for synset in syn.hyponyms() for lemma in synset.lemmas()])

#the semantic similarity in WordNet
vehicle = wordnet.synset('vehicle.n.01')
car = wordnet.synset('car.n.01')
print(car.lowest_common_hypernyms(vehicle))
