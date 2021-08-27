import re

def remove_punct(words):
    return re.sub('\W+', '', words)

def is_polindrome(words):
    revers_word = ''.join(reversed(words))
    return remove_punct(words) == remove_punct(revers_word)


word = 'ada'


print(is_polindrome(word))