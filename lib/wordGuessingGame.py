from random import choice

from guess_letter import make_wordlist

wordlist = make_wordlist('./somanywords.txt')

def pick_word(wordlist):
    return choice(wordlist)

def display(word, char_found):
    for char in word:
        if char in char_found:
            print(char, end=' ')
        else:
            print('_', end=' ')

def get_selection():
    print()
    print('Please guess a letter ')
    guess = input('>> ').lower().strip()
    return guess

def got_strike(word, guess):
    if guess not in word:
        return True
    else:
        return False

def found_word(word, char_found):
    for char in word:
        if char not in char_found:
            return False
    return True


def play():
    word = pick_word(wordlist)
    char_found = []
    found = False
    strikes = 0
    while not found:
        print(f'Strikes: {strikes} ')
        display(word, char_found)
        guess = get_selection()
        if got_strike(word, guess):
            print('Strike! ')
            strikes += 1
        else:
           char_found.append(guess)
        if found_word(word, char_found):
            found = True

    print(f'Congratulations! The word was "{word}" ')

# main -------------------------------------------------------------------------
if __name__ == '__main__':
    play()
