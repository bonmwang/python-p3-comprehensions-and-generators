#!/usr/bin/env python3

def return_evens(num_list):
    if not isinstance(num_list, (list, tuple, range)):
        raise TypeError("Input must be a sequence")
    return [num for num in num_list if num % 2 == 0]
    pass

def make_exclamation(sentence_list):
    if not isinstance(sentence_list, (list, tuple)):
        raise TypeError("Input must be a list or string")
    return [sentence + "!" for sentence in sentence_list]
    pass