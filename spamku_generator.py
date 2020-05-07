# -*- coding: utf-8 -*-
"""
Created on Thu May  7 08:45:25 2020

@author: njayj
"""

# -*- coding: utf-8 -*-
"""
1) parse spamku into parts of speech
2) classify lines by grammatical structure
3) randomly select structure
4) create word dicts - probability of one word given the preceding word


"""

# https://docs.python.org/3/library/os.html
import os

# https://docs.python.org/3/library/collections.html
from collections import defaultdict

# https://docs.python.org/3/library/random.html
import random

# https://docs.python.org/3/library/pickle.html
import pickle

# https://docs.python.org/3.0/library/string.html
import string

# https://www.nltk.org/
import nltk

# cmudict stands for Carnegie Mellon dict. Key is word, value is a list of strings containing pronuciations
from nltk.corpus import cmudict
nltk.download('cmudict')

# pos_tag is a function that returns parts of speech
#   An example from https://www.nltk.org/book/ch05.html
#       >> text = word_tokenize("And now for something completely different")
#       >> nltk.pos_tag(text)
#       >> [('And', 'CC'), ('now', 'RB'), ('for', 'IN'), ('something', 'NN'), ('completely', 'RB'), ('different', 'JJ')]
from nltk import pos_tag

#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')

################################
#   Helper functions
################################


# Takes a string and removes punctuation and makes it lowercase
# returns a string
# Depends on import string
def clean_word(word):
    word= word.translate(str.maketrans('', '', string.punctuation))
    word=word.lower()
    return word

#The markov chain function expects a string without any newlines
# Assumes the file is a text file of haiku with each line of a haiku on its own line in the text file
#   and no flags or newlines between each haiku
def prepare_corpus_for_markov_chaining(filename):
    file = open(filename, mode = 'r')
    text = ""
    for line in file:
        text += line.strip()+' '
    file.close()
    return text

# Makes a list of lists.  Each haiku is it's own list of three strings, one string for each line
# Assumes the file is a text file of haiku with each line of a haiku on its own line in the text file
#   and no flags or newlines between each haiku
def prepare_corpus_as_a_list_haiku(filename):
    line_counter=0
    single_haiku = []
    # haiku_list is the name of our list which holds the haiku in their original form
    haiku_list=[]
    file = open(filename, mode = 'r')
    for line in file:
        line_counter += 1
        single_haiku.append(line)
        if line_counter == 3:
            haiku_list.append(single_haiku)
            line_counter = 0
            single_haiku=[]
    file.close()
    return haiku_list

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



def main():
    filename="corpus/spamku.txt"
    text = prepare_corpus_for_markov_chaining(filename)
    prepare_corpus_as_a_list_haiku(filename)
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


        