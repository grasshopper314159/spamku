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
import pickle
import string
nltk.download('cmudict')
from nltk.corpus import cmudict
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
pronunciation_dict = cmudict.dict()
from nltk import pos_tag

def get_word(POS, syllables, preceding_word):
    pass

def get_syllable_count(pronunciation_dict, word):
    #print(pronunciation_dict[word])
    syl=[ x for x in pronunciation_dict[word][0] if x[-1].isdigit()]
    return len(syl)

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

def sort_words_by_syllable(pronunciation_dict, text):
    syllable_dict = defaultdict(list)
    for i in range(8):
        for word in text.split(' '):
            try:
                word= word.translate(str.maketrans('', '', string.punctuation))
                if get_syllable_count(pronunciation_dict, word.lower()) == i:
                    syllable_dict[i].append(word)
            except:
                pass
                #print(word)
    return syllable_dict;
        

def loadData(filename): 
    file = open(filename, 'rb')      
    data = pickle.load(file) 
    file.close()
    return data

pos_patterns = loadData("pos_patterns.p")
pos_dict = loadData("pos_dict.p")


def get_pos_label(word):
    return pos_tag(word)[0][1]


def choose_target_syllable_count(pattern, number_of_syllables_wanted):
    from random import randint
    syllable_lengths = {
    'VB': 1,
    'DT': 1,
    'RB': 2,
    'NN': 5,
    'VBG': 3,
    'IN': 1,
    'NNS': 4,
    'PRP$': 1,
    'CC': 1,
    'JJ': 2,
    'WP': 1,
    'VBZ': 1,
    'PRP': 1, 
    'VBN': 2,
    'JJS': 2,
    'MD': 1, 
    'TO': 1,
    'VBD': 2,
    'VBP': 2,
    'WRB': 1,
    'CD': 1, #cardinal digit, could be more
    'RBR': 2,
    'JJR': 2,
    'WDT': 1,
    'WP$': 1
    }
    syllable_counts = []
    possible = False
    pattern_len = len(pattern.split())
    max_per_word = number_of_syllables_wanted - pattern_len
    for i in range(len(pattern)):
        while possible == False:
            x = randint(1, syllable_lengths[pattern.split()[i]])
            if x <= max_per_word:
                possible = True
        syllable_counts.append[x]
        number_of_syllables_wanted -= x
        pattern_len -= 1
        max_per_word = number_of_syllables_wanted - pattern_len
    return syllable_counts
    syllable_counts = []
    possible = False
    pattern_len = len(pattern.split())
    max_per_word = number_of_syllables_wanted - pattern_len
    for i in range(len(pattern)):
        while possible == False:
            x = randint(1, syllable_lengths[pattern.split()[i]])
            if x <= max_per_word:
                possible = True
        syllable_counts.append[x]
        number_of_syllables_wanted -= x
        pattern_len -= 1
        max_per_word = number_of_syllables_wanted - pattern_len
    return syllable_counts


def main():
    pronunciation_dict = cmudict.dict()
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
    print('15 words from mc:', s)
    print("Procrastinate has", get_syllable_count(pronunciation_dict, 'procrastinate'), "syllables")
    #keys to this dict are digits 0 to 7.  Each key giveys you a list of words that with key-length syllables
    syllable_dict = sort_words_by_syllable(pronunciation_dict, text)
    print("All 6 syllable words in our spamku corpus:")
    print(syllable_dict[6])
    print(get_pos_label(['capicola']))
    print(get_pos_label(['pastrami']))
    print(get_pos_label(['andouille']))
    pos_patterns = loadData("pos_patterns.p")
    pos_dict = loadData("pos_dict.p")
    pattern_prob = []
    for k,v in pos_patterns.items():
        for i in range(v):
            try:
                if v != "":
                    pattern_prob.append(k)
            except:
                print("error: ", k, v)
    num_diff_patterns = len(pattern_prob)
    


    line1 = random.choice(pattern_prob)
    line2 = random.choice(pattern_prob)  # need to have two separate prob for 5 and 7
    line3 = random.choice(pattern_prob)
    l1=choose_target_syllable_count(line1, 5)

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
        