from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""

    with open("dictionary.txt",'r') as f:
        words = f.splitlines()

    return words





def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""


    return sum(DICTIONARY[character.upper()] for character in word)


def max_word_value(words=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if words is None:
        words = load_words()


    return max(calc_word_value(word) for word in words)



if __name__ == "__main__":
    pass
