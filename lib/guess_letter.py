#!/bin/#!/usr/bin/env python3

# guess_letter.py
# Michael Cole
# ------------------------------------------------------------------------------

# Read in somanywords.txt
def make_wordlist(word_file):
    with open(word_file) as textfile:
        original_wordlist = textfile.readlines()
    # remove whitespace
    wordlist = []
    for word in original_wordlist:
        stripped_word = word.strip()
        wordlist.append(stripped_word)
    return wordlist

def get_input_word():
    print()
    print('Input the current string (Use underscores for blanks) ')
    input_word = input('string: ').strip()
    return input_word

def length_based(input_word, wordlist):
    narrowed_list = []
    for word in wordlist:
        if len(word) == len(input_word):
            narrowed_list.append(word)
    return narrowed_list

def char_based(input_word, wordlist):
    narrowed_list = []
    for word in wordlist:
        wordcheck = True
        for idx,char in enumerate(input_word):
            if char == '_':
                pass
            elif char == word[idx]:
                pass    
            else:
                wordcheck = False
        if wordcheck:
            narrowed_list.append(word)
    return narrowed_list


def freq_based(wordlist, chars_used):
    original_letter_dict = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0,
                   'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0,
                   'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0,
                   'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}

    # remove used characters
    letter_dict = {}
    for letter,count in original_letter_dict.items():
        if letter not in chars_used:
            letter_dict[letter] = count

    # tally up characters
    for word in wordlist:
        for char in word:
            if char in letter_dict:
                letter_dict[char] += 1

    # Choose most frequent character
    most_frequent_char = ('null', -1)
    for char,value in letter_dict.items():
        if value > most_frequent_char[1]:
           most_frequent_char = (char, value)
    return most_frequent_char[0]

# Run --------------------------------------------------------------------------
def run():
    wordlist = make_wordlist('./somanywords.txt')
    print(f'There are {len(wordlist)} words left.')
    found = False
    chars_used = []
    while not found:
        input_word = get_input_word()
        narrowed_list = length_based(input_word, wordlist)
        narrowed_list = char_based(input_word, narrowed_list)
        if len(narrowed_list) == 1:
            print(f'Word found! The word is: {narrowed_list[0]} ')
            found = True
        else:
            most_frequent_char = freq_based(narrowed_list, chars_used)
            chars_used.append(most_frequent_char)
            print(f'You should choose "{most_frequent_char}" this time.')
        print(f'There are {len(narrowed_list)} words left.')
    print('Congratulations!')


if __name__ == '__main__':
    run()
