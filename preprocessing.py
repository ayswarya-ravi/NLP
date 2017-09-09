import nltk

def createTokens(path):
    print("abc")
    lines = open(path).read()
    tokens = nltk.word_tokenize(lines)
    words = [w.lower() for w in tokens]
    return words

def unigram_prep(path):
    words = createTokens(path);
    #print(words)
    total_tokens=len(words)
    return sorted(words),total_tokens
   
def create_dictionary(tokens):
    uni_dict={}
    for token in tokens:
	if token not in dict:
	  uni_dict[token] = 1
	else:
	  uni_dict[token] += 1
    return uni_dict

def probability_calc(tokens,dictionary,total_tokens):
    prob_dict={}
    for token in tokens:
        prob_dict[token]=dictionary[token]/total_tokens
    return prob_dict

#Get  the next probable word for a token
def predict_next(bigram_dict,start_word):
    ##TODO: write logic to get the word with max probability   
    word=[]
    return word

def get_biprob(bigram_dict,num_bigrams):
     prob_dict={}
     for token in bigram_dict.keys():
        for  next in bigram_dict[token].keys():
	    prob_dict[token][next] = bigram[token][next] /len(bigram[token].keys())    
     return prob_dict

## Build dictionary of bigrams 
def get_bigrams(tokens,total_tokens):
    bigram_dict={}
    for i in range(0,total_tokens-2):
        if tokens[i] in bigram_dict:
            if tokens[i+1] in bigram_dict[tokens[i]]:
               bigram_dict[tokens[i]][tokens[i+1]] += 1
            else:
               bigram_dict[tokens[i]][tokens[i+1]] = 1
	else:
           bigram_dict[tokens[i]]={}
           bigram_dict[tokens[i]][tokens[i+1]] = 1
    return bigram_dict,len(bigram_dict)


## Random sentence generator bigrams 
## Input: max len of sentence,Initial unigram tokens,optional sentence start tokens

def get_bisentence(max_len,tokens,sentence=''):
    bigram_dict,num_bigrams = get_bigrams(tokens,len(tokens))
    bigram_prob_dict = get_biprob(bigram_dict,num_bigrams)
    start_len=len(sentence)        

    #if no start token given,choose 1 word from the words occuring after '.'(Possible sentence start words)
    if start_len==0:
       sentence= bigram_dict['.'].keys()
       start_token= sentence[len(sentence)-1]
    else:
       sentence_tokens = sentence.split()
       start_token= sentence_tokens[len(sentence_tokens)-1]
   #predict next_words for max count 
    while (max_len):
       if start_token in bigram_dict.keys():
           next=predict_next(bigram_dict,start_token,bigram_prob_dict)
       else:
           next=random.choice(bigram_dict.keys())         
       sentence = sentence + ' '+ next
    
    return sentence

#print(unigram_prep('./Project1/SentimentDataset/Dev/neg.txt'))
