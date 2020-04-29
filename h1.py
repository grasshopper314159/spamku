# -*- coding: utf-8 -*-
"""
1) parse spamku into parts of speech
2) classify lines by grammatical structure
2a) calculate probabilites of b line structure given a line structure
2b) calculate probabilies of word being used given structure

3) randomly select structure
4) create word dicts - probability of one word given the preceding word


-classify lines by number of syllables
-factor in probability of a word choice given the preceding number of syllables 
-make function syllable count

"""

import nltk
import os
from collections import defaultdict

c=0
l=[]
haiku_list=[]
def get_word(POS, syllables, preceding_word):
    pass

def get_syllable_count(word):
    pass

def markov_chain(text):
    '''The input is a string of text and the output will be a dictionary with each word as
       a key and each value as the list of words that come after the key in the text.'''
    
    # Tokenize the text by word, though including punctuation
    words = text.split(' ')
    
    # Initialize a default dictionary to hold all of the words and next words
    m_dict = defaultdict(list)
    
    # Create a zipped list of all of the word pairs and put them in word: list of next words format
    for current_word, next_word in zip(words[0:-1], words[1:]):
        m_dict[current_word].append(next_word)

    # Convert the default dict back into a dictionary
    m_dict = dict(m_dict)
    return m_dict

def process(list):
    t=""
    for line in list:
        t+=line.strip()
    return t


# This file contains 8893 spam-ku
filename="spamku.txt"
file = open(filename, mode = 'r')
# make a list of spamku
for line in file:
    c+=1
    l.append(line)
    if c==3:
        haiku_list.append(l)
        c=0
        l=[]
file.close()




        