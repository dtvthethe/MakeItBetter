from collections import Counter
from re import findall
from text_utility import read

def get_most_common_used_word(str_file_path):
    '''
    Get the most commonly used word from text file
    :param str_file_path: text file path
    :return: A tuple most common used word
    '''
    return Counter(read(str_file_path).lower().split()).most_common(1)[0]

def get_words_next_to_right(str_file_path, key_word):
    '''
    Get all words next to right by the key word
    :param str_file_path: Text file path
    :param key_word: The key word
    :return: A List of words next to right by the key word
    '''
    word_next_to_rights = findall(key_word + ' [a-z]+', read(str_file_path).lower())
    return Counter(word_next_to_rights).most_common()