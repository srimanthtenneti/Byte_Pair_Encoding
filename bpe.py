###################################
# File :  Byte Pair Encoding 
# Author : Srimanth Tenneti 
# Date : 31st December 2023
###################################

import re
import numpy as np

dataset = open("data.txt", "r")
data = dataset.read()
chars = sorted(list(set(data))) 
datax = dataset.readlines()

n_iter = 500 ### Number of BPE itrations 

word_occurances = {} ### New Corpus 
for sent in datax : 
    for word in sent.split() : 
        if word in word_occurances : 
            word_occurances[word] = word_occurances[word] + 1
        else : 
            word_occurances[word] = 1
    
### Split Each word in corpus into their constituent characters 
### BPE Parameter 
corpus = list()
rule_deck = {}

for i in range(n_iter) : 
    
    if i == 0 :   
        ### Build a merged corpus only once at start 
        for word in word_occurances : 
            cha = re.split("", word)
            cha.pop(0)
            cha.pop(-1) 
            corpus.append(cha)
            
    else : ### For all other itrations use the merged corpus to form new tokens 
        ### Now count the occurances of token pairs throughout all the words in the corpus 
        token_pairs = {}
        for word in corpus : 
            for i , j in zip(word, word[1:]) : 
                if i + j in token_pairs : 
                    token_pairs[i+j] = token_pairs[i+j] + 1
                else : 
                    token_pairs[i+j] = 1
                    
        rules = {}
        for word in corpus : 
            for i , j in zip(word, word[1:]) : 
                if i +','+ j in rules : 
                    rules[i +','+ j] = rules[i +','+ j] + 1
                else : 
                    rules[i +','+ j] = 1
        ### get the most occured token pair 
        
        rule = [k for k,v in rules.items() if v == max(rules.values())] 
        merge = [k for k,v in token_pairs.items() if v == max(token_pairs.values())]
        
        ### Just to handle the case of multiple pairs having same count 
        if len(merge) > 1 : 
            mp = np.random.choice(merge)
        else : 
            mp = merge[0] 
            
        if len(rule) > 1 : 
            r = np.random.choice(rule)
        else : 
            r = rule[0] 

        chars.append(mp)
        rule_deck[r] = mp

        for word in corpus : 
            for i in range(len(word)-1) : 
                    if word[i] + word[i+1] == mp : 
                        word[i:i+2] = [''.join(word[i:i+2])]
                        break
                    else : 
                        continue

### Encode Function 
def encode(string) :   
    stoi = {ch : i  for i, ch in enumerate(chars)}
    word = re.split('', string)

    word.pop(0)
    word.pop(-1)

    final_word = []

    for k, v in rule_deck.items() :
        for i in range(len(word)-1) : 
            if word[i] + word[i+1] == ''.join(k.split(',')): 
                word[i:i+2] = [''.join(k.split(','))]
                final_word.append(word)
                break
               
    return [stoi[c] for c in final_word[-1]]

### Decode Function 
itos = {i  : ch for i, ch in enumerate(chars)} 
decode = lambda l : ''.join([itos[i] for i in l])
