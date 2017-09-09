import preprocessing as ngrams
import random
import nltk

unigram_map,token_count = ngrams.unigram_prep('./Project1/SentimentDataset/Dev/neg.txt')

#print (len(unigram_map))

for x in range(10):
  ran= random.randint(0,len(unigram_map))
#  print unigram_map[ran]
#print

## bigrams
tokens = ngrams.createTokens('./Project1/SentimentDataset/Dev/neg.txt')


bigram_dict,num_bigrams = ngrams.get_bigrams(tokens,len(tokens))
print bigram_dict['.'].keys()
print (len(bigram_dict['.'].keys()))
