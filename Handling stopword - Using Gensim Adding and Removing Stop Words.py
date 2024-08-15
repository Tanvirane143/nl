Using Gensim Adding and Removing Stop Words in Default Gensim Stop Words List

Gensim, a popular library for topic modeling and natural language processing tasks, also provides a set of default stop words.
Similar to NLTK, you can add or remove words from Gensim's default stop words list to customize it according to your needs.

Code : 
import gensim
from gensim.parsing.preprocessing import remove_stopwords
text = "Yashesh likes to play football, however he is not too fond of tennis."
print('Original text: ', text)
filtered_sentence = remove_stopwords(text)
print('\n After removing Stop words: ',filtered_sentence)

#The below line retrieves the default set of stop words from Gensim and prints them.
all_stopwords = gensim.parsing.preprocessing.STOPWORDS
print('\n Stop words in Gensim: ', all_stopwords)

#'''The following script adds likes and play to the list of stop words in Gensim:'''
from gensim.parsing.preprocessing import STOPWORDS
all_stopwords_gensim = STOPWORDS.union(set(['likes', 'play'])) # adding 'likes' and 'play' to stop words

text = "Yashesh likes to play football, however he is not too fond of tennis."
text_tokens = word_tokenize(text)

# Filter out the tokens that are in the new stop words set (including 'likes' and 'play')
tokens_without_sw = [word for word in text_tokens if not word in
all_stopwords_gensim]
print("\n After adding likes & play in stop word collection: ",tokens_without_sw)




# Remove the word 'not' from the existing set of Gensim stop words
from gensim.parsing.preprocessing import STOPWORDS
all_stopwords_gensim = STOPWORDS
sw_list = {"not"}

all_stopwords_gensim = STOPWORDS.difference(sw_list)
text = "Yashesh likes to play football, however he is not too fond of tennis."
text_tokens = word_tokenize(text)

# Filter out the tokens again with 'not' removed from stop words set
tokens_without_sw = [word for word in text_tokens if not word in
all_stopwords_gensim]
print(tokens_without_sw)
