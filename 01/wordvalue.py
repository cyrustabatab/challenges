from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""

    with open(DICTIONARY,'r') as f:
        words = f.read().splitlines()

    return words





def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""


    return sum(LETTER_SCORES.get(character.upper(),0) for character in word)


def max_word_value(words=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if words is None:
        words = load_words()
    
    max_word = None
    max_score = float("-inf")

    for word in words:
        score = calc_word_value(word)
        if score > max_score:
            max_score = score
            max_word = word

    return max_word


if __name__ == "__main__":
    pass
