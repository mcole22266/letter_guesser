#!/usr/bin/env python3

# guess_letter.py
# Michael Cole
# ------------------------------------------------------------------------------
def make_wordlist(wordfile):
    with open(wordfile) as textfile:
        wordlist_whitespaces = textfile.readlines()
    # remove whitespaces
    wordlist = []
    for word in wordlist_whitespaces:
        stripped_word = word.strip()
        wordlist.append(stripped_word)
    return wordlist

def wordfound(wordlist):
    if len(wordlist) == 1:
        return True
    else:
        return False

def get_string():
    print()
    print(f'Input the current string (Use underscores for blanks) ')
    string = input('string: ').strip()
    return string

def filter_wordlength(string, wordlist):
    filtered_wordlist = []
    for word in wordlist:
        if len(word) == len(string):
            filtered_wordlist.append(word)
    return filtered_wordlist

def filter_charnotfound(chars_notfound, wordlist):
    filtered_wordlist = []
    for word in wordlist:
        word_passedfiltration = True
        for wordchar in word:
            if wordchar in chars_notfound:
                word_passedfiltration = False
        if word_passedfiltration:
            filtered_wordlist.append(word)
    return filtered_wordlist


def filter_charlocation(string, wordlist):
    filtered_wordlist = []
    for word in wordlist:
        word_passedfiltration = True
        for idx,char in enumerate(string):
            if char == '_':
                pass
            elif char != word[idx]:
                word_passedfiltration = False
        if word_passedfiltration:
            filtered_wordlist.append(word)
    return filtered_wordlist

def suggested_char(chars_used, wordlist):
    char_dict_all = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0, 'g': 0,
                   'h': 0, 'i': 0, 'j': 0, 'k': 0, 'l': 0, 'm': 0, 'n': 0,
                   'o': 0, 'p': 0, 'q': 0, 'r': 0, 's': 0, 't': 0, 'u': 0,
                   'v': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
    # remove used characters
    char_dict = {}
    for char in char_dict_all.keys():
        if char not in chars_used :
            char_dict[char] = 0
    # tally up characters
    for word in wordlist:
        for char in word:
            if char in char_dict:
                char_dict[char] += 1
    # most frequent char
    most_frequent_char = ('null', -1)
    for char,value in char_dict.items():
        if value > most_frequent_char[1]:
            most_frequent_char = (char,value)
    print()
    print(f"I suggest you pick '{most_frequent_char[0]}'.")
    return most_frequent_char[0]

def printnumwords(wordlist):
    print()
    if len(wordlist) == 1:
        print(f'There is {len(wordlist)} word left!')
    else:
        print(f'There are {len(wordlist)} words left.')

def complete(wordlist):
    print()
    print(f'Congratulations! The word is {wordlist[0]}.')


# Run --------------------------------------------------------------------------
def run():
    wordlist = make_wordlist('./somanywords.txt')
    printnumwords(wordlist)
    chars_found = []
    chars_notfound = []
    string = get_string()
    previous_string = None
    while not wordfound(wordlist):
        chars_used = chars_found + chars_notfound
        wordlist = filter_wordlength(string, wordlist)
        wordlist = filter_charnotfound(chars_notfound, wordlist)
        wordlist = filter_charlocation(string, wordlist)
        if wordfound(wordlist):
            break
        printnumwords(wordlist)
        char = suggested_char(chars_used, wordlist)
        previous_string = string
        string = get_string()
        if previous_string == string:
            chars_notfound.append(char)
        else:
            chars_found.append(char)
    complete(wordlist)



if __name__ == '__main__':
    run()
