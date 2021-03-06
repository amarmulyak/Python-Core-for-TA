"""
Provide full program code of count_symbols(word) function which returns the dict with following structure:
{<symbol_1>: <number_in_word>, <symbol_2>: <number_in_word>,.....} or false when wrong input value.
word - type str.
EXAMPLE OF Inputs/Ouputs when using this function:
print count_symbols("abracadabra")
{'a': 5, 'r': 2, 'b': 2, 'c': 1, 'd': 1}
print count_symbols("100500")
{'1': 1, '0': 4, '5': 1}
print count_symbols("##$$aa")
{'a': 2, '#': 2, '$': 2}
print count_symbols(125)
False
"""

#word_dict = {}

def count_symbols(word):
    if isinstance(word, str):
        word_dict = dict.fromkeys(word, 0)
        for i in word:
            word_dict[i] += 1
        return word_dict
    else:
        return False

print(count_symbols("##$$aa"))