# -*- coding: utf-8 -*-

#how to install gensim
#run the command below in cmd or terminal
# conda install -c anaconda gensim 

# Natural Language Processing

# Importing the libraries

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 30 02:42:42 2020

@author: sakib
"""


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import gensim

dataset = pd.read_csv('Tweets.csv')

X = dataset['text']

import re 

corpus= []

for i in range (len(X)):
    review = re.sub('[^A-Za-z]', ' ' ,X[i])
    review = review.lower()
    review = review.split()
    corpus.append(review)
EMBEDDING_DIM = 100
w2v = gensim.models.Word2Vec(sentences = corpus, size = EMBEDDING_DIM, window = 5, workers = 4, min_count = 2, sg = 1)


word1 = w2v.wv['best']
word2 = w2v.wv['brilliant']

print (w2v.wv.similarity('best', 'brilliant'))
print(w2v.wv.similarity('and', 'that'))

print (w2v.wv.doesnt_match(['me','blue','red']))