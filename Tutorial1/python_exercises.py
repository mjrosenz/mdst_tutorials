"""
Intro to python exercises shell code
"""

def is_odd(x):
    if x % 2 == 1:
        return True
    else:
        return False
    """
    returns True if x is odd and False otherwise
    """


def is_palindrome(word):
    for index in range(0,len(word)//2):
        if word[index] != word[-1-index]:
            return False
    return True
    """
    returns whether `word` is spelled the same forwards and backwards
    """


def only_odds(numlist):
    new_list = []
    for num in numlist:
        if num % 2 == 1:
            new_list.append(num)
    return new_list
    """
    returns a list of numbers that are odd from numlist

    ex: only_odds([1, 2, 3, 4, 5, 6]) -> [1, 3, 5]
    """


def count_words(text):
    text = text.lower()
    words = {}
    for word in text.split():
        if word not in words:
            words[word] = 1
        words[word] += 1
    return words

    """
    return a dictionary of {word: count} in the text

    words should be split by spaces (and nothing else)
    words should be converted to all lowercase

    ex: count_words("How much wood would a woodchuck chuck"
                    " if a woodchuck could chuck wood?")
        ->
        {'how': 1, 'much': 1, 'wood': 1, 'would': 1, 'a': 2, 'woodchuck': 2,
        'chuck': 2, 'if': 1, 'could': 1, 'wood?': 1}
<<<<<<< HEAD
    """
=======
    """>>>>>>> 4cacadd03f88845ab300319124192975af91a09d
