# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import nltk;
nltk.download('punkt')

 	
from nltk.corpus import PlaintextCorpusReader
corpus_root = r'C:\cs\nlp\proj\corpus'
poems = PlaintextCorpusReader(corpus_root, '.*')
words=poems.words()
sents=poems.sents()
print(len(sents))
print(sents[1])
#wordlists.words('connectives')

fdist1 = nltk.FreqDist(poems)