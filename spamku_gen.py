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
import random


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


def generate_sentence(chain, count=15):
    '''Input a dictionary in the format of key = current word, value = list of next words
       along with the number of words you would like to see in your generated sentence.'''

    # Capitalize the first word
    word1 = random.choice(list(chain.keys()))
    sentence = word1.capitalize()

    # Generate the second word from the value list. Set the new word as the first word. Repeat.
    for i in range(count-1):
        word2 = random.choice(chain[word1])
        word1 = word2
        sentence += ' ' + word2

    # End it with a period
    sentence += '.'
    return(sentence)

def main():
    haiku_list=[]
    # This file contains 8893 spam-ku
    filename="corpus/spamku.txt"
    file = open(filename, mode = 'r')
    # text is for input into a crude markov chain
    text = ""
    for line in file:
        text += line.strip()+' '
    file.close()
    
    mc=markov_chain(text)
    s = generate_sentence(mc, 15)
    print('15 words', s)


if __name__=='__main__':
    main()


###############################################################
#               scractch work
###########################################################

def process_one_list(a_list):
    t=""
    for lines in a_list:
        t+=line.strip()+' '
    return t

def process_list_of_lists(lists):
    t=""
    for lines in lists:
        t = process_one_list(lines)
    return t
        