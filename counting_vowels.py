def count_vowels(word):
    """
    Given a single word, return the total number of vowels in that single word

    :param word: str
    :return: int

    >>> count_vowels('Pokemon')
    3

    >>> count_vowels('Mega')
    2
    """
    total_vowels = 0
    for letter in word:
        if letter in 'aeiou':
            total_vowels += 1
    return total_vowels

if __name__  == "__main__":
    import doctest
    doctest.testmod()